// Shared event normalization and session metrics for project reports and personal baselines.
import path from "node:path";
import { clip, eachJsonLine, extractTextContent, normalizePath, redactSensitiveText, ratio, readSessionMeta } from "./lib.mjs";
import { categorizeTool, classifyMessage, extractExitCode, filesFromPatchText, inspectProofCommand, parseExecArguments, shellCommandText, sessionKindFromMeta, skillNameFromCommand } from "./signals.mjs";

export const PARSER_VERSION = "1.4.0";

export async function collectSessions(entries, { cwd = "", selectionMode = "exact", privacyMode = "standard", threadIndex = new Map() } = {}) {
  const state = createEmptyState(cwd, selectionMode, privacyMode, threadIndex);
  for (const entry of [...entries].sort((a, b) => String(a.meta.timestamp || "").localeCompare(String(b.meta.timestamp || "")) || a.file.localeCompare(b.file))) {
    const meta = await readSessionMeta(entry.file) || entry.meta;
    const kind = sessionKindFromMeta(meta);
    if (kind === "subagent") await parseSubagentSession(entry.file, meta, state);
    else await parseSession(entry.file, meta, state, kind);
  }
  finalizeShellCommands(state);
  finalizeSignals(state);
  return state;
}

const KNOWN_PAYLOAD_TYPES = new Set([
  "task_started", "task_complete", "turn_aborted", "user_message", "agent_message",
  "message", "reasoning", "function_call", "function_call_output",
  "custom_tool_call", "custom_tool_call_output", "web_search_call", "web_search_end",
  "image_generation_call", "image_generation_end", "view_image_tool_call",
  "mcp_tool_call_begin", "mcp_tool_call_end", "collab_agent_spawn_begin", "collab_agent_spawn_end",
  "collab_close_begin", "collab_close_end", "collab_waiting_begin", "collab_waiting_end",
  "exec_command_begin", "exec_command_end", "exec_command_output_delta",
  "patch_apply_begin", "patch_apply_end", "token_count", "error", "context_compacted",
  "thread_goal_updated", "thread_name_updated", "thread_rolled_back",
  "tool_search_call", "tool_search_output", "agent_reasoning", "agent_reasoning_delta",
  "turn_diff", "plan_update", "stream_error"
]);


function createEmptyState(cwd, selectionMode, privacyMode, threadIndex) {
  return {
    cwd,
    threadIndex,
    selectionMode,
    privacyMode,
    sessions: [],
    humanMessages: [],
    assistantMessages: 0,
    agentMessages: 0,
    toolCalls: [],
    shellByCallId: new Map(),
    shellCommands: [],           // entries without a call_id
    patchEvents: [],
    patchByCallId: new Map(),
    eventSequence: 0,
    turnStarts: 0,
    turnCompletes: 0,
    turnAborts: 0,
    contextCompactions: 0,
    errors: 0,
    oversizedLines: 0,
    unknownExitCodeCommands: 0,
    tokenEvents: 0,
    maxContextUsedPct: 0,
    correctionSubstanceCount: 0,
    dynamicTools: new Set(),
    models: new Set(),
    sources: new Set(),
    filesTouched: new Set(),
    countedToolCallIds: new Set(),
    counters: {
      planUpdates: 0,
      webSearchCalls: 0,
      imageGenerationCalls: 0,
      viewImageCalls: 0,
      browserCalls: 0,
      mcpCalls: 0,
      subagentSpawns: 0,
      toolSearchCalls: 0,
      goalCalls: 0,
      threadGoalEvents: 0,
      nodeReplCalls: 0
    },
    mcpByServer: new Map(),
    subagentLifecycle: { spawned: 0, waitTargets: new Set(), closeTargets: new Set() },
    webQueries: [],
    skillReads: new Map(),
    subagent: { sessionCount: 0, byRole: {}, toolCalls: 0, edits: 0, nicknames: new Set() },
    eventTotal: 0,
    unknownTypes: new Map(),
    signals: {
      opening: emptySignalBucket(),
      directing: emptySignalBucket(),
      correcting: emptySignalBucket(),
      confirming: emptySignalBucket(),
      continuing: emptySignalBucket()
    }
  };
}

function emptySignalBucket() {
  return {
    messageCount: 0,
    counts: {
      explicitGoal: 0,
      expectedBehavior: 0,
      constraints: 0,
      filePath: 0,
      errorLog: 0,
      asksPlan: 0,
      asksVerify: 0,
      correction: 0,
      confirmation: 0,
      codeOrData: 0
    },
    ratios: {}
  };
}

// ---------------------------------------------------------------------------
// Session parsing
// ---------------------------------------------------------------------------

function newSessionRecord(file, meta, kind, threadIndex) {
  const indexed = meta.id ? threadIndex.get(meta.id) : null;
  return {
    id: meta.id || path.basename(file, ".jsonl"),
    file,
    kind,
    cwd: normalizePath(meta.cwd),
    timestamp: meta.timestamp || null,
    updatedAt: indexed?.updated_at || meta.timestamp || null,
    lastEventAt: meta.timestamp || null,
    threadName: indexed?.thread_name ? clip(redactSensitiveText(indexed.thread_name), 160) : null,
    source: typeof meta.source === "string" ? meta.source : null,
    modelProvider: meta.model_provider || null,
    humanMessages: 0,
    assistantMessages: 0,
    toolCalls: 0,
    edits: 0,
    proofPassed: 0,
    proofFailed: 0,
    proofUnknown: 0,
    failedCommands: 0,
    completedTurns: 0,
    abortedTurns: 0,
    startedTurns: 0,
    planUpdates: 0,
    lastPlan: null,
    corrections: 0,
    firstUserMessage: null,
    lastAgentMessage: null,
    currentHuman: null,
    lastEditSequence: null,
    proofAfterEdit: false,
    passedAfterEdit: false,
    recoveredProofFailure: false
  };
}

async function parseSession(file, meta, state, kind) {
  const session = newSessionRecord(file, meta, kind, state.threadIndex);
  state.sessions.push(session);
  if (meta.model_provider) state.models.add(meta.model_provider);
  const sourceLabel = typeof meta.source === "string" ? meta.source : meta.originator;
  if (sourceLabel) state.sources.add(sourceLabel);
  if (Array.isArray(meta.dynamic_tools)) {
    for (const tool of meta.dynamic_tools) {
      if (tool?.namespace && tool?.name) state.dynamicTools.add(`${tool.namespace}.${tool.name}`);
    }
  }

  const pendingExec = new Map();
  const processes = new Map(); // process session_id -> initial command
  const pendingPolls = new Map(); // polling call_id -> process session_id

  await eachJsonLine(file, (record) => {
    const payload = record.payload || {};
    state.eventSequence += 1;
    const timestamp = record.timestamp || payload.timestamp || session.timestamp;
    if (timestamp) session.lastEventAt = timestamp;
    if (payload.oversized) state.oversizedLines += 1;

    if (record.type === "turn_context") {
      if (payload.model) state.models.add(payload.model);
      return;
    }
    if (record.type === "compacted" || payload.type === "context_compacted") {
      state.contextCompactions += 1;
      return;
    }
    if (record.type === "session_meta") return;

    if (payload.type) {
      state.eventTotal += 1;
      if (!KNOWN_PAYLOAD_TYPES.has(payload.type)) {
        state.unknownTypes.set(payload.type, (state.unknownTypes.get(payload.type) || 0) + 1);
      }
    }

    switch (payload.type) {
      case "task_started":
        state.turnStarts += 1;
        session.startedTurns += 1;
        break;
      case "task_complete":
        state.turnCompletes += 1;
        session.completedTurns += 1;
        if (payload.last_agent_message) {
          // narrative only — NOT added to agentMessages (agent_message events already count)
          session.lastAgentMessage = clip(redactSensitiveText(payload.last_agent_message), 220);
        }
        break;
      case "turn_aborted":
        state.turnAborts += 1;
        session.abortedTurns += 1;
        if (session.currentHuman) session.currentHuman.after.aborts += 1;
        break;
      case "user_message":
        addHumanMessage(state, session, payload.message || "", timestamp);
        break;
      case "agent_message":
        state.agentMessages += 1;
        if (payload.message) session.lastAgentMessage = clip(redactSensitiveText(payload.message), 220);
        break;
      case "message":
        if (payload.role === "assistant") {
          const text = extractTextContent(payload.content);
          if (text) {
            state.assistantMessages += 1;
            session.assistantMessages += 1;
          }
        }
        break;
      case "function_call":
        handleFunctionCall(state, session, payload, timestamp, pendingExec, pendingPolls);
        break;
      case "custom_tool_call":
        handleCustomToolCall(state, session, payload, timestamp);
        break;
      case "function_call_output":
        handleFunctionCallOutput(state, session, payload, timestamp, pendingExec, processes, pendingPolls);
        break;
      case "custom_tool_call_output":
        handlePatchOutput(state, session, payload);
        break;
      case "web_search_call":
        state.counters.webSearchCalls += 1;
        if (payload.action?.query && state.privacyMode !== "strict") {
          state.webQueries.push(clip(redactSensitiveText(payload.action.query), 120));
        }
        addToolCall(state, session, "web_search", payload, timestamp);
        break;
      case "image_generation_call":
        state.counters.imageGenerationCalls += 1;
        addToolCall(state, session, "image_generation", payload, timestamp);
        break;
      case "view_image_tool_call":
        state.counters.viewImageCalls += 1;
        addToolCall(state, session, "view_image", payload, timestamp);
        break;
      case "mcp_tool_call_end":
        handleMcpCallEnd(state, session, payload, timestamp);
        break;
      case "collab_agent_spawn_end":
        recordSubagentSpawn(state, session, payload, timestamp, payload.call_id);
        break;
      case "exec_command_end":
        handleExecCommandEnd(state, session, payload, timestamp);
        break;
      case "patch_apply_end":
        addPatchEvent(state, session, payload, timestamp);
        break;
      case "token_count":
        state.tokenEvents += 1;
        trackContextUsage(state, payload);
        break;
      case "thread_goal_updated":
        state.counters.threadGoalEvents += 1;
        break;
      case "tool_search_call":
        state.counters.toolSearchCalls += 1;
        addToolCall(state, session, "tool_search", payload, timestamp);
        break;
      case "error":
      case "stream_error":
        state.errors += 1;
        break;
      default:
        break;
    }
  });
  for (const [callId, pending] of pendingExec) {
    upsertShellCommand(state, session, { ...pending, callId, exitCode: null });
  }
}

// Subagent threads share the project cwd but their "user messages" are written
// by the parent agent — they must not pollute communication/outcome stats.
// We only aggregate them as orchestration evidence.
async function parseSubagentSession(file, meta, state) {
  state.subagent.sessionCount += 1;
  const spawn = typeof meta.source === "object" ? meta.source?.subagent?.thread_spawn : null;
  const role = spawn?.agent_role || (typeof meta.source === "object" ? Object.keys(meta.source.subagent || {})[0] : "unknown") || "unknown";
  state.subagent.byRole[role] = (state.subagent.byRole[role] || 0) + 1;
  if (spawn?.agent_nickname) state.subagent.nicknames.add(spawn.agent_nickname);
  await eachJsonLine(file, (record) => {
    const payload = record.payload || {};
    if (payload.type === "function_call" || payload.type === "custom_tool_call") state.subagent.toolCalls += 1;
    if (payload.type === "patch_apply_end") state.subagent.edits += 1;
  });
}

// ---------------------------------------------------------------------------
// Event handlers
// ---------------------------------------------------------------------------

function addHumanMessage(state, session, text, timestamp) {
  const cleaned = String(text || "").trim();
  if (!cleaned) return;
  const features = classifyMessage(cleaned);
  const message = {
    timestamp,
    text: cleaned,
    sessionId: session.id,
    sessionKind: session.kind,
    index: state.humanMessages.length,
    sessionIndex: session.humanMessages,
    features,
    after: { toolCalls: 0, edits: 0, proofRuns: 0, failedCommands: 0, aborts: 0 }
  };
  state.humanMessages.push(message);
  session.humanMessages += 1;
  session.currentHuman = message;
  if (session.firstUserMessage === null) {
    session.firstUserMessage = clip(redactSensitiveText(cleaned), 220);
  }

  addSignals(state.signals.directing, features);
  if (message.sessionIndex < 2) addSignals(state.signals.opening, features); // per-session opening
  if (features.correction) {
    addSignals(state.signals.correcting, features);
    session.corrections += 1;
    if (features.filePath || features.errorLog || features.codeOrData) state.correctionSubstanceCount += 1;
  }
  if (features.confirmation) addSignals(state.signals.confirming, features);
  if (/^(继续|continue|go on|next|再来|接着)/i.test(cleaned)) addSignals(state.signals.continuing, features);
}

function addToolCall(state, session, name, payload, timestamp, callId = payload?.call_id) {
  if (callId) {
    const key = `${session.id}:${callId}`;
    if (state.countedToolCallIds.has(key)) return; // dedup within this session
    state.countedToolCallIds.add(key);
  }
  const toolName = name || "unknown_tool";
  const category = categorizeTool(toolName, payload);
  state.toolCalls.push({ timestamp, name: toolName, category, sessionId: session.id });
  session.toolCalls += 1;
  if (session.currentHuman) session.currentHuman.after.toolCalls += 1;
}

function handleFunctionCall(state, session, payload, timestamp, pendingExec, pendingPolls) {
  const name = (payload.name || "unknown_tool").split(".").pop();
  addToolCall(state, session, name, payload, timestamp);
  switch (name) {
    case "exec_command":
      if (payload.call_id) {
        const { command, workdir } = parseExecArguments(payload.arguments);
        pendingExec.set(payload.call_id, { command, cwd: workdir, timestamp, human: session.currentHuman, sequence: state.eventSequence });
      }
      break;
    case "write_stdin": {
      const args = parseArguments(payload.arguments);
      if (payload.call_id && args.session_id != null) pendingPolls.set(payload.call_id, String(args.session_id));
      break;
    }
    case "update_plan":
      state.counters.planUpdates += 1;
      session.planUpdates += 1;
      session.lastPlan = parsePlanArguments(payload.arguments);
      break;
    case "spawn_agent":
      recordSubagentSpawn(state, session, payload, timestamp, payload.call_id, true);
      break;
    case "wait_agent":
      for (const target of parseAgentTargets(payload.arguments)) state.subagentLifecycle.waitTargets.add(target);
      break;
    case "close_agent":
      for (const target of parseAgentTargets(payload.arguments)) state.subagentLifecycle.closeTargets.add(target);
      break;
    case "view_image":
      state.counters.viewImageCalls += 1;
      break;
    case "js":
      state.counters.nodeReplCalls += 1;
      break;
    case "web_search":
      state.counters.webSearchCalls += 1;
      break;
    case "create_goal":
    case "update_goal":
    case "get_goal":
      state.counters.goalCalls += 1;
      break;
    default:
      if (name.toLowerCase().includes("browser") || name.toLowerCase().includes("screenshot")) {
        state.counters.browserCalls += 1;
      }
      break;
  }
}

function handleCustomToolCall(state, session, payload, timestamp) {
  const name = String(payload.name || "").split(".").pop();
  addToolCall(state, session, name, payload, timestamp);
  if (name === "apply_patch") {
    mergePatch(state, session, {
      callId: payload.call_id, files: filesFromPatchText(payload.input),
      timestamp, status: "unknown", human: session.currentHuman, sequence: state.eventSequence
    });
  }
}

function parseArguments(value) {
  try { return typeof value === "object" && value ? value : JSON.parse(String(value || "{}")); }
  catch { return {}; }
}

function processIdFromOutput(output) {
  const parsed = parseArguments(output);
  const id = parsed.session_id ?? parsed.sessionId;
  if (id != null) return String(id);
  return String(output || "").match(/Process running with session ID\s+(\S+)/i)?.[1] || null;
}

function handleFunctionCallOutput(state, session, payload, timestamp, pendingExec, processes, pendingPolls) {
  const callId = payload.call_id;
  if (!callId) return;
  let pending = pendingExec.get(callId);
  let initialCallId = callId;
  if (pending) {
    pendingExec.delete(callId);
    pending = { ...pending, callId };
    const processId = processIdFromOutput(payload.output);
    if (processId) processes.set(processId, pending);
  } else if (pendingPolls.has(callId)) {
    const processId = pendingPolls.get(callId);
    pendingPolls.delete(callId);
    pending = processes.get(processId);
    initialCallId = pending?.callId;
  }
  if (!pending) return;
  const { exitCode } = extractExitCode(payload.output);
  upsertShellCommand(state, session, {
    ...pending, callId: initialCallId, timestamp: pending.timestamp || timestamp, exitCode
  });
}

function handlePatchOutput(state, session, payload) {
  const key = `${session.id}:${payload.call_id}`;
  const patch = state.patchByCallId.get(key);
  if (!patch) return;
  const result = parseArguments(payload.output);
  const text = typeof payload.output === "string" ? payload.output : JSON.stringify(payload.output || {});
  if (result.isError === true || result.success === false || /(?:^|\n)(?:Error|Failed|Patch rejected|apply_patch verification failed)\b/i.test(text)) {
    patch.status = "failed";
  } else if (result.success === true || /^Success\. Updated the following files:/i.test(text)) {
    patch.status = "succeeded";
  }
}

function handleExecCommandEnd(state, session, payload, timestamp) {
  const command = shellCommandText(payload.command);
  const parsed = Array.isArray(payload.parsed_cmd)
    ? payload.parsed_cmd.map((item) => item?.cmd).filter(Boolean).join("; ")
    : "";
  upsertShellCommand(state, session, {
    callId: payload.call_id || null,
    timestamp,
    command: command || parsed,
    cwd: payload.cwd || null,
    exitCode: typeof payload.exit_code === "number" ? payload.exit_code : null
  });
}

// Merge shell info across the two persistence formats, keyed by call_id.
function upsertShellCommand(state, session, entry) {
  const key = entry.callId ? `${session.id}:${entry.callId}` : null;
  if (key && state.shellByCallId.has(key)) {
    const target = state.shellByCallId.get(key);
    if (!target.command && entry.command) target.command = entry.command;
    if (typeof entry.exitCode === "number") target.exitCode = entry.exitCode;
    if (entry.human !== undefined) target.human = entry.human;
    if (entry.sequence !== undefined) target.sequence = entry.sequence;
    return;
  }
  const target = {
    ...entry, command: entry.command || "", cwd: entry.cwd || null,
    exitCode: typeof entry.exitCode === "number" ? entry.exitCode : null,
    human: entry.human ?? session.currentHuman,
    sequence: entry.sequence ?? state.eventSequence,
    sessionId: session.id
  };
  if (key) state.shellByCallId.set(key, target);
  else state.shellCommands.push(target);
}

function handleMcpCallEnd(state, session, payload, timestamp) {
  state.counters.mcpCalls += 1;
  const server = payload.invocation?.server || "unknown";
  const tool = payload.invocation?.tool || "unknown";
  const isError = Boolean(payload.result && typeof payload.result === "object" && "Err" in payload.result);
  const entry = state.mcpByServer.get(server) || { calls: 0, errors: 0, tools: {} };
  entry.calls += 1;
  if (isError) entry.errors += 1;
  entry.tools[tool] = (entry.tools[tool] || 0) + 1;
  state.mcpByServer.set(server, entry);
  addToolCall(state, session, `mcp:${server}.${tool}`, payload, timestamp);
}

function recordSubagentSpawn(state, session, payload, timestamp, callId, fromFunctionCall = false) {
  // Dedup: a spawn may appear both as function_call and collab_agent_spawn_end.
  const key = callId ? `${session.id}:spawn:${callId}` : null;
  if (key && state.countedToolCallIds.has(key)) return;
  if (key) state.countedToolCallIds.add(key);
  state.counters.subagentSpawns += 1;
  state.subagentLifecycle.spawned += 1;
  if (!fromFunctionCall) addToolCall(state, session, "spawn_agent", payload, timestamp, callId ? `tool:${callId}` : undefined);
}

function mergePatch(state, session, patch) {
  const key = `${session.id}:${patch.callId || `event-${state.eventSequence}`}`;
  const previous = state.patchByCallId.get(key);
  if (previous) {
    if (patch.files.length) previous.files = patch.files;
    if (patch.status !== "unknown") previous.status = patch.status;
    return;
  }
  state.patchByCallId.set(key, { ...patch, sessionId: session.id });
}

function addPatchEvent(state, session, payload, timestamp) {
  const changes = payload.changes && typeof payload.changes === "object" ? payload.changes : {};
  let files = Object.keys(changes);
  if (!files.length && typeof payload.stdout === "string") {
    files = payload.stdout.match(/^[AMD]\s+(.+)$/gm)?.map(line => line.replace(/^[AMD]\s+/, "")) || [];
  }
  mergePatch(state, session, {
    callId: payload.call_id, files, timestamp, sequence: state.eventSequence,
    human: session.currentHuman,
    status: payload.success === false || payload.status === "failed" ? "failed" : payload.success === true || payload.status === "completed" ? "succeeded" : "unknown"
  });
}

function trackContextUsage(state, payload) {
  const info = payload.info;
  // last_token_usage.input_tokens approximates the live context size;
  // total_token_usage is cumulative and can exceed the window.
  if (!info?.last_token_usage?.input_tokens || !info.model_context_window) return;
  const pct = info.last_token_usage.input_tokens / info.model_context_window;
  if (pct > state.maxContextUsedPct) state.maxContextUsedPct = Math.min(1, pct);
}

function parsePlanArguments(argsText) {
  try {
    const parsed = JSON.parse(String(argsText || ""));
    const plan = Array.isArray(parsed.plan) ? parsed.plan : [];
    return {
      total: plan.length,
      completed: plan.filter((step) => step?.status === "completed").length
    };
  } catch {
    return null;
  }
}

function parseAgentTargets(argsText) {
  try {
    const parsed = JSON.parse(String(argsText || ""));
    if (Array.isArray(parsed.targets)) return parsed.targets.filter(Boolean);
    if (parsed.target) return [parsed.target];
    return [];
  } catch {
    return [];
  }
}

function addSignals(bucket, features) {
  bucket.messageCount += 1;
  for (const [key, value] of Object.entries(features)) {
    if (value && key in bucket.counts) bucket.counts[key] += 1;
  }
}

// ---------------------------------------------------------------------------
// Finalization
// ---------------------------------------------------------------------------

function finalizeShellCommands(state) {
  const sessionById = new Map(state.sessions.map(session => [session.id, session]));
  state.patchEvents = [...state.patchByCallId.values()].map(patch => ({ ...patch, success: patch.status === "succeeded" }));
  for (const patch of state.patchEvents) {
    if (!patch.success) continue;
    const session = sessionById.get(patch.sessionId);
    if (!session) continue;
    for (const file of patch.files) state.filesTouched.add(file);
    const edits = Math.max(1, patch.files.length);
    session.edits += edits;
    session.lastEditSequence = Math.max(session.lastEditSequence ?? 0, patch.sequence);
    if (patch.human) patch.human.after.edits += edits;
  }
  state.allShellCommands = [...state.shellByCallId.values(), ...state.shellCommands]
    .map(entry => {
      const inspection = inspectProofCommand(entry.command);
      return { ...entry, proof: inspection.proof, proofExitCode: inspection.reliableExit ? entry.exitCode : null };
    });
  state.unknownExitCodeCommands = state.allShellCommands.filter(shell => shell.exitCode === null).length;
  const lastFailedProof = new Map();
  for (const shell of [...state.allShellCommands].sort((a, b) => a.sequence - b.sequence)) {
    const session = sessionById.get(shell.sessionId);
    if (!session) continue;
    const skill = skillNameFromCommand(shell.command);
    if (skill) state.skillReads.set(skill, (state.skillReads.get(skill) || 0) + 1);
    if (shell.proof) {
      if (shell.proofExitCode === 0) session.proofPassed += 1;
      else if (typeof shell.proofExitCode === "number") session.proofFailed += 1;
      else session.proofUnknown += 1;
      if (shell.human) shell.human.after.proofRuns += 1;
      if (session.lastEditSequence !== null && shell.sequence > session.lastEditSequence) {
        session.proofAfterEdit = true;
        session.passedAfterEdit = shell.proofExitCode === 0;
      }
      if (typeof shell.proofExitCode === "number" && shell.proofExitCode !== 0) { lastFailedProof.set(session.id, shell.sequence); session.recoveredProofFailure = false; }
      if (shell.proofExitCode === 0 && lastFailedProof.has(session.id)) session.recoveredProofFailure = true;
    }
    if (typeof shell.exitCode === "number" && shell.exitCode !== 0) {
      session.failedCommands += 1;
      if (shell.human) shell.human.after.failedCommands += 1;
    }
  }
}

function finalizeSignals(state) {
  for (const bucket of Object.values(state.signals)) {
    for (const key of Object.keys(bucket.counts)) {
      bucket.ratios[key] = ratio(bucket.counts[key], bucket.messageCount);
    }
  }
  // Share of corrections that show substance (path / error log / code) —
  // corrections that show, not just tell.
  state.signals.correcting.substanceRatio = state.signals.correcting.messageCount
    ? round2(ratio(state.correctionSubstanceCount, state.signals.correcting.messageCount))
    : null;
}


function round2(value) { return Math.round(value * 100) / 100; }
