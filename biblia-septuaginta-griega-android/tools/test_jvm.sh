#!/usr/bin/env bash
# Ejecuta las pruebas unitarias sin Gradle ni SDK de Android.
#
# Para qué sirve: en entornos sin acceso a dl.google.com no se puede ejecutar
# ./gradlew test, pero Maven Central sí es alcanzable. Esto compila con kotlinc
# las clases que no dependen de Android —los modelos y la normalización del
# texto— junto con sus pruebas, y las corre con JUnit.
#
#   ./tools/test_jvm.sh
#
# Las pruebas que sí dependen de Android, y las funcionales sobre emulador, las
# ejecuta GitHub Actions con el flujo «Pruebas — Biblia».

set -euo pipefail

KOTLIN_VERSION="2.1.21"
JUNIT_VERSION="4.13.2"
HAMCREST_VERSION="1.3"

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cache="$root/build/kotlinc"
mkdir -p "$cache"

fetch() {
    local path="$1" file="$2"
    if [ ! -f "$cache/$file" ]; then
        echo "  descargando $file"
        curl -sSL -o "$cache/$file" "https://repo1.maven.org/maven2/$path"
    fi
}

fetch "org/jetbrains/kotlin/kotlin-compiler/$KOTLIN_VERSION/kotlin-compiler-$KOTLIN_VERSION.jar" kotlin-compiler.jar
fetch "org/jetbrains/kotlin/kotlin-stdlib/$KOTLIN_VERSION/kotlin-stdlib-$KOTLIN_VERSION.jar" kotlin-stdlib.jar
fetch "org/jetbrains/kotlinx/kotlinx-coroutines-core-jvm/1.8.1/kotlinx-coroutines-core-jvm-1.8.1.jar" kotlinx-coroutines.jar
fetch "org/jetbrains/intellij/deps/trove4j/1.0.20200330/trove4j-1.0.20200330.jar" trove4j.jar
fetch "org/jetbrains/annotations/23.0.0/annotations-23.0.0.jar" annotations.jar
fetch "junit/junit/$JUNIT_VERSION/junit-$JUNIT_VERSION.jar" junit.jar
fetch "org/hamcrest/hamcrest-core/$HAMCREST_VERSION/hamcrest-core-$HAMCREST_VERSION.jar" hamcrest.jar

out="$cache/pruebas"
rm -rf "$out"
mkdir -p "$out"

# Solo lo que no toca Android: los modelos y la normalización del texto.
sources=(
    "$root/app/src/main/java/com/dc388/bibliagriega/data/Models.kt"
    "$root/app/src/main/java/com/dc388/bibliagriega/data/Texto.kt"
    "$root/app/src/test/java/com/dc388/bibliagriega/NavegacionDeCapitulosTest.kt"
    "$root/app/src/test/java/com/dc388/bibliagriega/BusquedaTest.kt"
)

echo "Compilando ${#sources[@]} archivos…"
env -u JAVA_TOOL_OPTIONS java \
    -cp "$cache/kotlin-compiler.jar:$cache/kotlinx-coroutines.jar:$cache/trove4j.jar:$cache/annotations.jar" \
    org.jetbrains.kotlin.cli.jvm.K2JVMCompiler \
    -no-stdlib -nowarn \
    -cp "$cache/kotlin-stdlib.jar:$cache/junit.jar:$cache/hamcrest.jar" \
    -d "$out" "${sources[@]}"

echo
env -u JAVA_TOOL_OPTIONS java \
    -cp "$out:$cache/kotlin-stdlib.jar:$cache/junit.jar:$cache/hamcrest.jar" \
    org.junit.runner.JUnitCore \
    com.dc388.bibliagriega.NavegacionDeCapitulosTest \
    com.dc388.bibliagriega.BusquedaTest
