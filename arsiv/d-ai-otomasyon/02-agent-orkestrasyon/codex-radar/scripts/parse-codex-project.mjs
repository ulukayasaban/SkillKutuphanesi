#!/usr/bin/env node
// parse-codex-project.mjs — extract deterministic FACTS from local Codex sessions.
// It does NOT write prose. prepare-model-input.mjs turns these facts into the
// compact, security-bounded input used for model-authored analysis (see SKILL.md).
//
// v2.1: joins function_call/function_call_output by call_id (modern rollout format),
// classifies sessions (interactive / automation / subagent), computes the baseline
// formulas in code, and emits evidenceAtoms / workflowEpisodes / criticalIncidents
// plus a modernToolSummary and parserCoverage drift detector.
import fs from "node:fs";
import path from "node:path";
import {
  allSessionFiles,
  cleanupOldFiles,
  clip,
  CODEX_HOME,
  countBy,
  displayNameFromCwd,
  fileExists,
  loadRubric,
  loadSessionMetasCached,
  loadThreadIndex,
  normalizePath,
  RADAR_HOME,
  redactSensitiveText,
  ratio,
  topCounts,
  writeFilePrivate
} from "./lib.mjs";
import { normalizeCommand } from "./signals.mjs";
import { buildProjectCatalog, resolveProject } from "./project-selection.mjs";
import { createAnalysisWindow, sessionInWindow } from "./analysis-window.mjs";
import { collectSessions, PARSER_VERSION } from "./session-parser.mjs";
import { computeBaselines, FORMULA_VERSION } from "./scoring.mjs";
import { fileURLToPath } from "node:url";

const SKILL_DIR = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const rubric = loadRubric(SKILL_DIR);

function usage() {
  console.error("Usage: node parse-codex-project.mjs <project-cwd> [--privacy standard|strict] [--days N | --since YYYY-MM-DD] [--until YYYY-MM-DD]");
  process.exit(2);
}

function parseArgs(argv) {
  const parsed = { projectCwd: null, privacyMode: "standard" };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (["--days", "--since", "--until"].includes(arg)) {
      parsed[arg.slice(2)] = arg === "--days" ? Number(argv[index + 1]) : argv[index + 1];
      if (argv[index + 1] == null) usage();
      index += 1;
    } else if (arg === "--privacy") {
      parsed.privacyMode = argv[index + 1];
      index += 1;
    } else if (arg.startsWith("--privacy=")) {
      parsed.privacyMode = arg.slice("--privacy=".length);
    } else if (!arg.startsWith("--") && !parsed.projectCwd) {
      parsed.projectCwd = arg;
    } else usage();
  }
  if (!["standard", "strict"].includes(parsed.privacyMode)) usage();
  return parsed;
}

const cli = parseArgs(process.argv.slice(2));
let projectCwd = normalizePath(cli.projectCwd);
if (!projectCwd) usage();

let analysisWindow;
try { analysisWindow = createAnalysisWindow(cli); } catch (error) { console.error(error.message); process.exit(2); }

const threadIndex = loadThreadIndex();
const files = await allSessionFiles();
const metaMap = await loadSessionMetasCached(files);
const catalog = buildProjectCatalog(metaMap, threadIndex);
const match = resolveProject(projectCwd, catalog);
const selectionMode = match?.matchType || "exact";
if (match) projectCwd = match.cwd;
const selectedCwds = new Set(match?.selectedCwds || []);
let selected = [...metaMap].filter(([, meta]) => selectedCwds.has(normalizePath(meta.cwd)))
  .map(([file, meta]) => ({ file, meta }));
const matchedSessionCount = selected.length;
selected = selected.filter(entry => sessionInWindow(entry.meta, analysisWindow));

if (selected.length === 0) {
  console.error(`No Codex sessions found in the selected window for cwd: ${projectCwd}`);
  process.exit(1);
}

const state = await collectSessions(selected, {
  cwd: projectCwd, selectionMode, privacyMode: cli.privacyMode, threadIndex
});

if (state.sessions.length === 0) {
  console.error(`All ${selected.length} sessions for this cwd are subagent threads — nothing user-authored to evaluate.`);
  process.exit(1);
}

const facts = buildFacts(state);
facts.computedBaselines = computeBaselines(facts);

const tempDir = path.join(RADAR_HOME, "temp");
cleanupOldFiles(tempDir, {
  prefixes: ["codex-facts-", "codex-model-input-", "codex-analysis-", "codex-report-"]
});
const stamp = new Date().toISOString().replace(/[:.]/g, "-");
const factsPath = path.join(tempDir, `codex-facts-${stamp}.json`);
writeFilePrivate(factsPath, JSON.stringify(facts, null, 2) + "\n");

console.log(JSON.stringify({
  factsPath,
  project: facts.project.displayName,
  profile: facts.projectProfile.label,
  profileType: facts.projectProfile.type,
  sessions: facts.project.sessionCount,
  subagentSessionsExcluded: facts.subagentActivity.sessionCount,
  automationShare: facts.projectProfile.automationShare,
  humanMessages: facts.stats.humanMessages,
  confidence: facts.confidenceLevel,
  dominantLanguage: facts.dominantLanguage,
  privacyMode: facts.privacyMode,
  parserWarnings: facts.parserWarnings
}, null, 2));

// ---------------------------------------------------------------------------
// State
// ---------------------------------------------------------------------------

// ---------------------------------------------------------------------------
// Facts assembly
// ---------------------------------------------------------------------------

function buildFacts(state) {
  const stats = buildStats(state);
  const toolcraftSummary = buildToolcraft(state, stats);
  const outcomeTotals = buildOutcomes(state, stats);
  const projectAssets = inspectProjectAssets(state.cwd);
  const projectProfile = classifyProject(state, stats, outcomeTotals, projectAssets);
  const confidence = computeConfidence(state, stats);
  const dominantLanguage = detectLanguage(state.humanMessages);
  const evidence = buildEvidence(state);
  const modernToolSummary = buildModernToolSummary(state);
  const parserCoverage = buildParserCoverage(state);
  const parserWarnings = buildParserWarnings(state, parserCoverage, toolcraftSummary);
  const selfBaseline = loadSelfBaseline();

  return {
    schemaVersion: "facts-2.1",
    formulaVersion: FORMULA_VERSION,
    generatedAt: new Date().toISOString(),
    privacyMode: state.privacyMode,
    analysisWindow,
    analyzedSessionIds: state.sessions.map(session => session.id).sort(),
    source: { codexHome: CODEX_HOME, selectionMode: state.selectionMode, selectedCwds: [...selectedCwds], matchedSessions: matchedSessionCount, windowSessions: selected.length, parserVersion: PARSER_VERSION },
    project: {
      cwd: state.cwd,
      displayName: displayNameFromCwd(state.cwd),
      sessionCount: state.sessions.length,
      firstActiveAt: minDate(state.sessions.map((session) => session.timestamp)),
      lastActiveAt: maxDate(state.sessions.flatMap(session => [session.updatedAt, session.lastEventAt, session.timestamp])),
      sessionKinds: countBy(state.sessions, (session) => session.kind)
    },
    projectProfile,
    projectAssets,
    stats,
    toolcraftSummary,
    modernToolSummary,
    outcomeTotals,
    signalsByPosition: state.signals,
    subagentActivity: {
      sessionCount: state.subagent.sessionCount,
      byRole: state.subagent.byRole,
      toolCalls: state.subagent.toolCalls,
      edits: state.subagent.edits,
      nicknames: [...state.subagent.nicknames].slice(0, 10)
    },
    confidenceLevel: confidence.level,
    signalDensity: confidence.signalDensity,
    outcomeDensity: confidence.outcomeDensity,
    dominantLanguage,
    keyMessages: evidence.keyMessages,
    evidenceAtoms: evidence.atoms,
    workflowEpisodes: evidence.episodes,
    criticalIncidents: evidence.incidents,
    sessionFlows: evidence.episodes.map((episode) => ({
      id: episode.sessionId,
      threadName: episode.threadName,
      humanMessages: episode.humanMessages,
      toolCalls: episode.toolCalls,
      edits: episode.edits,
      proofCommands: episode.proofPassed + episode.proofFailed + episode.proofUnknown,
      completedTurns: episode.completedTurns,
      abortedTurns: episode.aborts
    })),
    parserCoverage,
    parserWarnings,
    selfBaseline
  };
}

function buildStats(state) {
  const humanMessages = state.humanMessages.length;
  const totalChars = state.humanMessages.reduce((sum, message) => sum + message.text.length, 0);
  return {
    sessions: state.sessions.length,
    humanMessages,
    assistantMessages: state.assistantMessages,
    agentMessages: state.agentMessages,
    totalToolCalls: state.toolCalls.length,
    shellCommandCount: state.allShellCommands.length,
    patchEventCount: state.patchEvents.length,
    turnStarts: state.turnStarts,
    turnCompletes: state.turnCompletes,
    turnAborts: state.turnAborts,
    silentDrops: state.sessions.reduce((sum, session) => sum + Math.max(0, session.startedTurns - session.completedTurns - session.abortedTurns), 0),
    contextCompactions: state.contextCompactions,
    errors: state.errors,
    oversizedLines: state.oversizedLines,
    imageCalls: state.counters.imageGenerationCalls,
    viewImageCalls: state.counters.viewImageCalls,
    webSearchCalls: state.counters.webSearchCalls,
    mcpCalls: state.counters.mcpCalls,
    browserCalls: state.counters.browserCalls,
    planCalls: state.counters.planUpdates,
    subagentCalls: state.counters.subagentSpawns,
    averageHumanMessageLength: humanMessages ? Math.round(totalChars / humanMessages) : 0,
    sources: [...state.sources],
    models: [...state.models]
  };
}

function buildToolcraft(state, stats) {
  const byTool = countBy(state.toolCalls, (call) => call.name);
  const byCategory = countBy(state.toolCalls, (call) => call.category);
  const commandSuccesses = state.allShellCommands.filter((command) => command.exitCode === 0).length;
  const commandFailures = state.allShellCommands.filter((command) => typeof command.exitCode === "number" && command.exitCode !== 0).length;
  const known = commandSuccesses + commandFailures;
  return {
    totalToolCalls: stats.totalToolCalls,
    byTool: topCounts(byTool, 18),
    topTools: topCounts(byTool, 10),
    byCategory: topCounts(byCategory, 12),
    commandSuccesses,
    commandFailures,
    commandsWithUnknownExit: state.unknownExitCodeCommands,
    // null when no command carried a readable exit code — formulas treat null as neutral
    commandSuccessRate: known ? commandSuccesses / known : null,
    dynamicTools: [...state.dynamicTools].sort().slice(0, 24),
    planCompletionRate: (() => {
      const sessions = state.sessions.filter(session => session.lastPlan?.total > 0);
      return sessions.length ? sessions.reduce((sum, session) => sum + ratio(session.lastPlan.completed, session.lastPlan.total), 0) / sessions.length : null;
    })(),
    planModeEntries: state.counters.planUpdates,
    planUpdates: state.counters.planUpdates,
    subagentCalls: state.counters.subagentSpawns,
    webSearchCalls: state.counters.webSearchCalls,
    imageCalls: state.counters.imageGenerationCalls,
    viewImageCalls: state.counters.viewImageCalls,
    mcpCalls: state.counters.mcpCalls,
    browserCalls: state.counters.browserCalls,
    toolSearchCalls: state.counters.toolSearchCalls
  };
}

function buildOutcomes(state, stats) {
  const proofPassed = state.sessions.reduce((sum, session) => sum + session.proofPassed, 0);
  const proofFailed = state.sessions.reduce((sum, session) => sum + session.proofFailed, 0);
  const proofUnknown = state.sessions.reduce((sum, session) => sum + session.proofUnknown, 0);
  const successfulPatches = state.patchEvents.filter((event) => event.success).length;
  const fileEditCount = state.patchEvents.filter(event => event.success).reduce((sum, event) => sum + Math.max(1, event.files.length), 0);
  const observedTurns = state.sessions.reduce((sum, session) => sum + Math.max(session.startedTurns, session.completedTurns + session.abortedTurns), 0);
  const turnDenominator = Math.max(1, observedTurns);
  return {
    fileEditCount,
    distinctFilesTouched: state.filesTouched.size,
    successfulPatches,
    patchResults: {
      attempted: state.patchEvents.length,
      succeeded: successfulPatches,
      failed: state.patchEvents.filter(event => event.status === "failed").length,
      unknown: state.patchEvents.filter(event => event.status === "unknown").length
    },
    verification: verificationMetrics(state.sessions),
    proofCommands: { total: proofPassed + proofFailed + proofUnknown, passed: proofPassed, failed: proofFailed, unknown: proofUnknown },
    observedTurns,
    cleanEndRatio: ratio(stats.turnCompletes, turnDenominator),
    editsPerHumanMsg: ratio(fileEditCount, stats.humanMessages),
    toolsPerHumanMsg: ratio(stats.totalToolCalls, stats.humanMessages),
    filesPerHumanMsg: ratio(state.filesTouched.size, stats.humanMessages),
    abortRatio: ratio(stats.turnAborts + stats.silentDrops, turnDenominator)
  };
}

function verificationMetrics(sessions) {
  const edited = sessions.filter(session => session.edits > 0);
  const verified = edited.filter(session => session.proofAfterEdit).length;
  const passed = edited.filter(session => session.passedAfterEdit).length;
  const failed = sessions.filter(session => session.proofFailed > 0);
  const recovered = failed.filter(session => session.recoveredProofFailure).length;
  const observed = sessions.filter(session => session.proofPassed + session.proofFailed + session.proofUnknown > 0);
  const observedPassed = sessions.filter(session => session.proofPassed > 0);
  return {
    editedSessions: edited.length,
    verifiedEditedSessions: verified,
    passedEditedSessions: passed,
    coverage: edited.length ? ratio(verified, edited.length) : null,
    passingCoverage: edited.length ? ratio(passed, edited.length) : null,
    failedSessions: failed.length,
    recoveredSessions: recovered,
    recoveryRate: failed.length ? ratio(recovered, failed.length) : null,
    observedCoverage: ratio(observed.length, sessions.length),
    observedPassingCoverage: ratio(observedPassed.length, sessions.length)
  };
}

function inspectProjectAssets(cwd) {
  const resolved = fileExists(cwd);
  const has = (relativePath) => resolved && fileExists(path.join(cwd, relativePath));
  const entries = resolved ? safeReaddir(cwd) : [];
  const manifestRules = [
    ["javascript", /^(package\.json|deno\.jsonc?|bun\.lockb?)$/i],
    ["python", /^(pyproject\.toml|requirements(?:\.[^.]+)?\.txt|setup\.py|Pipfile)$/i],
    ["rust", /^Cargo\.toml$/i],
    ["go", /^go\.mod$/i],
    ["java", /^(pom\.xml|build\.gradle(?:\.kts)?|settings\.gradle(?:\.kts)?)$/i],
    ["dotnet", /\.(?:sln|csproj|fsproj|vbproj)$/i],
    ["swift", /^(Package\.swift|.*\.xcodeproj|.*\.xcworkspace)$/i],
    ["ruby", /^(Gemfile|Rakefile|.*\.gemspec)$/i],
    ["php", /^composer\.json$/i],
    ["elixir", /^mix\.exs$/i],
    ["dart", /^pubspec\.yaml$/i],
    ["cpp", /^(CMakeLists\.txt|meson\.build)$/i]
  ];
  const manifestFiles = [];
  const detectedStacks = new Set();
  for (const entry of entries) {
    for (const [stack, pattern] of manifestRules) {
      if (!pattern.test(entry)) continue;
      manifestFiles.push(entry);
      detectedStacks.add(stack);
      break;
    }
  }
  const hasPackageJson = entries.some((entry) => /^package\.json$/i.test(entry));
  const hasPyproject = entries.some((entry) => /^pyproject\.toml$/i.test(entry));
  const hasCargoToml = entries.some((entry) => /^Cargo\.toml$/i.test(entry));
  return {
    cwdResolved: resolved,
    hasAgentsMd: has("AGENTS.md"),
    hasClaudeMd: has("CLAUDE.md"),
    hasCodexDir: has(".codex"),
    hasAgentsDir: has(".agents"),
    hasGit: has(".git"),
    hasPackageJson,
    hasPyproject,
    hasCargoToml,
    hasManifest: manifestFiles.length > 0,
    manifestFiles: manifestFiles.slice(0, 12),
    detectedStacks: [...detectedStacks].sort(),
    hasReadme: entries.some((entry) => /^readme\.(md|txt)$/i.test(entry)),
    hasTestsDir: resolved && hasTestAssets(cwd),
    rootEntryCount: entries.length
  };
}

function safeReaddir(dir) {
  try {
    return fs.readdirSync(dir);
  } catch {
    return [];
  }
}

function hasTestAssets(root, maxDepth = 2) {
  const ignored = new Set([
    ".git", ".hg", ".svn", "node_modules", "vendor", "Pods", ".build",
    "build", "dist", "coverage", "target", ".venv", "venv"
  ]);
  const queue = [{ dir: root, depth: 0 }];
  while (queue.length) {
    const { dir, depth } = queue.shift();
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true }).slice(0, 500);
    } catch {
      continue;
    }
    for (const entry of entries) {
      if (entry.isDirectory()) {
        if (/^(test|tests|__tests__|spec|specs|uitests|integration-tests?)$/i.test(entry.name)) return true;
        if (depth < maxDepth && !ignored.has(entry.name)) {
          queue.push({ dir: path.join(dir, entry.name), depth: depth + 1 });
        }
      } else if (
        /\.(?:test|spec)\.[cm]?[jt]sx?$/i.test(entry.name)
        || /_test\.go$/i.test(entry.name)
        || /(?:Tests?|Spec)\.swift$/i.test(entry.name)
        || /(?:Test|Tests)\.(?:cs|fs|java|kt|rb|php|py)$/i.test(entry.name)
      ) {
        return true;
      }
    }
  }
  return false;
}

function classifyProject(state, stats, outcomes, assets) {
  const automationSessions = state.sessions.filter((session) => session.kind === "automation").length;
  const automationShare = ratio(automationSessions, state.sessions.length);
  let type;
  let rationale;
  if (automationShare >= 0.6) {
    type = "automation";
    rationale = {
      en: `${Math.round(automationShare * 100)}% of sessions are non-interactive codex exec runs, so this is judged as an automation pipeline.`,
      zh: `${Math.round(automationShare * 100)}% 的会话是非交互式 codex exec 运行，因此按自动化流水线评估。`
    };
  } else if (outcomes.fileEditCount === 0 && stats.humanMessages >= 4 && outcomes.proofCommands?.total === 0) {
    type = "learning";
    rationale = {
      en: "Conversation-heavy sessions with no file edits or proof runs indicate learning or exploration.",
      zh: "会话以讨论为主，没有文件编辑或验证运行，符合学习探索型项目。"
    };
  } else if (stats.sessions >= 5 || stats.contextCompactions >= 2 || stats.humanMessages >= 30) {
    type = "long_running";
    rationale = {
      en: "Multiple sessions, many messages, or context compactions indicate sustained collaboration.",
      zh: "多个会话、大量消息或上下文压缩表明这是持续协作项目。"
    };
  } else if (outcomes.fileEditCount >= 4 || outcomes.distinctFilesTouched >= 3) {
    type = "feature_build";
    rationale = {
      en: "The edit volume and number of touched files indicate implementation work.",
      zh: "文件编辑量和触及文件数量表明这是实现型工作。"
    };
  } else {
    type = "one_shot";
    rationale = {
      en: "The small number of sessions and messages fits a focused one-shot task.",
      zh: "会话和消息数量较少，符合聚焦的一次性任务。"
    };
  }
  const profile = rubric.profiles[type] || rubric.profiles.one_shot;
  const naDimensions = [...(profile.naDimensions || [])];
  if (!assets.cwdResolved && !naDimensions.includes("architecture")) naDimensions.push("architecture");
  return {
    type,
    label: profile.label,
    rationale,
    automationShare: Math.round(automationShare * 100) / 100,
    categoryWeights: profile.categoryWeights,
    naDimensions
  };
}

function computeConfidence(state, stats) {
  const humanMessages = stats.humanMessages || 0;
  const directing = state.signals.directing;
  const signalSum = Object.values(directing.counts).reduce((sum, value) => sum + value, 0);
  const signalDensity = humanMessages ? signalSum / humanMessages : 0;
  const outcomeDensity = humanMessages ? stats.totalToolCalls / humanMessages : 0;
  let level = "high";
  if (humanMessages < 5) {
    level = "low";
  } else if (humanMessages < 20 && signalDensity < 1.2 && outcomeDensity < 2) {
    level = "low";
  } else if (humanMessages < 40 && (signalDensity < 1.2 || outcomeDensity < 1)) {
    level = "medium";
  } else if (humanMessages < 50) {
    level = "medium";
  }
  return { level, signalDensity: round2(signalDensity), outcomeDensity: round2(outcomeDensity) };
}

function detectLanguage(messages) {
  let cjk = 0;
  let letters = 0;
  let msgWithCjk = 0;
  for (const message of messages) {
    const stripped = String(message.text || "")
      .replace(/```[\s\S]*?```/g, " ")
      .replace(/`[^`]*`/g, " ")
      .replace(/[\w@./:-]+\.[a-z0-9]+/gi, " ");
    const cjkChars = (stripped.match(/[一-鿿]/g) || []).length;
    const letterChars = (stripped.match(/[a-zA-Z一-鿿]/g) || []).length;
    cjk += cjkChars;
    letters += letterChars;
    if (cjkChars > 0) msgWithCjk += 1;
  }
  const charRatio = letters ? cjk / letters : 0;
  const msgRatio = messages.length ? msgWithCjk / messages.length : 0;
  return charRatio > 0.15 || msgRatio > 0.3 ? "zh" : "en";
}

// ---------------------------------------------------------------------------
// Evidence pipeline v2: atoms, episodes, incidents, stratified key messages
// ---------------------------------------------------------------------------

function messageInterestScore(message) {
  const f = message.features;
  return (f.correction ? 4 : 0) + (f.errorLog ? 3 : 0) + (f.asksVerify ? 2 : 0)
    + (f.codeOrData ? 2 : 0) + (f.constraints ? 1 : 0) + (f.expectedBehavior ? 1 : 0)
    + (f.filePath ? 1 : 0) + Math.min(2, message.text.length / 300);
}

function buildEvidence(state) {
  const evidenceText = (message, max) => {
    if (state.privacyMode === "strict") {
      const features = Object.keys(message.features || {}).filter((key) => message.features[key]);
      return `[content omitted in strict mode; signals: ${features.join(", ") || "none"}]`;
    }
    return clip(redactSensitiveText(message.text), max);
  };
  const commandText = (command, max) => state.privacyMode === "strict"
    ? "[command omitted in strict mode]"
    : clip(redactSensitiveText(command), max);

  // --- stratified key messages across three time windows ---
  const all = state.humanMessages;
  const interesting = all.filter((message) => messageInterestScore(message) >= 1);
  const third = Math.max(1, Math.ceil(all.length / 3));
  const windows = [[], [], []];
  for (const message of interesting) {
    windows[Math.min(2, Math.floor(message.index / third))].push(message);
  }
  const picked = [];
  for (const window of windows) {
    window.sort((a, b) => messageInterestScore(b) - messageInterestScore(a));
    picked.push(...window.slice(0, 10));
  }
  picked.sort((a, b) => a.index - b.index);
  const selected = picked.slice(0, 30);

  // --- evidence atoms: selected messages + notable shell failures + aborts ---
  const atoms = [];
  let atomSeq = 0;
  const atomIdByMessageIndex = new Map();
  for (const message of selected) {
    const id = `a${++atomSeq}`;
    atomIdByMessageIndex.set(message.index, id);
    atoms.push({
      id,
      role: "user",
      sessionId: message.sessionId,
      timestamp: message.timestamp,
      snippet: evidenceText(message, 400),
      features: Object.keys(message.features).filter((key) => message.features[key]),
      after: message.after
    });
  }

  const failedShell = state.allShellCommands.filter((command) => typeof command.exitCode === "number" && command.exitCode !== 0);
  const failuresByCommand = new Map();
  for (const shell of failedShell) {
    const key = normalizeCommand(shell.command);
    const entry = failuresByCommand.get(key) || { command: key, failures: 0, sessions: new Set(), lastExitCode: shell.exitCode };
    entry.failures += 1;
    entry.sessions.add(shell.sessionId);
    entry.lastExitCode = shell.exitCode;
    failuresByCommand.set(key, entry);
  }
  const topFailures = [...failuresByCommand.values()].sort((a, b) => b.failures - a.failures).slice(0, 8);
  const failureAtomIds = new Map();
  for (const failure of topFailures) {
    const id = `a${++atomSeq}`;
    failureAtomIds.set(failure.command, id);
    atoms.push({
      id,
      role: "shell",
      sessionId: [...failure.sessions][0] || null,
      timestamp: null,
      snippet: `${commandText(failure.command, 160)} → exit ${failure.lastExitCode} (${failure.failures}× failed)`,
      features: ["commandFailure"],
      after: null
    });
  }

  // --- critical incidents ---
  const incidents = [];
  let incidentSeq = 0;
  const addIncident = (incident) => incidents.push({ id: `i${++incidentSeq}`, ...incident });
  for (const failure of topFailures.filter((entry) => entry.failures >= 2).slice(0, 4)) {
    addIncident({
      type: "command_retry_churn",
      summary: `Command failed ${failure.failures}× across ${failure.sessions.size} session(s): ${commandText(failure.command, 120)}`,
      sessionIds: [...failure.sessions].slice(0, 3),
      evidenceRefs: [failureAtomIds.get(failure.command)].filter(Boolean)
    });
  }
  const correctionMessages = selected.filter((message) => message.features.correction)
    .sort((a, b) => messageInterestScore(b) - messageInterestScore(a))
    .slice(0, 4);
  for (const message of correctionMessages) {
    addIncident({
      type: "correction",
      summary: `User course-corrected: ${evidenceText(message, 140)}`,
      sessionIds: [message.sessionId],
      evidenceRefs: [atomIdByMessageIndex.get(message.index)].filter(Boolean)
    });
  }
  const abortedSessions = state.sessions.filter((session) => session.abortedTurns > 0).slice(0, 2);
  for (const session of abortedSessions) {
    addIncident({
      type: "aborted_turns",
      summary: `${session.abortedTurns} aborted turn(s) in session ${
        state.privacyMode === "strict" ? session.id : (session.threadName || session.id)
      }`,
      sessionIds: [session.id],
      evidenceRefs: []
    });
  }
  if (state.contextCompactions >= 2) {
    addIncident({
      type: "context_pressure",
      summary: `${state.contextCompactions} context compactions across the project — sessions run long enough to lose context.`,
      sessionIds: [],
      evidenceRefs: []
    });
  }

  // --- workflow episodes: last 20 sessions + earlier ones with trouble ---
  const chronological = [...state.sessions].sort((a, b) => new Date(a.timestamp || 0) - new Date(b.timestamp || 0));
  const tail = chronological.slice(-20);
  const troubled = chronological.slice(0, -20).filter((session) => session.abortedTurns > 0 || session.failedCommands >= 3);
  const episodeSessions = [...troubled.slice(-8), ...tail];
  const episodes = episodeSessions.map((session) => ({
    sessionId: session.id,
    kind: session.kind,
    threadName: state.privacyMode === "strict" ? null : session.threadName,
    startedAt: session.timestamp,
    endedAt: session.lastEventAt,
    durationMinutes: durationMinutes(session.timestamp, session.lastEventAt),
    humanMessages: session.humanMessages,
    toolCalls: session.toolCalls,
    edits: session.edits,
    proofPassed: session.proofPassed,
    proofFailed: session.proofFailed,
    proofUnknown: session.proofUnknown,
    failedCommands: session.failedCommands,
    completedTurns: session.completedTurns,
    aborts: session.abortedTurns,
    planUpdates: session.planUpdates,
    planCompletion: session.lastPlan,
    corrections: session.corrections,
    firstUserMessage: state.privacyMode === "strict" ? null : session.firstUserMessage,
    lastAgentMessage: state.privacyMode === "strict" ? null : session.lastAgentMessage
  }));

  const keyMessages = selected.map((message) => ({
    timestamp: message.timestamp,
    sessionId: message.sessionId,
    atomId: atomIdByMessageIndex.get(message.index),
    text: evidenceText(message, 400),
    features: Object.keys(message.features).filter((key) => message.features[key]),
    after: message.after
  }));

  return { keyMessages, atoms, episodes, incidents: incidents.slice(0, 12) };
}

function buildModernToolSummary(state) {
  const mcpByServer = {};
  for (const [server, entry] of state.mcpByServer) {
    mcpByServer[server] = {
      calls: entry.calls,
      errors: entry.errors,
      tools: topCounts(entry.tools, 8)
    };
  }
  const lifecycle = state.subagentLifecycle;
  const closed = lifecycle.closeTargets.size;
  const planSessions = state.sessions.filter((session) => session.lastPlan);
  const planCompletionAvg = planSessions.length
    ? round2(planSessions.reduce((sum, session) => sum + ratio(session.lastPlan.completed, Math.max(1, session.lastPlan.total)), 0) / planSessions.length)
    : null;
  return {
    mcpByServer,
    subagentLifecycle: {
      spawned: lifecycle.spawned,
      waited: lifecycle.waitTargets.size,
      closed,
      orphanedEstimate: Math.max(0, lifecycle.spawned - closed)
    },
    plans: {
      updates: state.counters.planUpdates,
      sessionsWithPlan: planSessions.length,
      planCompletionAvg
    },
    goals: {
      goalToolCalls: state.counters.goalCalls,
      threadGoalEvents: state.counters.threadGoalEvents
    },
    toolSearch: { calls: state.counters.toolSearchCalls },
    skillReads: topCounts(Object.fromEntries(state.skillReads), 8),
    web: {
      searches: state.counters.webSearchCalls,
      topQueries: state.webQueries.slice(0, 5)
    },
    images: {
      generated: state.counters.imageGenerationCalls,
      viewed: state.counters.viewImageCalls
    },
    nodeRepl: { jsCalls: state.counters.nodeReplCalls },
    contextHygiene: {
      compactions: state.contextCompactions,
      oversizedLines: state.oversizedLines,
      maxContextUsedPct: round2(state.maxContextUsedPct)
    }
  };
}

function buildParserCoverage(state) {
  const unknownTotal = [...state.unknownTypes.values()].reduce((sum, value) => sum + value, 0);
  return {
    eventsTotal: state.eventTotal,
    eventsUnknown: unknownTotal,
    unknownTypes: topCounts(Object.fromEntries(state.unknownTypes), 8),
    coverageRatio: state.eventTotal ? round2(1 - unknownTotal / state.eventTotal) : 1
  };
}

function buildParserWarnings(state, coverage, toolcraft) {
  const warnings = [];
  if (coverage.eventsTotal > 200 && coverage.coverageRatio < 0.9) {
    warnings.push(`Parser coverage is ${Math.round(coverage.coverageRatio * 100)}% — the Codex rollout format may have drifted; consider updating codex-radar.`);
  }
  if (state.unknownExitCodeCommands > 0) {
    warnings.push(`${state.unknownExitCodeCommands} shell command output(s) had no recognizable exit-code format; command success rate covers the rest.`);
  }
  if (toolcraft.commandSuccessRate === null && state.allShellCommands.length > 0) {
    warnings.push("No shell command carried a readable exit code — success-rate signals were treated as neutral.");
  }
  if (state.oversizedLines > 0) {
    warnings.push(`${state.oversizedLines} oversized session line(s) (>2MB) were only partially parsed.`);
  }
  return warnings;
}

function loadSelfBaseline() {
  const baselinePath = path.join(RADAR_HOME, "cache", "self-baseline.json");
  try {
    const raw = JSON.parse(fs.readFileSync(baselinePath, "utf8"));
    if (raw && raw.schemaVersion === "self-baseline-1" && raw.parserVersion === PARSER_VERSION) return raw;
  } catch { /* absent or unreadable — fine */ }
  return null;
}

// ---------------------------------------------------------------------------
// Small helpers
// ---------------------------------------------------------------------------

function durationMinutes(start, end) {
  const a = new Date(start || 0).getTime();
  const b = new Date(end || 0).getTime();
  if (!a || !b || b < a) return null;
  return Math.round((b - a) / 60000);
}

function round2(value) {
  return Math.round((Number.isFinite(value) ? value : 0) * 100) / 100;
}

function minDate(values) {
  const dates = values.filter(Boolean).map((value) => new Date(value)).filter((date) => !Number.isNaN(date.getTime()));
  if (!dates.length) return null;
  return new Date(Math.min(...dates.map((date) => date.getTime()))).toISOString();
}

function maxDate(values) {
  const dates = values.filter(Boolean).map((value) => new Date(value)).filter((date) => !Number.isNaN(date.getTime()));
  if (!dates.length) return null;
  return new Date(Math.max(...dates.map((date) => date.getTime()))).toISOString();
}
