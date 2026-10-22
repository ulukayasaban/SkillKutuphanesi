#!/usr/bin/env node
// list-codex-projects.mjs — group local Codex sessions into projects.
// Uses an incremental meta cache, folds automation-heavy child directories,
// and returns only the recent selection fields needed by the skill.
import { allSessionFiles, loadSessionMetasCached, loadThreadIndex, normalizePath } from "./lib.mjs";
import { buildProjectCatalog, resolveProject } from "./project-selection.mjs";

function parseArgs(argv) {
  const args = { cwd: process.cwd(), limit: 10 };
  for (let i = 0; i < argv.length; i += 1) {
    if (argv[i] === "--cwd") {
      args.cwd = argv[i + 1];
      i += 1;
    } else if (argv[i] === "--limit") {
      const limit = Number.parseInt(argv[i + 1], 10);
      if (!Number.isInteger(limit) || limit < 1 || limit > 50) {
        console.error("Usage: node list-codex-projects.mjs [--cwd <path>] [--limit 1..50]");
        process.exit(2);
      }
      args.limit = limit;
      i += 1;
    }
  }
  return args;
}

const args = parseArgs(process.argv.slice(2));
const currentCwd = normalizePath(args.cwd);
const threadIndex = loadThreadIndex();
const files = await allSessionFiles();
const metaMap = await loadSessionMetasCached(files);
const catalog = buildProjectCatalog(metaMap, threadIndex);
const projects = catalog.projects;
const cwdMatch = resolveProject(currentCwd, catalog);

console.log(JSON.stringify({
  sessionFileCount: files.length,
  count: projects.length,
  returnedCount: Math.min(projects.length, args.limit),
  flatCount: catalog.grouped.size,
  cwd: currentCwd,
  cwdMatch,
  projects: projects.slice(0, args.limit)
}, null, 2));
