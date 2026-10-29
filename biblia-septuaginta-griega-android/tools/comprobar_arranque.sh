#!/usr/bin/env bash
# Comprueba que la aplicación que de verdad se publica abre y sigue en pie.
#
# Hasta que esto existió, nada arrancaba nunca la compilación de publicación:
# las pruebas del emulador ejecutan «connectedDebugAndroidTest», o sea la de
# depuración, sin R8, sin recorte de recursos y con los anuncios de prueba. Una
# versión que compila, se firma, se sube y se cierra sola al abrirla pasaba por
# todas las comprobaciones en verde y llegaba al teléfono de un usuario. Pasó.
#
# Va en un archivo y no dentro del YAML a propósito: la acción del emulador
# ejecuta cada línea del bloque «script» en un shell distinto, así que una
# variable definida en una línea está vacía en la siguiente. El primer intento
# de esta comprobación se cayó por eso sin llegar a instalar nada, y dio un
# falso positivo de fallo que parecía el de la aplicación.
set -euo pipefail

PAQUETE="com.dc388.bibliagriega"
ESPERA="${1:-30}"
ASENTAR="${2:-45}"

apk=$(find app/build/outputs/apk/release -name '*.apk' | head -1)
if [ -z "$apk" ]; then
    echo "::error::No se compiló ningún APK de publicación."
    exit 1
fi
echo "APK: $apk"

# El emulador recién arrancado sigue instalándose por dentro durante el primer
# minuto: Google Play Services baja e instala sus módulos, entre ellos los de
# anuncios. Y el SDK de anuncios carga el WebView del sistema nada más abrirse
# la aplicación. Abrirla justo en medio de eso la mató una vez con un SIGTRAP
# dentro de libmonochrome —el WebView—, sin que el código de la aplicación
# tuviera nada que ver; el mismo APK paso la comprobación antes y después.
#
# Esto no excusa ningún fallo ni relaja nada de lo de abajo: solo espera a que
# el teléfono esté como lo tiene un usuario, quieto, antes de mirar. Si vuelve
# a caer con la pila entera dentro de WebView, mirar primero si Play Services
# seguía instalando módulos en el registro.
echo "Esperando $ASENTAR s a que el emulador acabe de instalarse por dentro…"
sleep "$ASENTAR"

adb install -r "$apk"
adb logcat -c

# Se lanza con «monkey» y no con «am start» para no depender del nombre de la
# actividad: resuelve sola la del lanzador, que es por donde entra el usuario
# al tocar el icono.
adb shell monkey -p "$PAQUETE" -c android.intent.category.LAUNCHER 1

# La base de datos se copia del APK al almacenamiento interno la primera vez, y
# son unos 25 MB: hay que darle tiempo antes de preguntar si sigue viva.
sleep "$ESPERA"

# «adb shell» devuelve retorno de carro, y un «\r» suelto no es cadena vacía:
# sin limpiarlo, una aplicación muerta pasaría por viva y esto no serviría.
vivo=$(adb shell pidof "$PAQUETE" 2>/dev/null | tr -d '\r\n ' || true)
caidas=$(adb logcat -d -b crash | grep -c "FATAL EXCEPTION" | tr -d '\r\n ' || true)
caidas=${caidas:-0}

if [ -z "$vivo" ] || [ "$caidas" -gt 0 ]; then
    echo "::error::La aplicación de publicación no se mantiene abierta. Esto es lo que vería el usuario al tocar el icono."
    echo "----- registro de fallos -----"
    adb logcat -d -b crash | tail -150
    echo "----- del registro general -----"
    adb logcat -d | grep -iE "bibliagriega|AndroidRuntime|ads|sqlite" | tail -80
    exit 1
fi

echo "La aplicación de publicación arranca y sigue en pie (pid $vivo)."
