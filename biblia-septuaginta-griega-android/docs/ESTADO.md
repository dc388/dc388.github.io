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
| 3 | Capturas de pantalla | **hecho** — `docs/store/capturas/` |
| 4 | Borrar los idiomas sobrantes de la ficha de Play | tuyo |
| 5 | Formulario de **Seguridad de los datos** | respuestas en PUBLICAR_EN_PLAY.md |
| 6 | Perfil de pagos de AdMob | tuyo, y sin él no sirven anuncios |

Sin los secretos de AdMob, `assembleRelease` **falla a propósito**: una versión
firmada con los identificadores de prueba se vería idéntica y no ingresaría
nada.

## Las capturas — hechas

Seis por tamaño, en `docs/store/capturas/{telefono,tablet7,tablet10}/`, todas
en 9:16 exacto: biblioteca, Juan 1 con la Reina-Valera, el interlineal, Génesis
en hebreo, la búsqueda y los ajustes. Las toma el flujo «Capturas — Biblia» con
`screencap` sobre la aplicación instalada en un emulador.

Costó once intentos, y lo que más costó fue no poder ver nada: los artefactos
de Actions están en un almacenamiento que la sesión no alcanza, y la cola del
registro se corta antes de llegar al error. Hasta que el informe de fallos no
se subió a la propia rama, cada arreglo era una suposición. Las lecciones, por
si hay que volver a tocarlo:

- El informe y las imágenes se dejan en la rama, no solo como artefacto.
- Las comprobaciones copiadas de `FlujoDeLecturaTest` asumen una pantalla más
  alta que la 9:16 que exige Play: lo que allí se ve, aquí no se compone.
- Antes de dar por hecho que un botón existe en una pantalla, hay que mirar el
  código de `ui/screens/`. El simulador HTML no coincide con la aplicación.

**Mirar la aplicación por primera vez sacó tres defectos que nadie había
notado**, y ese fue el verdadero resultado del ejercicio:

- Los filtros de la búsqueda no cabían en 411 dp y «NT griego» se partía en
  vertical, una letra por línea. La fila se desplaza ahora en horizontal.
- La barra inferior salía lavanda sobre pergamino: el tema no definía los tonos
  `surfaceContainer` y Material caía a su paleta de fábrica.
- La captura de la búsqueda salía con el teclado tapando media pantalla.

## Datos que conviene tener a mano

- Idioma predeterminado de la ficha: **es-419**, no se puede cambiar.
- `applicationId`: `com.dc388.bibliagriega` (el de depuración lleva `.debug`).
- Alias de la clave de firma: `biblia-griega`.
- Producto de suscripción: `sin_anuncios_mensual`, y tampoco se puede cambiar.
- La base de datos no está en el repositorio: la regenera `tools/build_db.py`.
