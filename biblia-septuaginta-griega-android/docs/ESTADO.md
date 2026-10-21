# Dónde se quedó esto — 21 de octubre de 2026

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

## Publicada

**La aplicación está en Google Play, en producción, desde el 17 de octubre de
2026.** La prueba cerrada de 12 probadores y 14 días, la verificación de
desarrollador y el acceso a producción están los tres concedidos.

La versión viva es la **1.2.4** (`versionCode` 10). La anterior, la 1.2.3,
llegó a producción y **se cerraba al tocar el icono**: está contado en
[TRASPASO.md](TRASPASO.md), y lo que lo permitió —que nada arrancara nunca la
compilación de publicación— quedó cerrado con `tools/comprobar_arranque.sh`.

### Lo que falta, y ya no bloquea publicar

| | Qué falta | De quién depende |
|---|---|---|
| 1 | **Perfil de pagos de AdMob y formulario fiscal de EE. UU.** | tuyo, y sin ellos no se cobra nada |
| 2 | Comprobar que Estados Unidos está en la lista de países | tuyo |
| 3 | Formulario de **Seguridad de los datos**, si sigue pendiente | respuestas en PUBLICAR_EN_PLAY.md |
| 4 | Borrar los idiomas sobrantes de la ficha | tuyo |

**El 1 es el único que importa de verdad ahora.** La aplicación está publicada
y sirviendo anuncios; sin perfil de pagos esos anuncios no ingresan nada, y sin
el formulario fiscal se retiene lo que generen los usuarios estadounidenses.

### La APK para quien no tiene Play

Ya no es la vía principal —la aplicación está en la tienda— pero sigue
haciendo falta donde Play no llega: **en Cuba no opera**, y el país ni siquiera
aparece en la lista que Play deja seleccionar. Allí la única forma es mandar el
archivo.

Ojo: una instalación a mano **no cuenta** como instalación en Play, no suma a
las estadísticas ni al posicionamiento. La etiqueta lleva el `versionCode` dentro, así que la de ahora es

**<https://github.com/dc388/dc388.github.io/releases/tag/biblia-apk-v10>**

(«Biblia Griega y Hebrea 1.2.4 — APK», 30 MB).

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
