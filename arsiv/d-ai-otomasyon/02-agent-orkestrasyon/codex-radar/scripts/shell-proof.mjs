// Conservative shell inspection. Never execute a command to classify it.
// Only executable positions count; quoted text, filenames and here-doc bodies
// cannot turn a read/print command into verification.
export function inspectProofCommand(command, depth = 0) {
  if (depth > 4) return { proof: false, reliableExit: false };
  const parsed = shellSegments(String(command || ''));
  if (!parsed) return { proof: false, reliableExit: false };
  const matches = parsed.segments.map(tokens => inspectExecutable(tokens, depth));
  return {
    proof: matches.some(match => match.proof),
    reliableExit: parsed.segments.length === 1 && !parsed.complex && matches[0]?.reliableExit === true
  };
}

function shellSegments(text) {
  // Dynamic shell code and heredocs need a real shell parser. Leave them
  // unclassified rather than crediting commands embedded in source/data.
  if (/<<|\$\(|`/.test(text)) return null;
  const segments = [];
  let tokens = [], word = '', quote = null, active = false, complex = false;
  const flushWord = () => { if (active) tokens.push(word); word = ''; active = false; };
  const flushSegment = () => { flushWord(); if (tokens.length) segments.push(tokens); tokens = []; };
  for (let i = 0; i < text.length; i += 1) {
    const c = text[i];
    if (c === '\\' && quote !== "'") {
      if (text[i + 1] === '\n') { i += 1; continue; }
      if (i + 1 < text.length) { word += text[++i]; active = true; }
      continue;
    }
    if (quote) { if (c === quote) quote = null; else word += c; continue; }
    if (c === "'" || c === '"') { quote = c; active = true; continue; }
    if (c === '#' && !active) { while (i < text.length && text[i] !== '\n') i += 1; flushSegment(); continue; }
    if (';&|\n'.includes(c)) { if (c !== '\n') complex = true; flushSegment(); continue; }
    if (/\s/.test(c)) { flushWord(); continue; }
    if ('()<>'.includes(c)) complex = true;
    word += c; active = true;
  }
  if (quote) return null;
  flushSegment();
  return { segments, complex };
}

const yes = { proof: true, reliableExit: true };
const no = { proof: false, reliableExit: false };
const programName = value => String(value || '').replaceAll('\\', '/').split('/').pop().replace(/\.exe$/i, '').toLowerCase();
function inspectExecutable(input, depth) {
  const tokens = [...input];
  while (/^[A-Za-z_][A-Za-z0-9_]*=/.test(tokens[0] || '')) tokens.shift();
  const program = programName(tokens.shift());
  if (!program) return no;
  if (['env', 'command', 'builtin', 'nohup', 'time'].includes(program)) {
    while (tokens[0]?.startsWith('-')) tokens.shift();
    return inspectExecutable(tokens, depth);
  }
  if (['bash', 'sh', 'zsh', 'dash'].includes(program)) {
    const i = tokens.findIndex(token => /^-[a-z]*c[a-z]*$/.test(token));
    return i >= 0 ? inspectProofCommand(tokens[i + 1], depth + 1) : no;
  }
  if (tokens.some(token => ['--version', '--help', '-h'].includes(token))) return no;
  if (['npx', 'bunx'].includes(program)) {
    while (['--yes', '-y', '--no-install', '--'].includes(tokens[0])) tokens.shift();
    return inspectExecutable(tokens, depth);
  }
  if (['npm', 'pnpm', 'yarn', 'bun'].includes(program)) {
    while (['--prefix', '--cwd', '-C', '--dir', '--filter', '-w', '--workspace'].includes(tokens[0])) tokens.splice(0, 2);
    if (tokens[0] === 'exec' || tokens[0] === 'dlx') return inspectExecutable(tokens.slice(1), depth);
    if (tokens[0] === 'run') tokens.shift();
    return /^(test|build|check|lint|typecheck|e2e|coverage)(?::[\w-]+)?$/.test(tokens[0] || '') ? yes : no;
  }
  if (['uv', 'poetry', 'pipenv'].includes(program) && tokens[0] === 'run') return inspectExecutable(tokens.slice(1), depth);
  if (/^python(?:\d+(?:\.\d+)*)?$/.test(program)) {
    return tokens[0] === '-m' && ['pytest', 'unittest'].includes(tokens[1]) ? yes : no;
  }
  if (program === 'node') {
    if (tokens.some(token => ['-e', '--eval', '-p', '--print'].includes(token) || /^--(?:eval|print)=/.test(token))) return no;
    for (const token of tokens) {
      if (token === '--test' || token === '--check' || token === '-c') return yes;
      if (!token.startsWith('-') || token === '--') break;
    }
    return no;
  }
  if (program === 'bundle' && tokens[0] === 'exec') return inspectExecutable(tokens.slice(1), depth);
  const commands = {
    cargo: ['test', 'check', 'clippy', 'build'], go: ['test', 'vet', 'build'],
    swift: ['test', 'build'], make: ['test', 'check', 'lint', 'build'],
    mvn: ['test', 'verify', 'check', 'package'], mvnw: ['test', 'verify', 'check', 'package'],
    gradle: ['test', 'check', 'build', 'lint'], gradlew: ['test', 'check', 'build', 'lint'],
    dotnet: ['test', 'build'], rake: ['test', 'spec'], composer: ['test', 'check', 'lint', 'analyse', 'analyze'],
    mix: ['test', 'compile'], flutter: ['test', 'analyze', 'build'], dart: ['test', 'analyze'],
    deno: ['test', 'check', 'lint'], ninja: ['test', 'check'], playwright: ['test'], cypress: ['run'],
    biome: ['check', 'lint'], coverage: ['run']
  };
  if (commands[program]) return commands[program].includes(tokens[0]) ? yes : no;
  if (program === 'xcodebuild') return tokens.some(token => ['test', 'build', 'archive', 'analyze'].includes(token)) ? yes : no;
  if (program === 'cmake') return tokens[0] === '--build' ? yes : no;
  if (program === 'ruff') return tokens[0] === 'check' || tokens[0] === 'format' && tokens.includes('--check') ? yes : no;
  if (program === 'prettier') return tokens.includes('--check') ? yes : no;
  if (['pytest', 'mypy', 'flake8', 'tox', 'vitest', 'jest', 'mocha', 'ava', 'tsc', 'eslint', 'stylelint', 'rspec', 'phpunit', 'ctest'].includes(program)) return yes;
  return no;
}
