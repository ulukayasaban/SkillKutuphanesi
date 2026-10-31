#!/usr/bin/env bash
set -euo pipefail

mode="${1:-lan}"
case "$mode" in
  lan|tunnel|local) ;;
  *)
    echo "Usage: start-phone-preview.sh [lan|tunnel|local]"
    exit 2
    ;;
esac

if [ ! -f package.json ]; then
  echo "package.json not found. Run this inside an Expo project."
  exit 1
fi

if ! node -e "const p=require('./package.json'); const deps={...p.dependencies,...p.devDependencies}; process.exit(deps.expo?0:1)" 2>/dev/null; then
  echo "Expo dependency not found in package.json."
  exit 1
fi

if [ ! -d node_modules ]; then
  echo "node_modules not found; installing dependencies first."
  npm install
fi

echo "Starting Expo preview in $mode mode."
echo "Install Expo Go on your phone, then scan the QR code."
echo "Keep this terminal open while Codex edits the app."
echo

npx expo start "--$mode"
