# Dónde se quedó esto — 14 de septiembre de 2026

Nota para retomar sin reconstruir nada de memoria.

## Hecho y comprobado

- **Aplicación completa**: 122 libros, 60 651 versículos, 439 705 palabras
  analizadas. 15 pruebas unitarias y 5 funcionales en verde.
- **Anuncios y suscripción**: AdMob con consentimiento europeo, banner al pie
  del lector y suscripción `sin_anuncios_mensual` que lo quita. Compila y pasa
  R8. Ver [ANUNCIOS_Y_SUSCRIPCION.md](ANUNCIOS_Y_SUSCRIPCION.md).
- **Clave de firma creada** y los cuatro secretos puestos en GitHub.
- **Política de privacidad publicada** y actualizada con lo de los anuncios:
  <https://dc388.github.io/biblia-privacidad.html>
- **32 traducciones procesadas** de `open-bibles`, en sus tres formatos, con
  índice y comprobación de cobertura. Ver [PLAN_IDIOMAS.md](PLAN_IDIOMAS.md).
- **Play Console**: clasificación de contenido, público objetivo, funciones
  financieras, salud e ID de publicidad, todo contestado.

## Lo que bloquea ahora mismo

| | Qué falta | De quién depende |
|---|---|---|
| 1 | **AdMob**: crear la app y el bloque de banner | tuyo, 5 minutos |
| 2 | Secretos `ADMOB_APP_ID` y `ADMOB_BANNER` en GitHub | depende de 1 |
| 3 | **Capturas de pantalla** | el flujo las genera, ver abajo |
| 4 | Borrar los idiomas sobrantes de la ficha de Play | tuyo |
| 5 | Formulario de **Seguridad de los datos** | respuestas en PUBLICAR_EN_PLAY.md |
| 6 | Perfil de pagos de AdMob | tuyo, y sin él no sirven anuncios |

Sin los secretos de AdMob, `assembleRelease` **falla a propósito**: una versión
firmada con los identificadores de prueba se vería idéntica y no ingresaría
nada.

## Las capturas

El flujo «Capturas — Biblia» las toma en un emulador, de la aplicación de
verdad, en los tres tamaños que pide Play (teléfono, tablet de 7 y de 10),
todos en 9:16 exacto.

Dos intentos fallidos y lo que se aprendió:

1. El comando de Gradle iba partido con `\`. La acción ejecuta cada línea con
   su propio `sh -c`, así que la barra llegó como nombre de tarea. Corregido.
2. El test no podía pulsar «Modo interlineal»: al añadir la tarjeta de la
   suscripción al principio de Ajustes, esa fila quedó fuera de la pantalla y
   Compose no deja pulsar lo que no se ve. Corregido con `performScrollTo()`.

## Datos que conviene tener a mano

- Idioma predeterminado de la ficha: **es-419**, no se puede cambiar.
- `applicationId`: `com.dc388.bibliagriega` (el de depuración lleva `.debug`).
- Alias de la clave de firma: `biblia-griega`.
- Producto de suscripción: `sin_anuncios_mensual`, y tampoco se puede cambiar.
- La base de datos no está en el repositorio: la regenera `tools/build_db.py`.
