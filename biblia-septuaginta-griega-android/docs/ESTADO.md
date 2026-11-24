# Dónde se quedó esto — 24 de noviembre de 2026

Nota para retomar sin reconstruir nada de memoria.

## Hecho y comprobado

- **Aplicación completa**: 122 libros, 60 651 versículos, 439 705 palabras
  analizadas. 30 pruebas unitarias y 9 funcionales en verde.
- **Versículo del día**: 30 versículos escritos a mano, cada uno con una
  palabra del original y lo que esa palabra dice. Se reparte por el día del
  año, con aviso opcional cada mañana y botón de compartir. Ver
  `data/VersiculoDelDia.kt`, que lleva escrita la regla que los gobierna.
- **Lectura en alto** con el sintetizador del teléfono: el español donde hay
  traducción, el original donde no la hay si el teléfono trae voz para esa
  lengua. Ver `data/Lector.kt`.
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

La versión publicada en Play es la **1.2.4** (`versionCode` 10). En esta rama
va la **1.3.0** (`versionCode` 11), con el versículo del día, el aviso de cada
mañana y la lectura en alto. El flujo «Publicación — Biblia» compila y firma
el AAB y el APK en cada empujón y comprueba en un emulador que la versión de
publicación arranca.

**Desde el 4 de noviembre el flujo también sabe subirla.** En *Run workflow* se
elige la pista —prueba interna, cerrada, abierta o producción— y el AAB sube
solo por la API de Google Play. Sube con él el `mapping` de R8, para que los
informes de caídas de Play Console lleguen legibles, y las notas de versión en
`distribucion/notas/whatsnew-es-419`.

**Falta una cosa, y es tuya:** crear la cuenta de servicio y guardar su `.json`
en el secreto `PLAY_SERVICE_ACCOUNT_JSON`. Son cinco pasos, están contados en
[PUBLICAR_EN_PLAY.md](PUBLICAR_EN_PLAY.md#4-subir-a-play-sin-entrar-en-play-console),
y se hacen una sola vez. Hasta que ese secreto exista, la subida se niega a
empezar y dice por qué. **A 24 de noviembre sigue sin estar**: la última subida
que se intentó es del 4 de noviembre, en seco, con la pista en «no».

El sitio donde se da el permiso es **Usuarios y permisos**, no «Acceso a la
API». Está corregido en PUBLICAR_EN_PLAY.md, pero conviene repetirlo porque es
donde se atasca todo el mundo: sin ese permiso la API contesta 403, y el 403 no
dice que falte un permiso.

Lo que sigue sin poder hacer una sesión de Claude Code es entrar en Play
Console: ni la cuenta de servicio, ni los formularios, ni abrir la pista de
prueba abierta con sus países.

La 1.2.3 llegó a producción y **se cerraba al tocar el icono**: está contado en
[TRASPASO.md](TRASPASO.md), y lo que lo permitió —que nada arrancara nunca la
compilación de publicación— quedó cerrado con `tools/comprobar_arranque.sh`.

### Lo que falta

| | Qué falta | De quién depende |
|---|---|---|
| 0 | **Declarar el estado de operador, antes de febrero de 2027** | tuyo, y es lo único con fecha de caducidad |
| 1 | **Perfil de pagos de AdMob y formulario fiscal de EE. UU.** | tuyo, y sin ellos no se cobra nada |
| 2 | Secreto `PLAY_SERVICE_ACCOUNT_JSON`, para que el flujo pueda subir | tuyo, cinco pasos, una vez |
| 3 | Abrir la pista de **prueba abierta** con sus países | tuyo, en Play Console |
| 4 | Comprobar que Estados Unidos está en la lista de países | tuyo |
| 5 | Formulario de **Seguridad de los datos**, si sigue pendiente | respuestas en PUBLICAR_EN_PLAY.md |
| 6 | Borrar los idiomas sobrantes de la ficha | tuyo |

**El 0 es nuevo y es el más grave, aunque no corra prisa hoy.** Play Console lo
avisa en su portada: si el estado de operador no se declara antes de febrero de
2027, *el perfil de desarrollador y todas las aplicaciones se retiran de Google
Play en todo el mundo*. Es un formulario corto, está en la portada de Play
Console bajo «Declara tu estado de operador → Empezar», y una vez hecho no se
vuelve a tocar. Quince meses parecen muchos hasta que se olvidan.

**El 1 es el que cuesta dinero cada día.** La aplicación está publicada y
sirviendo anuncios desde el 17 de octubre; sin perfil de pagos esos anuncios no
ingresan nada, y sin el formulario fiscal se retiene lo que generen los
usuarios estadounidenses. El 4 de noviembre la ficha marcaba 127 adquisiciones
y 66 dispositivos activos al mes, subiendo fuerte. Son impresiones servidas que
valen cero.

### La APK para quien no tiene Play

Ya no es la vía principal, y **a fecha de 29 de octubre de 2026 tampoco hace
falta**: el dueño confirma que a la gente de Cuba la aplicación les sale en
Play. Eso contradice lo que se dio por sentado aquí durante semanas —que Play
no opera en Cuba, que es lo que dice Google— así que lo que vale es lo que se
observa, no lo que se supone. Probablemente llegan con la cuenta de Google
puesta en otro país.

Queda por si acaso, para quien algún día no pueda instalar desde la tienda.

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

## Lo que se hizo el 4 de noviembre

**El léxico pasó del 81,4 % al 86,1 %** en español: 12 585 de 14 610 artículos
de Brown-Driver-Briggs y Abbott-Smith. Son cuatro tandas de palabras, y de paso
salieron **tres fugas que corrompían texto ya publicado**, las tres con la
misma raíz —la marca de la tabla puesta en la palabra equivocada—:

- El género se decidía por la última palabra del valor y no por la cabeza:
  «un salida del sol», «el ofrenda de grano», «un piedra de molino». 72 valores.
- La regla que quita la «a» del infinitivo inglés miraba esa misma pieza, así
  que «to accomplish» salía **«llevar cabo»** y «to seize» «a apoderarse de».
  22 valores.
- Al gentilicio le faltaba marca de adjetivo, así que salía en orden inglés:
  «el griego alfabeto», «un hebreo medida», «el romano emperador».

Y el **borde negro** que enmarcaba el selector de colecciones, el botón
«Escuchar» y el campo de búsqueda: el tema no definía `outline` y Material caía
a su paleta de fábrica, el mismo despiste que dejaba la barra inferior en
lavanda.

Todo ello está en la 1.3.0, que **sigue sin subir a Play**.

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

## Lo que se arregló el 28 de octubre, y que nadie había notado

**En 62 de los 150 salmos, el hebreo mostraba debajo la traducción del
versículo siguiente.** El Salmo 46:11 decía «Jehová de los ejércitos es con
nosotros» donde el hebreo dice «Estad quietos, y conoced que yo soy Dios». El
Códice de Leningrado numera el encabezamiento del salmo como versículo 1 y la
Reina-Valera no, así que a partir del título todo iba corrido un sitio.

No era un hueco —un hueco se ve—: era un texto equivocado que se lee tan
campante, en la aplicación y en la web, desde el primer día. Se arregló en
`tools/build_db.py` y la base ya **no se construye** si tres salmos de testigo
dejan de cuadrar.

La lección vale más que el arreglo: el código ya sabía que los títulos
descuadraban la cuenta —lo decía en un comentario— y lo trataba como una
explicación de por qué la cobertura no llegaba al 100 %. Nadie se preguntó qué
pasaba con los versículos que sí tenían traducción.

## Datos que conviene tener a mano

- Idioma predeterminado de la ficha: **es-419**, no se puede cambiar. Es el
  único idioma al que el flujo manda notas de versión: Play las quiere con el
  código exacto de la ficha, y mandar uno que la ficha no tenga tumba la subida
  entera.
- `applicationId`: `com.dc388.bibliagriega` (el de depuración lleva `.debug`).
- Alias de la clave de firma: `biblia-griega`.
- Producto de suscripción: `sin_anuncios_mensual`, y tampoco se puede cambiar.
- La base de datos no está en el repositorio: la regenera `tools/build_db.py`.
