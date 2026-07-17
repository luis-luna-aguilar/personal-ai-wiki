#!/usr/bin/env bash
# java-env.sh — shared Java resolver, sourced by scripts that run robot.jar or
# Apache Jena. Both require Java 11+, but the system-default `java` may be older
# (Java 8 on this machine), which fails with UnsupportedClassVersionError.
#
# Resolution order:
#   1. An already-set JAVA_HOME, if its java is >= 11 (explicit user override).
#   2. The newest installed JDK >= 11 via /usr/libexec/java_home (macOS).
#   3. Fail loudly with install instructions.
#
# Exports JAVA_HOME and JAVA (the java binary path; Jena's bin scripts honor it).

_java_major() {
  "$1" -version 2>&1 | awk -F'"' '/version/ { split($2, v, "."); print (v[1] == 1) ? v[2] : v[1]; exit }'
}

if [ -n "${JAVA_HOME:-}" ] && [ -x "$JAVA_HOME/bin/java" ] \
   && [ "$(_java_major "$JAVA_HOME/bin/java")" -ge 11 ] 2>/dev/null; then
  : # keep the caller's JAVA_HOME
elif [ -x /usr/libexec/java_home ] && _jh="$(/usr/libexec/java_home -v 11+ 2>/dev/null)"; then
  JAVA_HOME="$_jh"
else
  echo "✗ No Java 11+ found (robot.jar and Apache Jena require it)." >&2
  echo "  Install a JDK (e.g. 'brew install --cask temurin') or set JAVA_HOME to one." >&2
  exit 1
fi

export JAVA_HOME
export JAVA="$JAVA_HOME/bin/java"
