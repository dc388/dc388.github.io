# Auditoría del APK y del orden de los textos

Revisión del orden de las tres colecciones contra el texto que llevan dentro, y
de la aplicación pantalla por pantalla. Once fallos corregidos, dos puntos que
siguen abiertos, dos comprobaciones que pasan.

Para verlo en marcha sin instalar nada hay una vista previa de la app en el
navegador, con el texto y el léxico reales: **[Biblia Griega en el
teléfono](https://claude.ai/code/artifact/9e0ec959-3d21-4953-90b5-73f29c339dfe)**.

## Corregido

### 1. La Carta de Jeremías no se podía abrir

La fuente de Swete numera el libro entero como capítulo 0 (`52.0.0`, `52.0.1`…),
porque es una carta sin división en capítulos. La base guardaba esos 73
versículos en el capítulo 0, pero el selector ofrecía un capítulo 1 que no
existía: **el libro era inaccesible desde la interfaz**.

Ahora, cuando todos los versículos de un libro caen en el capítulo 0, se
renumeran al 1.

### 2. La Oda 14 y Sabiduría 20 quedaban fuera del selector

`chapter_count` se calculaba contando capítulos distintos, y la pantalla de
capítulos pintaba `1..chapter_count`. Eso solo funciona si la numeración es
contigua, y en la Septuaginta no lo es: a las Odas les falta la 4 y a Sabiduría
el 15. Con un hueco en medio, el último capítulo caía fuera de la cuenta.

La tabla `books` guarda ahora `chapter_list`, la lista real de capítulos, y la
navegación —rejilla y botones de anterior/siguiente— se mueve por esa lista.

### 3. Se ofrecían capítulos vacíos

El mismo fallo por el otro lado: Sabiduría 15 y Eclesiástico 52 se pintaban en
la rejilla y abrían un capítulo en blanco.

### 4. Cinco versículos salían vacíos

Éxodo 20:1, Números 17:1 y 19:1, 3 Reinos 14:1 y 16:1. En la transcripción, el
encabezado del capítulo en números romanos está numerado como si fuera el primer
versículo (`2.20.1 XX`). `tools/clean.py` quita los numerales romanos sueltos,
que es lo correcto, y el versículo quedaba en blanco. Ahora, si un versículo
queda sin texto tras la limpieza, no se inserta: el capítulo empieza donde
empieza el texto, como en la edición impresa.

### 5. Un ajuste describía algo que había dejado de ser cierto

«Modo interlineal — Disponible en el Nuevo Testamento», escrito antes de que
existiera el interlineal hebreo.

### 6. El selector de colección cortaba el nombre

Tres botones en 411 dp no dan para «Nuevo Testamento»: se veía «Nuevo Testa…».
Las etiquetas pasan a ser «AT hebreo», «Septuaginta» y «NT griego».

### 7. El resumen del constructor contaba de más

Anunciaba 60 656 versículos cuando la base tenía 60 651: sumaba lo leído de las
fuentes, no lo insertado. Ahora el resumen consulta la base.

### 8. La definición breve del interlineal estaba en inglés

Bajo cada palabra, el interlineal mostraba la glosa del léxico tal cual: `λόγος →
a word`, `θεός → a god or deity`. Y el artículo `ὁ`, la palabra más frecuente del
Nuevo Testamento, salía glosado «he», porque Abbott-Smith abre su artículo por el
uso demostrativo homérico. Cuatro veces seguidas en Juan 1:1.

`tools/glosario.py` traduce a mano los 1 196 lemas más frecuentes —632 griegos y
564 hebreos—, que cubren el 84,5 % de las palabras del Nuevo Testamento y el
74,9 % del Antiguo, y el 100 % de los capítulos que la aplicación enseña de
entrada. Van en su propia tabla, `glosario`, no mezclados con los léxicos: la
traducción es obra de este proyecto y las obras de referencia se citan aparte,
en su lengua.

Los criterios están en la cabecera del módulo, para que las entradas nuevas
sigan los mismos: se glosa el lema y no la forma concreta, los verbos en
infinitivo, y una sola acepción por lema —seis caracteres de media—, porque la
glosa se pinta en una columna estrecha bajo cada palabra y dos acepciones
separadas por coma parten el interlineal en más líneas. Entre dos posibles gana
la que distingue el lema de sus sinónimos, para que el interlineal no diga lo
mismo de dos palabras distintas: `ὁράω` es «ver» y `βλέπω` «mirar», `λόγος` es
«palabra» y `ῥῆμα` «dicho», `χρόνος` es «tiempo» y `καιρός` «momento». Donde el
griego no tiene equivalente —la partícula `ἄν`— se dice qué hace la partícula en
vez de forzar una traducción.

El resto de las palabras sigue mostrando la glosa inglesa, y el artículo
completo del léxico —que también está en inglés— sigue a un toque en la ficha:
esto sustituye la línea corta, no la obra de referencia.

### 9. La compilación de publicación no pasaba

El APK de depuración compilaba sin quejarse, pero `bundleRelease` fallaba en
`lintVitalRelease`, la comprobación que Android solo ejecuta al compilar para
publicar:

```
Error: biblia.db is not in an included path [FullBackupContent]
    <exclude domain="file" path="biblia.db" />
```

Las reglas de copia de seguridad incluían `datastore/` y además excluían
`biblia.db`. Pero en cuanto hay un `<include>`, Android respalda *únicamente* lo
incluido, así que excluir algo que no estaba incluido no significa nada, y lint
lo trata como error fatal. Quitados los tres `<exclude>`: los 63 MB de la base
siguen sin respaldarse —nunca lo estuvieron— y la app ya compila para Play.

Es justo el tipo de fallo que motivó montar el flujo de publicación antes de
tener la clave de firma: no aparece en la compilación de depuración, y se habría
descubierto el día de subir la app.

### 10. En la Septuaginta no se podía consultar ninguna palabra

Al tocar un versículo de la Septuaginta salía el texto y los botones de
marcador, nota y compartir, pero ninguna palabra que tocar. El motivo es real y
no tiene que ver con el código: **la edición de Swete es texto corrido**, sin
numeración Strong ni morfología. Los otros dos textos sí vienen analizados —el
Nuevo Testamento por Robinson, el hebreo por OSHB—, pero de la Septuaginta no
existe una digitalización etiquetada cuya licencia permita distribuirla con una
aplicación en Play: la de CATSS, que es la referencia, restringe el uso a fines
académicos.

Lo que sí se puede hacer, y se ha hecho: **el 82,3 % de las palabras de la
Septuaginta aparecen con la forma exacta en el Nuevo Testamento**, que sí está
analizado. La tabla `nt_forms` guarda, por cada una de las 17 174 formas del
Nuevo Testamento, hasta sus tres lecturas más frecuentes. Al tocar una palabra
griega de la Septuaginta, la aplicación enseña lo que esa misma forma significa
allí.

Y lo dice con todas las letras: «La Septuaginta no viene analizada. Esta forma
aparece así en el Nuevo Testamento». No es un análisis del texto de los Setenta
—una forma puede coincidir y venir de otra palabra, y el griego de la
Septuaginta no siempre usa el vocabulario con el sentido del Nuevo Testamento—,
y la ficha lo advierte al pie. Cuando la forma no aparece, se dice también, y
queda el botón de buscarla en el texto.

### 11. No se podía leer en español

La aplicación traía los tres textos en su lengua y ni una línea de traducción.
Servía para estudiar el original, pero quien abre Marcos 11 quiere saber qué
dice, y no había forma de averiguarlo dentro de la aplicación.

Ahora lleva la **Reina-Valera de 1909**, en dominio público, debajo de cada
versículo y en la ficha que sale al tocarlo. Cubre el 99,3 % de los versículos
del hebreo y del Nuevo Testamento —31 084 en total—, y se puede apagar en
Ajustes.

Se descartaron las revisiones modernas: la de 1960 y las posteriores son
propiedad de las Sociedades Bíblicas Unidas y no se pueden distribuir con una
aplicación. De las libres, la de 1909 es la que sigue el mismo tipo de texto que
lleva la aplicación —masorético en el Antiguo Testamento, mayoritario en el
Nuevo—, así que casa versículo a versículo casi siempre.

La Septuaginta se queda sin traducción, y es deliberado: la Reina-Valera traduce
del hebreo, y la numeración de la Septuaginta se aparta de la hebrea en los
Salmos, en Jeremías y en varios libros más, además de traer libros que la
Reina-Valera no tiene. Poner una traducción desalineada sería peor que no poner
ninguna.

### Y para que no vuelva a pasar

`verify()` —que corre en cada compilación y en CI, sobre la base ya construida—
comprueba ahora dos invariantes más:

- todo capítulo que el selector vaya a ofrecer tiene que existir;
- todo capítulo que exista tiene que poder alcanzarse desde el selector;
- ningún versículo puede quedarse sin texto;
- ninguna entrada del glosario puede apuntar a un número Strong que no aparezca
  en el texto, que es como se vería una errata de tecleo: la palabra seguiría
  mostrando la glosa inglesa y la traducción quedaría muerta en el diccionario.

## Abierto

### 91 versículos con restos de OCR

El 0,15 % de la Septuaginta conserva letras latinas o sílabas pegadas de la
transcripción de Swete, aguas arriba. Están documentados y el constructor los
cuenta y avisa en cada compilación. Corregirlos exigiría cotejar con el
facsímil.

### Los comentarios clásicos siguen sin fuente

Matthew Henry y Jamieson-Fausset-Brown eran el cuarto módulo de la propuesta. El
repositorio que iba a servirlos está vacío, y no se ha sustituido por ninguna
digitalización auditable. El módulo no existe; no se ha fingido que exista.

## Comprobado

- **Tres permisos, y ninguno toca el teléfono.** `INTERNET`,
  `ACCESS_NETWORK_STATE` y el identificador de publicidad, que son los que
  piden AdMob y Google Play. Sin almacenamiento, sin ubicación, sin contactos.
  Todo el contenido —texto, léxico, traducción— se lee en modo avión; la red
  solo trae el anuncio y pregunta por la suscripción. La ficha de Play sí tiene
  que declarar recogida de datos desde que hay anuncios: ver
  [ANUNCIOS_Y_SUSCRIPCION.md](ANUNCIOS_Y_SUSCRIPCION.md).
- **El interlineal reconstruye el texto.** Concatenar las palabras analizadas
  devuelve el versículo carácter por carácter en los 7 957 del Nuevo Testamento.
  Si no fuera así, alguna palabra estaría mostrando el análisis de la de al lado.

## Orden de las colecciones

Revisado libro por libro, no da problemas:

- **Antiguo Testamento hebreo (39 libros)**: orden del Tanaj —Torá, Profetas,
  Escritos—, que es el del Códice de Leningrado del que procede el texto.
- **Septuaginta (56 libros)**: orden de Swete, con los deuterocanónicos en su
  sitio y las dobles versiones (Daniel, Susana, Bel) separadas en LXX y
  Teodoción, como las imprime la edición.
- **Nuevo Testamento (27 libros)**: orden tradicional, el que espera un lector
  en español.

Las diferencias de numeración entre el hebreo y el griego —Joel con 4 capítulos
en hebreo y 3 en la Septuaginta, Malaquías con 3 y 4— son reales en las
ediciones, no errores de importación.
