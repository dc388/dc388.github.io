# Auditoría del APK y del orden de los textos

Revisión del orden de las tres colecciones contra el texto que llevan dentro, y
de la aplicación pantalla por pantalla. Siete fallos corregidos, cuatro puntos
que siguen abiertos, dos comprobaciones que pasan.

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

### Y para que no vuelva a pasar

`verify()` —que corre en cada compilación y en CI, sobre la base ya construida—
comprueba ahora dos invariantes más:

- todo capítulo que el selector vaya a ofrecer tiene que existir;
- todo capítulo que exista tiene que poder alcanzarse desde el selector;
- ningún versículo puede quedarse sin texto.

## Abierto

### La definición breve del interlineal está en inglés

Bajo cada palabra, el interlineal muestra la glosa del léxico: `λόγος → a word`,
`θεός → a god or deity`. Strong, Brown-Driver-Briggs y Abbott-Smith son obras
inglesas y se muestran tal cual. El análisis morfológico sí está traducido al
español, palabra por palabra, por este proyecto.

Es lo primero que va a notar un lector español, y no tiene arreglo barato:
traducir los tres léxicos es un trabajo editorial, no una conversión. Lo que sí
es abordable —y sería lo más rentable— es un glosario español cerrado para las
cuarenta o cincuenta palabras funcionales más frecuentes (artículo, `καί`, `ἐν`,
`εἰμί`, los pronombres), que cubren cerca de la mitad de las apariciones del
Nuevo Testamento. Es exactamente el método que ya se usa con la morfología
hebrea. Queda fuera de este cambio porque es una decisión editorial.

### El artículo ὁ aparece glosado «he»

Abbott-Smith abre el artículo por el uso demostrativo homérico, así que su
primera acepción no es «el». `tools/abbott_smith.py` toma la primera glosa sin
heurísticas, que es lo honesto con la fuente, pero repetido cuatro veces en Juan
1:1 despista. Se resolvería con el mismo glosario del punto anterior.

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

- **Ni un permiso en el manifiesto.** Sin `INTERNET`, sin almacenamiento, sin
  ubicación. La app funciona igual en modo avión y la ficha de Play no tiene que
  declarar recogida de datos.
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
