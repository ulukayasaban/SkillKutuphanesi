#!/usr/bin/env bash
set -euo pipefail

echo "Codex Phone Lab doctor"
echo

need() {
  local cmd="$1"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[ok] $cmd: $(command -v "$cmd")"
  else
    echo "[missing] $cmd"
    return 1
  fi
}

missing=0
need node || missing=1
need npm || missing=1
need npx || missing=1

echo
if command -v node >/dev/null 2>&1; then
  echo "node version: $(node -v)"
fi
if command -v npm >/dev/null 2>&1; then
  echo "npm version: $(npm -v)"
fi

echo
if [ -f package.json ]; then
  echo "[ok] package.json found"
  if node -e "const p=require('./package.json'); const deps={...p.dependencies,...p.devDependencies}; process.exit(deps.expo?0:1)" 2>/dev/null; then
    echo "[ok] expo dependency found"
  else
    echo "[warn] package.json exists but expo dependency was not found"
  fi
else
  echo "[info] package.json not found; this directory can be used for a new Expo app"
fi

echo
echo "Phone requirements:"
echo "- Install Expo Go on iPhone or Android."
echo "- For LAN mode, keep phone and computer on the same Wi-Fi."
echo "- If LAN fails, run start-phone-preview.sh tunnel."

exit "$missing"
