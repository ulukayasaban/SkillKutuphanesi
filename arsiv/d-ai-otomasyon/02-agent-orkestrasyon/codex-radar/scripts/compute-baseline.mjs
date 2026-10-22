#!/usr/bin/env node
// compute-baseline.mjs — build the user's self-baseline: the distribution of
// per-session collaboration metrics across ALL their Codex projects.
// Entirely local; used so reports can say "half the proof density of your
// median session" instead of quoting numbers with no anchor.
//
// Usage: node compute-baseline.mjs [--if-stale] [--refresh]
//   --if-stale  exit immediately if the cache is fresher than 7 days (default for SKILL flow)
//   --refresh   force a rebuild
import fs from "node:fs";
import path from "node:path";
import { allSessionFiles, RADAR_HOME, readSessionMeta, writeFilePrivate } from "./lib.mjs";
import { sessionKindFromMeta } from "./signals.mjs";
import { collectSessions, PARSER_VERSION } from "./session-parser.mjs";

const MAX_FILES = 400;
const STALE_MS = 7 * 24 * 60 * 60 * 1000;

const args = new Set(process.argv.slice(2));
const cachePath = path.join(RADAR_HOME, "cache", "self-baseline.json");

if (args.has("--if-stale") && !args.has("--refresh")) {
  try {
    const existing = JSON.parse(fs.readFileSync(cachePath, "utf8"));
    if (existing?.parserVersion === PARSER_VERSION && existing?.generatedAt && Date.now() - new Date(existing.generatedAt).getTime() < STALE_MS) {
      console.log(JSON.stringify({ cachePath, status: "fresh", generatedAt: existing.generatedAt }));
      process.exit(0);
    }
  } catch { /* no cache — build it */ }
}

const files = await allSessionFiles();
const sampled = files.length <= MAX_FILES
  ? files
  : Array.from({ length: MAX_FILES }, (_, index) => (
      files[Math.floor(index * (files.length - 1) / (MAX_FILES - 1))]
    ));

const byKind = { interactive: [], automation: [] };
for (const file of sampled) {
  const meta = await readSessionMeta(file);
  if (!meta?.cwd) continue;
  const kind = sessionKindFromMeta(meta);
  if (kind === "subagent") continue;
  const metrics = await sessionMetrics(file, meta);
  if (metrics.humanMessages > 0) byKind[kind].push(metrics);
}

function metricsFor(sessions) {
  if (!sessions.length) return null;
  return {
    sessions: sessions.length,
    humanMessages: distribution(sessions.map((s) => s.humanMessages)),
    averageMessageLength: distribution(sessions.map((s) => s.avgMsgLen)),
    editsPerHumanMsg: distribution(sessions.map((s) => s.edits / s.humanMessages)),
    toolsPerHumanMsg: distribution(sessions.map((s) => s.toolCalls / s.humanMessages)),
    proofRunsPerSession: distribution(sessions.map((s) => s.proofRuns)),
    explicitGoalRatio: distribution(sessions.map((s) => s.explicitGoal / s.humanMessages)),
    asksVerifyRatio: distribution(sessions.map((s) => s.asksVerify / s.humanMessages)),
    filePathRatio: distribution(sessions.map((s) => s.filePath / s.humanMessages))
  };
}

const result = {
  schemaVersion: "self-baseline-1",
  parserVersion: PARSER_VERSION,
  generatedAt: new Date().toISOString(),
  sessionsSampled: byKind.interactive.length + byKind.automation.length,
  interactive: metricsFor(byKind.interactive),
  automation: metricsFor(byKind.automation)
};

writeFilePrivate(cachePath, JSON.stringify(result, null, 2) + "\n");
console.log(JSON.stringify({ cachePath, status: "rebuilt", sessionsSampled: result.sessionsSampled }));

async function sessionMetrics(file, meta) {
  const state = await collectSessions([{ file, meta }], { privacyMode: "strict" });
  const session = state.sessions[0];
  const messages = state.humanMessages;
  const counts = state.signals.directing.counts;
  return {
    humanMessages: messages.length,
    avgMsgLen: messages.length ? Math.round(messages.reduce((sum, message) => sum + message.text.length, 0) / messages.length) : 0,
    edits: session?.edits || 0,
    toolCalls: state.toolCalls.length,
    proofRuns: (session?.proofPassed || 0) + (session?.proofFailed || 0) + (session?.proofUnknown || 0),
    explicitGoal: counts.explicitGoal, asksVerify: counts.asksVerify, filePath: counts.filePath
  };
}

function distribution(values) {
  const sorted = values.filter((value) => Number.isFinite(value)).sort((a, b) => a - b);
  if (!sorted.length) return null;
  const q = (p) => sorted[Math.min(sorted.length - 1, Math.floor(p * sorted.length))];
  return {
    p25: round2(q(0.25)),
    median: round2(q(0.5)),
    p75: round2(q(0.75))
  };
}

function round2(value) {
  return Math.round(value * 100) / 100;
}
