# Apple CoreSimulator Slimming & Optimization Guide (`simslim`)

Guide for slimming and cleaning iOS, tvOS, watchOS, and visionOS simulators using `simslim` to dramatically lower RAM footprint and disk storage.

---

## What is `simslim`?

Apple simulators run dozens of non-essential macOS-hosted background daemons (Widgets, Siri, Apple Intelligence, iCloud sync, Photos analysis, Telemetry) that consume significant memory (1–2 GB RAM per booted simulator) and write continuous logs and caches to disk.

`simslim` configures persistent launchd disable overrides on simulators to stop these services while keeping critical development daemons (test runners, share sheets, XCUITest / GameKit) running.

---

## 168 Daemons Across 15 Categories

| Category | Daemons | Idle RAM Saved | Development Impact When Disabled |
| :--- | :--- | :--- | :--- |
| **`widgets`** | 4 | ~675 MB | Home/Lock screen widgets & Live Activities paused |
| **`siri`** | 28 | ~265 MB | Siri & Apple Intelligence disabled *(dictation `assistantd` kept on)* |
| **`other`** | 14 | ~195 MB | Wallet, merchant, asset background services |
| **`health`** | 14 | ~135 MB | HealthKit, HomeKit, Fitness integrations |
| **`telemetry`** | 11 | ~105 MB | Diagnostics, crash reporting, ads |
| **`icloud`** | 21 | ~100 MB | iCloud sync, Keychain backup |
| **`apps`** | 11 | ~90 MB | News, Weather, Maps background sync *(GameKit `gamed` kept on for XCUITest)* |
| **`store`** | 14 | ~80 MB | Remote push, StoreKit / App Store background loops |
| **`pim`** | 8 | ~80 MB | Contacts, Reminders, Calendar sync |
| **`connectivity`**| 11 | ~65 MB | AirDrop, Continuity, CarPlay *(share sheet `sharingd` kept on)* |
| **`family`** | 8 | ~65 MB | Screen Time & Family Sharing |
| **`photos`** | 8 | ~60 MB | Photos analysis and cloud libraries |
| **`messaging`** | 7 | ~60 MB | iMessage / FaceTime background services |
| **`search`** | 5 | ~50 MB | Core Spotlight indexing |
| **`web`** | 10 | ~50 MB | Safari history sync & background web daemons |

> [!NOTE]
> Core workflow daemons (like `com.apple.sharingd` for share sheets and `com.apple.gamed` for XCUITest launches) are protected and are **never** disabled.

---

## Optimizing a Simulator with `simslim`

### 1. Persistent Disables & Reboot
```bash
# Slim an existing simulator and keep its shutdown state
simslim on <UDID> --preserve-boot-state
```

### 2. Disk Space Cleanup (`disk-clean`)
Clean out accumulated caches, diagnostic logs, temporary files, and downloaded language models:

```bash
# Clean all safe categories
simslim disk-clean <UDID> --categories caches,logs,temporary,linguistic-data --confirm
```
*Reduces individual simulator disk footprint down to ~56 MB.*

### 3. Verification & Live Monitoring
```bash
# Measure allocated disk footprint
simslim size <UDID>

# Verify disable overrides match profile exactly
simslim verify <UDID>

# Live fleet RAM, CPU, and process monitor
simslim top
```

### 4. Automated Watch Mode (for CI & Parallel Testing)
Automatically slims every newly booted or cloned simulator as tests spawn:
```bash
simslim watch
```
