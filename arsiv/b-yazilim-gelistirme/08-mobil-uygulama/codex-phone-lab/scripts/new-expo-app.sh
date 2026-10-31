#!/usr/bin/env bash
set -euo pipefail

app_name="${1:-}"
if [ -z "$app_name" ]; then
  echo "Usage: new-expo-app.sh <app-name>"
  exit 2
fi

if [ -e "$app_name" ]; then
  echo "Directory already exists: $app_name"
  exit 1
fi

template="${CODEX_PHONE_LAB_EXPO_TEMPLATE:-expo-template-default@sdk-54}"

echo "Creating Expo app: $app_name"
echo "Using Expo template: $template"
npx create-expo-app@latest "$app_name" --template "$template" --yes

echo
echo "Created $app_name"
echo "Next:"
echo "  cd $app_name"
echo "  ~/.codex/skills/codex-phone-lab/scripts/start-phone-preview.sh lan"
