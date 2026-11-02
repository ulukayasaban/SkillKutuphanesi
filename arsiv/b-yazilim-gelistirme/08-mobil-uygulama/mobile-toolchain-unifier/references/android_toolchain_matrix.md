# Android Toolchain Compatibility Matrix

Quick reference for keeping Android Gradle Plugin (AGP), Gradle Wrapper, Java/JVM, NDK, and compileSdk in sync without runtime failures.

## Recommended Standard

| Component | Unified Target | Notes |
| :--- | :--- | :--- |
| **Android SDK Platform** | API 37 | Target & Compile SDK |
| **Android SDK Build-Tools** | `37.0.0` | Latest build-tools release |
| **Android CMake** | `4.1.2` | Installed in Android SDK `cmake/4.1.2` |
| **Android NDK** | `30.0.16248370` (NDK r30) | Explicitly pinned in `build.gradle.kts` |
| **Gradle Wrapper** | `9.8.2-bin` | Minimum for Java 21 / 27 support |
| **Android Gradle Plugin** | `9.4.1` / `9.5.0` | Eliminates legacy `InternalProblems` removals from Gradle 9.6+ |
| **Kotlin Gradle Plugin** | `2.4.21` | Matches AGP 9.x |
| **Java / JVM Toolchain** | Java 21 LTS | Both Launcher JVM and Daemon JVM |
| **Flutter SDK** | `3.47.8` / Dart `3.13.7` | FVM managed |

---

## AGP & Gradle Compatibility Reference

| AGP Version | Compatible Gradle Wrapper | Recommended Java |
| :--- | :--- | :--- |
| **9.4.x - 9.5.x** | **9.6.0 - 9.8.2+** | **Java 21 LTS** |
| 8.13.x | 8.11 - 9.5.0 *(incompatible with Gradle 9.6+)* | Java 17 - 21 |
| 8.9.x - 8.12.x | 8.9 - 9.0 | Java 17 - 21 |
| 8.4.x - 8.8.x | 8.6 - 8.10 | Java 17 |

> [!WARNING]
> AGP 8.13 and earlier rely on `org.gradle.api.problems.internal.InternalProblems`, a Gradle internal API removed in **Gradle 9.6.0**. Upgrading Gradle wrappers to 9.6+ requires bumping AGP to 9.4.1+.

---

## Kotlin 2.x JVM Target Configuration in `build.gradle.kts`

When standardizing on Java 21 with Kotlin 2.4+:

```kotlin
android {
    compileSdk = 37
    ndkVersion = "30.0.16248370"

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }

    kotlin {
        jvmToolchain(21)
    }
}

// Enforce JVM 21 across all Kotlin compilation tasks
tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile>().configureEach {
    compilerOptions {
        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_21)
    }
}
```

---

## Java Daemon Synchronization

To prevent Gradle from spawning multiple background daemons (e.g. one for each project or different JVM launcher):

1. **`~/.zshenv` & `~/.zshrc`**:
   ```bash
   export JAVA_HOME="$HOME/.gradle/jdks/eclipse_adoptium-21-aarch64-os_x.2/jdk-21.0.7+6/Contents/Home"
   export PATH="$JAVA_HOME/bin:$PATH"
   export CPPFLAGS="-I$JAVA_HOME/include"
   ```
   *(Placing in `~/.zshenv` ensures non-interactive subshells, IDE subprocesses, and CI scripts resolve Java properly).*

2. **`~/.gradle/gradle.properties`**:
   ```properties
   org.gradle.java.home=/path/to/jdk-21/Contents/Home
   org.gradle.jvmargs=-Xmx4G -XX:MaxMetaspaceSize=2G -XX:+HeapDumpOnOutOfMemoryError
   ```
