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

# Se lanza con «monkey» y no con «am start» para no depender del nombre de la
# actividad: resuelve sola la del lanzador, que es por donde entra el usuario
# al tocar el icono.
#
# La base de datos se copia del APK al almacenamiento interno la primera vez, y
# son unos 25 MB: hay que darle tiempo antes de preguntar si sigue viva.
abrir() {
    # Los dos registros, no solo el general: «logcat -c» a secas no vacía el
    # de caídas, y una caída vieja daría por rota una compilación sana.
    adb logcat -c
    adb logcat -b crash -c 2>/dev/null || true
    adb shell monkey -p "$PAQUETE" -c android.intent.category.LAUNCHER 1
    sleep "$ESPERA"
}

# «adb shell» devuelve retorno de carro, y un «\r» suelto no es cadena vacía:
# sin limpiarlo, una aplicación muerta pasaría por viva y esto no serviría.
sigue_viva() {
    [ -n "$(adb shell pidof "$PAQUETE" 2>/dev/null | tr -d '\r\n ' || true)" ]
}

se_cayo() {
    [ -n "$(adb logcat -d -b crash 2>/dev/null | tr -d '\r' | head -5)" ]
}

# Android mata la aplicación, sin que se caiga, cuando muere un proceso del
# que depende. En un emulador recién arrancado eso pasa: Play Services se
# reinicia solo mientras instala sus módulos y se lleva por delante a quien
# esté usando alguno de sus proveedores —el de fuentes, en este caso—.
#
#   Killing com.dc388.bibliagriega (adj 0): depends on provider
#   com.google.android.gms/.fonts.provider.FontsProvider
#   in dying proc com.google.android.gms.persistent
#
# Eso no es un fallo de la aplicación y no debe contarse como tal: el registro
# de caídas está vacío. Pero tampoco se deja pasar en silencio, porque si la
# comprobación da falsos fallos se acaba ignorando, y es lo único que separa
# una compilación rota de una reseña de una estrella. Se vuelve a abrir una
# vez; si a la segunda tampoco aguanta, se falla.
la_mato_play_services() {
    adb logcat -d 2>/dev/null \
        | grep -q "Killing .*$PAQUETE.*dying proc com.google.android.gms"
}

rendirse() {
    echo "::error::La aplicación de publicación no se mantiene abierta. Esto es lo que vería el usuario al tocar el icono."
    echo "----- registro de fallos -----"
    adb logcat -d -b crash | tail -150
    echo "----- del registro general -----"
    adb logcat -d | grep -iE "bibliagriega|AndroidRuntime|ads|sqlite" | tail -80
    exit 1
}

abrir

if ! sigue_viva; then
    if se_cayo; then
        rendirse
    elif la_mato_play_services; then
        echo "Aviso: Android la cerró porque Play Services se estaba reiniciando," \
             "no porque se cayera. El registro de caídas está vacío. Se abre otra vez."
        abrir
        sigue_viva || rendirse
    else
        rendirse
    fi
fi

vivo=$(adb shell pidof "$PAQUETE" 2>/dev/null | tr -d '\r\n ' || true)
echo "La aplicación de publicación arranca y sigue en pie (pid $vivo)."
