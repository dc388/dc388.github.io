#!/usr/bin/env bash
# Comprobación de sintaxis de las fuentes Kotlin, sin SDK de Android.
#
# Para qué sirve: en entornos donde no se puede compilar de verdad —sin el SDK
# de Android, o sin acceso a dl.google.com para bajar AGP y Compose— esto al
# menos pasa el parser de Kotlin sobre el código y señala los errores de
# estructura: paréntesis sin cerrar, comas de más, plantillas de cadena mal
# formadas. Es lo que se escapa al revisar a ojo tras editar con sed.
#
# Qué NO comprueba: nada que dependa de resolver símbolos. Sin androidx en el
# classpath, todos los imports fallan y el compilador emite cientos de
# «unresolved reference» que aquí se descartan. La compilación de verdad la hace
# GitHub Actions.
#
#   ./tools/check_kotlin.sh
#
# Descarga el compilador de Maven Central la primera vez (unos 57 MB) y lo
# guarda en build/kotlinc/.

set -euo pipefail

KOTLIN_VERSION="2.1.21"
COROUTINES_VERSION="1.8.1"
TROVE_VERSION="1.0.20200330"

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

fetch "org/jetbrains/kotlin/kotlin-compiler/$KOTLIN_VERSION/kotlin-compiler-$KOTLIN_VERSION.jar" \
    "kotlin-compiler.jar"
fetch "org/jetbrains/kotlin/kotlin-stdlib/$KOTLIN_VERSION/kotlin-stdlib-$KOTLIN_VERSION.jar" \
    "kotlin-stdlib.jar"
# El propio compilador necesita estas dos en su classpath.
fetch "org/jetbrains/kotlinx/kotlinx-coroutines-core-jvm/$COROUTINES_VERSION/kotlinx-coroutines-core-jvm-$COROUTINES_VERSION.jar" \
    "kotlinx-coroutines.jar"
fetch "org/jetbrains/intellij/deps/trove4j/$TROVE_VERSION/trove4j-$TROVE_VERSION.jar" \
    "trove4j.jar"

sources=$(find "$root/app/src/main/java" -name '*.kt')
count=$(echo "$sources" | wc -l)
output="$cache/salida.txt"

# JAVA_TOOL_OPTIONS trae ajustes de proxy que el compilador no necesita y que
# ensucian su salida.
env -u JAVA_TOOL_OPTIONS java \
    -cp "$cache/kotlin-compiler.jar:$cache/kotlinx-coroutines.jar:$cache/trove4j.jar" \
    org.jetbrains.kotlin.cli.jvm.K2JVMCompiler \
    -no-stdlib -cp "$cache/kotlin-stdlib.jar" -nowarn \
    -d "$cache/out" $sources > "$output" 2>&1 || true

errors=$(grep -c "syntax error:" "$output" || true)
echo "Archivos analizados: $count"

if [ "$errors" -gt 0 ]; then
    echo "Errores de sintaxis: $errors"
    grep "syntax error:" "$output"
    exit 1
fi

echo "Errores de sintaxis: 0"
