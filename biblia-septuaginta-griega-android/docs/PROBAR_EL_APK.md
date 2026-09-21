# Probar el APK antes de publicarlo

El APK de depuración se compila en GitHub Actions y se publica como artefacto de
la ejecución. No hace falta firmarlo ni tener Android Studio: basta con
descargarlo e instalarlo en un teléfono.

## 1. Descargar el APK

1. Entra en la pestaña **Actions** del repositorio.
2. Abre la última ejecución de **APK de prueba — Biblia** (o de **Build**, si el
   proyecto ya vive en su propio repositorio).
3. Al final de la página, en **Artifacts**, descarga `biblia-apk-debug`.
4. Es un `.zip`; dentro está `app-debug.apk`.

El artefacto caduca a los 30 días. Para volver a tenerlo, lanza el workflow otra
vez desde **Actions → Run workflow**.

## 2. Instalarlo en el teléfono

Pasa el `.apk` al teléfono (cable, Drive, Telegram, lo que uses) y ábrelo desde
el gestor de archivos.

Android pedirá permiso para instalar desde esa aplicación: **Ajustes →
Instalar apps desconocidas → [la app desde la que abres el archivo] → Permitir**.
Es lo normal en cualquier APK que no venga de Play.

Requisitos: **Android 8.0 o superior** y unos **250 MB libres**. El APK pesa
**43 MB** y, al primer arranque, descomprime la base de datos de 63 MB en su
almacenamiento privado: en total ronda los **110 MB** instalada.

La versión firmada que se sube a Play pesará menos, porque pasa por la reducción
de código de R8 y porque Play entrega un AAB del que cada teléfono descarga solo
lo que necesita.

El primer arranque tarda unos segundos justamente por esa copia. Los siguientes
son inmediatos.

## 3. Qué conviene probar

- **Las tres colecciones**: hebreo, Septuaginta y Nuevo Testamento. El selector
  está arriba de la lista de libros.
- **El hebreo se lee de derecha a izquierda.** Abre Génesis y comprueba que el
  texto se alinea a la derecha y que las vocales y los acentos se apilan bien
  sobre las consonantes. Es lo más delicado de toda la app: si algún teléfono no
  trae Noto Serif Hebrew, se verían cuadros en vez de letras.
- **El griego politónico**: en la Septuaginta, que los espíritus y los acentos
  circunflejos salgan bien.
- **Modo interlineal**: actívalo en Ajustes y abre Juan 1 o Génesis 1. Debajo de
  cada palabra tienen que verse la transliteración, la definición breve y el
  número Strong.
- **Ficha de palabra**: toca una palabra. Comprueba el análisis en español, la
  definición de Strong y el artículo del léxico —Brown-Driver-Briggs en hebreo,
  Abbott-Smith en griego—, y el botón de concordancia.
- **Búsqueda**: prueba `λογ` (debe traer λόγος, λόγῳ y λόγον, pero no φλογός) y
  una palabra hebrea sin vocales.
- **Notas y marcadores**: escribe una nota, cierra la app, vuelve a abrirla y
  comprueba que sigue ahí.
- **Tema oscuro** y **tamaño de letra** desde Ajustes.
- **Modo avión**: la app no declara permiso de internet, así que debe funcionar
  igual. Si algo fallara sin red, sería un error.

## 4. Diferencias con la versión de Play

El APK de depuración lleva el identificador `com.dc388.bibliagriega.debug`, así
que se puede instalar junto a la versión de Play sin pisarla. Tampoco pasa por
la reducción de código de R8, de modo que pesa algo más y arranca un poco más
lento que la versión final.

Para generar la versión firmada que se sube a Play, ver
[PUBLICAR_EN_PLAY.md](PUBLICAR_EN_PLAY.md).
