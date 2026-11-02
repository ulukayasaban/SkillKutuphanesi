# Android Emulator Slimming & Play Store Preservation Guide

Guide for creating and maintaining lean, memory-efficient Android emulators using `avdslim` while keeping essential Google Play Services and Google Play Store intact.

## Why 4 KB Google APIs Images?

| System Image Type | Host RAM Usage | Guest Root (`adb root`) | Play Store |
| :--- | :--- | :--- | :--- |
| **Google APIs (4 KB)** | **~1.5 GB** | **Enabled** | **Pre-installed (`com.android.vending`)** |
| Google Play (4 KB) | ~2.5 - 4 GB | Disabled (production build) | Pre-installed |
| 16 KB Page Size (ps16k) | $\ge$ 4 GB (enforced by QEMU) | Enabled | Varies |

Always choose:
```bash
sdkmanager "system-images;android-<latest>;google_apis;arm64-v8a"
```

---

## Bloatware Uninstall vs Disable

### The Difference
* **`pm disable-user --user 0 <pkg>`**: Freezes the app. Package files and local state remain cached.
* **`pm uninstall --user 0 <pkg>`**: Completely deletes the app from the user profile, freeing guest RAM and preventing background wakeups entirely. Requires `adb root` on system apps.

---

## 54 Safe-to-Uninstall Bloatware Packages

These packages can be safely uninstalled from user 0 without breaking Firebase Auth, FCM, Maps, or the Google Play Store:

```text
com.google.android.telephony.satellite
com.google.android.gm
com.android.carrierdefaultapp
com.android.traceur
com.google.android.as.oss
com.google.android.apps.messaging
com.google.android.apps.youtube.music
com.android.stk
com.android.nfc
com.google.android.deskclock
com.google.android.apps.accessibility.voiceaccess
com.android.bips
com.google.android.partnersetup
com.android.cellbroadcastreceiver
com.google.android.tts
com.google.android.googlequicksearchbox
com.google.android.projection.gearhead
com.android.cameraextensions
com.google.android.nfc
com.google.android.apps.bard
com.android.dreams.basic
com.google.android.configupdater
com.google.android.calendar
com.google.android.feedback
com.google.android.contacts
com.google.android.settings.intelligence
com.android.chrome
com.android.bluetoothmidiservice
com.google.android.apps.maps
com.google.android.printservice.recommendation
com.google.android.dialer
com.google.android.gms.supervision
com.google.android.as
com.google.mainline.adservices
com.google.android.apps.photos
com.google.android.apps.wellbeing
com.google.android.markup
com.android.emulator.multidisplay
com.google.android.marvin.talkback
com.google.android.adservices.api
com.google.android.ondevicepersonalization.services
com.google.android.healthconnect.controller
com.google.android.apps.wallpaper
com.google.android.apps.docs
com.google.android.federatedcompute
com.android.printspooler
com.google.android.apps.safetyhub
com.android.DeviceAsWebcam
com.google.android.cellbroadcastservice
com.android.imsserviceentitlement
com.google.android.apps.restore
com.android.wallpaper.livepicker
com.android.camera2
com.google.android.youtube
com.google.android.apps.pulse
com.android.emergency
```

---

## Automated Root Uninstall Loop

Run this via ADB once the emulator is booted:

```bash
# 1. Switch to root
adb root

# 2. Wait for reconnect
adb wait-for-device

# 3. Ensure Play Store is enabled
adb shell pm enable com.android.vending

# 4. Uninstall all disabled bloatware except Play Store
adb shell "for pkg in \$(pm list packages -d | sed 's/package://'); do \
  if [ \"\$pkg\" != 'com.android.vending' ]; then \
    echo -n \"Uninstalling \$pkg: \"; \
    pm uninstall --user 0 \"\$pkg\"; \
  fi; \
done"
```

---

## Golden Snapshot Workflow

```bash
# Capture pristine state into Golden Snapshot
avdslim snap

# Gracefully stop
avdslim stop

# Launch in under 1.5s anytime
avdslim start <avd_name>
```
