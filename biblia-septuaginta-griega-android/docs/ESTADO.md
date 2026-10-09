# Dónde se quedó esto — 9 de octubre de 2026

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

Lo técnico está terminado. El flujo «Publicación — Biblia» produce en cada
cambio un **AAB firmado y con los identificadores reales de AdMob**, que es lo
que Play acepta; se comprueba en el resumen de la ejecución, que dice «Firmada»
y «Anuncios: identificadores reales». Lo que queda es todo de Play Console.

| | Qué falta | De quién depende |
|---|---|---|
| 1 | Borrar los idiomas sobrantes de la ficha de Play | tuyo |
| 2 | Formulario de **Seguridad de los datos** | respuestas en PUBLICAR_EN_PLAY.md |
| 3 | Perfil de pagos de AdMob | tuyo, y sin él no se cobra |
| 4 | Verificación de identidad de Play | tuya, tarda días |
| 5 | **Prueba cerrada: 12 probadores, 14 días seguidos** | tuya, si la cuenta es personal y posterior a nov. de 2023 |

De los cinco, **solo el 5 marca el calendario**. Los demás son de una tarde.

### La APK que se puede instalar sin pasar por Play

Mientras Play no la distribuya, la aplicación se instala desde una release de
GitHub. La etiqueta lleva el `versionCode` dentro, así que la de ahora es

**<https://github.com/dc388/dc388.github.io/releases/tag/biblia-apk-v7>**

(«Biblia Griega y Hebrea 1.2.1 — APK», 30 MB).

Quien se la baje tiene que conceder el permiso de **instalar aplicaciones de
origen desconocido** al navegador o al gestor de archivos. Android lo pide una
sola vez y es donde se atasca todo el que instala un APK a mano por primera
vez; las notas de la release lo explican paso a paso.

Para publicar una versión nueva **no hay que tocar ningún número**. El flujo
«APK para compartir» coge el APK de la última compilación de publicación que
haya salido bien, le lee la versión con `aapt2`, comprueba con `apksigner` que
está firmado y que el paquete no es el de depuración, y de ahí saca la etiqueta
y el título. Se lanza desde Actions, o tocando su propio archivo mientras viva
en una rama de trabajo.

La release vieja `biblia-apk-v3` («Biblia Griega y Hebrea 1.0.0», 18 de
septiembre, 9 descargas) se queda donde está: quien la instaló recibe la nueva
encima, con sus notas y marcadores intactos, porque la clave de firma es la
misma. Eso se comprobó mirando el registro de las dos compilaciones: el almacén
restaurado pesa 2710 bytes en las dos, o sea el mismo secreto. Si alguna vez se
cambiara la clave, Android rechazaría la actualización con «aplicación no
instalada» y habría que desinstalar antes, perdiendo las notas.

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
