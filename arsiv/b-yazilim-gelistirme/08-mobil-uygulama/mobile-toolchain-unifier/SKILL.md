---
name: mobile-toolchain-unifier
description: Audits, unifies, and optimizes mobile development environments and toolchains across a drive (Android, Flutter, iOS). Consolidates fragmented NDKs, SDK platforms, Gradle distributions, Flutter SDKs (FVM), and Java/JVM daemon versions to the latest stable releases, verifies project builds, reclaims tens of gigabytes of disk space, aggressively trims emulator bloatware using avdslim while preserving Play Store, and creates instant-boot Golden Snapshots. Use whenever the user asks to clean, unify, upgrade, or optimize Android SDKs, NDKs, Gradle wrappers, Java/JVM daemons, iOS simulator runtimes, or mobile emulator environments.
metadata:
  author: harish
  version: 1.0.0
---

# Mobile Toolchain Unifier

A comprehensive skill for auditing, unifying, and reclaiming disk space across multi-project mobile development workspaces (Flutter, Android native, and iOS).

## Overview

Over time, active mobile development machines accumulate duplicate SDKs, conflicting Gradle versions, multiple Java daemons, redundant NDKs, bloated system images, and gigabytes of orphaned simulator runtimes.

This skill provides an automated, non-destructive workflow to:
1. **Audit & Discover:** Find all mobile projects across the drive and inventory their toolchain versions.
2. **Unify & Pin:** Align all projects onto the latest stable common denominators (Gradle wrapper, AGP, Java LTS, NDK, SDK platforms, Flutter FVM).
3. **Verify Builds:** Test compilation across all projects to ensure zero breaking changes.
4. **Purge Obsolete Assets:** Remove older toolchain copies, Gradle caches, and legacy simulator runtimes, saving 20–80+ GB of disk space.
5. **Optimize Emulators:** Build ultra-lightweight Android emulators with `avdslim`, uninstall bloatware while keeping Google Play Services & Play Store, and bake `<1.5s` Golden Snapshots.

---

## Reference Guides

| Domain | Reference file |
| --- | --- |
| AGP, Gradle, Java, NDK & compileSdk Matrix | `references/android_toolchain_matrix.md` |
| Bloatware Removal, Play Store & `avdslim` Guide | `references/emulator_slimming_guide.md` |
| Apple Simulator Slimming & `simslim` Guide | `references/simslim_optimization_guide.md` |

---

## 6-Phase Workflow

### Phase 1: Audit & Discovery

Scan the drive for all active mobile projects and toolchains.

#### 1. Discover Projects
```bash
# Locate Gradle and Flutter configurations across Developer directories
find ~/Developer -maxdepth 5 \( -name "build.gradle" -o -name "build.gradle.kts" -o -name ".fvmrc" \) -not -path "*/build/*" -not -path "*/.gradle/*"
```

#### 2. Inventory Installed Toolchains
```bash
# Android SDK components
sdkmanager --list_installed

# Flutter FVM versions
ls -lh ~/fvm/versions/

# Java runtimes and daemon JVMs
java -version
/usr/libexec/java_home -V
cat ~/.gradle/gradle.properties

# iOS CoreSimulator runtimes and disk images
xcrun simctl runtime list
```

---

### Phase 2: Toolchain Unification

Consolidate all discovered projects onto unified versions:

#### 1. Android NDK
* Inspect pinned `ndkVersion` in every `build.gradle.kts` / `build.gradle`.
* Pin to the latest installed stable release (e.g. `30.0.16248370` / NDK r30).
* Ensure projects without explicit `ndkVersion` declare it to prevent Android Gradle Plugin from auto-downloading legacy fallbacks.

#### 2. Gradle Wrapper & Android Gradle Plugin (AGP)
* Upgrade `gradle/wrapper/gradle-wrapper.properties` in all projects to the latest stable release (e.g. `gradle-9.8.2-bin.zip`).
* Align AGP in `settings.gradle.kts` / root `build.gradle` (e.g. AGP `9.4.x` / `9.5.x`) to ensure compatibility with Gradle 9.6+.
* Align Kotlin Gradle Plugin (`org.jetbrains.kotlin.android`) to `2.4.x` to match AGP 9.

#### 3. Java / JVM Daemon Alignment
Prevent Gradle from spawning multiple incompatible daemon JVMs:
* In `~/.zshrc`, point `JAVA_HOME` and `PATH` to the latest LTS JDK (e.g. Java 21 LTS):
  ```bash
  export JAVA_HOME="$HOME/.gradle/jdks/eclipse_adoptium-21-aarch64-os_x.2/jdk-21.0.7+6/Contents/Home"
  export PATH="$JAVA_HOME/bin:$PATH"
  ```
* In `~/.gradle/gradle.properties`, set matching daemon JVM:
  ```properties
  org.gradle.java.home=/path/to/jdk-21/Contents/Home
  ```
* In each project's `build.gradle.kts`, standardize compatibility:
  ```kotlin
  compileOptions {
      sourceCompatibility = JavaVersion.VERSION_21
      targetCompatibility = JavaVersion.VERSION_21
  }
  tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile>().configureEach {
      compilerOptions {
          jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_21)
      }
  }
  ```

#### 4. Flutter SDK (FVM)
* Update all `.fvmrc` files to point to the latest installed Flutter release (e.g. `3.47.8`).
* Update `pubspec.yaml` environment constraints:
  ```yaml
  environment:
    sdk: 3.13.7
    flutter: 3.47.8
  ```
* Update `local.properties` in Flutter Android modules:
  ```properties
  flutter.sdk=/Users/<user>/fvm/versions/3.47.8
  ```

---

### Phase 3: Build Verification

Never delete or finalize before verifying that all projects build cleanly:

```bash
# 1. Flutter dependencies
cd <project> && fvm flutter pub get

# 2. Native Android compilation
cd <project>/android && ./gradlew assembleDebug

# 3. Verify Daemon JVM reuse
./gradlew --status
```
*Look for: `Launcher JVM: 21.x` and `Daemon JVM: 21.x` matching across every run.*

---

### Phase 4: Disk Reclamation & Pruning

Once builds are verified, safely eliminate redundant older assets:

```bash
# 1. Remove older NDK directories
rm -rf ~/Library/Android/sdk/ndk/<older-version>

# 2. Remove older SDK platforms and system images
rm -rf ~/Library/Android/sdk/platforms/android-{34,35,36}
rm -rf ~/Library/Android/sdk/system-images/android-{34,35,36}

# 3. Clean older Gradle wrapper distributions (frees 1-3 GB)
rm -rf ~/.gradle/wrapper/dists/gradle-{8.*,9.0.*,9.3.*,9.6.*}

# 4. Clean obsolete Gradle version caches (frees 10-25+ GB)
rm -rf ~/.gradle/caches/{9.0.0,9.3.1,9.6.0}

# 5. Remove older Flutter FVM SDKs (frees ~2.2 GB per version)
rm -rf ~/fvm/versions/<older-version>

# 6. Clean unneeded simulator runtimes (frees 20-60+ GB)
xcrun simctl runtime delete <runtime-uuid>
xcrun simctl delete unavailable
```

---

### Phase 5: Android Emulator Optimization (`avdslim`)

Create a lightning-fast, ultra-low-RAM single emulator instance:

1. **Delete All Existing AVDs:**
   ```bash
   avdmanager delete avd -n <old_avd>
   ```

2. **Select Google APIs Image (4 KB page size):**
   * Prefer `system-images;android-<latest>;google_apis;arm64-v8a`.
   * *Avoid Google Play production images* (blocks `adb root` and runs heavy background security scanners).
   * *Avoid 16 KB page size images* (forces QEMU to allocate $\ge$ 4096 MB RAM).

3. **Create Pre-Tuned AVD:**
   ```bash
   avdslim create Slim_Pixel --api=<latest> --ram=1536
   ```

4. **Uninstall Bloatware While Preserving Play Store:**
   * Boot the emulator headlessly with low-memory host flags:
     ```bash
     emulator -avd Slim_Pixel -memory 1536 -gpu host -no-audio -camera-back none -camera-front none -no-boot-anim -lowram -no-window
     ```
   * Elevate ADB daemon to root:
     ```bash
     adb root
     ```
   * Enable Google Play Store (`com.android.vending`):
     ```bash
     adb shell pm enable com.android.vending
     ```
   * Completely uninstall all bloatware for user 0 (see list in `references/emulator_slimming_guide.md`):
     ```bash
     adb shell "for pkg in \$(pm list packages -d | sed 's/package://'); do if [ \"\$pkg\" != 'com.android.vending' ]; then pm uninstall --user 0 \"\$pkg\"; fi; done"
     ```

5. **Capture Golden Snapshot & Install Shim:**
   ```bash
   # Snapshot live state (<1.5s restore)
   avdslim snap

   # Gracefully shut down
   avdslim stop

   # Install Android Studio wrapper shim
   avdslim install-shim
   ```

---

### Phase 6: iOS & Apple Simulator Optimization (`simslim`)

Prune runtimes and slim remaining simulators to reduce disk and idle RAM consumption:

1. **Prune Outdated Runtimes:**
   ```bash
   # List installed runtime disk images
   xcrun simctl runtime list

   # Delete outdated runtimes (frees 10-60+ GB)
   xcrun simctl runtime delete <UUID>
   ```

2. **Consolidate Device Fleet:**
   * Prune devices down to 2 primary target devices (e.g. 1 modern iPhone and 1 iPad Pro) and delete all other device UUIDs:
   ```bash
   xcrun simctl delete <UUID>
   xcrun simctl delete unavailable
   ```

3. **Slim Simulators with `simslim`:**
   * Configure persistent launchd disable overrides for 168 non-essential background daemons:
   ```bash
   simslim on <UDID> --preserve-boot-state
   ```

4. **Reclaim Disk Space (`disk-clean`):**
   * Purge accumulated caches, diagnostic logs, and temporary files:
   ```bash
   simslim disk-clean <UDID> --categories caches,logs,temporary,linguistic-data --confirm
   ```
   *Drops individual simulator storage down to ~56 MB.*

5. **Verify and Monitor:**
   ```bash
   # Measure allocated disk size
   simslim size <UDID>

   # Live fleet memory and CPU monitor
   simslim top
   ```
