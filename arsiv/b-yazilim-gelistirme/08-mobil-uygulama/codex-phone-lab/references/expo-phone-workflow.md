# Expo Phone Workflow

## Use Expo Go When

- The user wants a fast prototype on a real phone.
- The app can stay inside Expo's supported native runtime.
- The goal is visual/product iteration, not app-store distribution.

Command sequence:

```bash
npx create-expo-app@latest my-app --yes
cd my-app
npx expo start --lan
```

Use `--tunnel` if the phone cannot reach the computer on the local network.

## Use A Development Build When

- The app needs custom native modules.
- The app needs native config unavailable in Expo Go.
- The user wants a more production-like beta while still iterating locally.

This usually involves EAS and an Expo account.

## Use TestFlight When

- iPhone users need to install without Expo Go.
- The app is close to beta.
- The user has or will create an Apple Developer account.

TestFlight is distribution, not the fastest dev loop.

## Use App Store / Play Store When

- The user wants public release.
- Metadata, signing, review, privacy, screenshots, and store compliance matter.

For early Codex Phone Lab work, defer this until the app's product shape is clear.
