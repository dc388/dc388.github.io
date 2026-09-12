# Atribuciones

Esta aplicación redistribuye textos preparados por terceros. Estas son las
atribuciones exigidas por sus licencias.

## Antiguo Testamento hebreo — Open Scriptures Hebrew Bible

> *Westminster Leningrad Codex*, en dominio público, etiquetado con números
> Strong y análisis morfológico por el Open Scriptures Hebrew Bible.

Fuente: [openscriptures/morphhb](https://github.com/openscriptures/morphhb).

Licencia: **Creative Commons Attribution 4.0 International** (CC BY 4.0), que
permite el uso comercial. Atribución exigida por la licencia: «Original work of
the Open Scriptures Hebrew Bible available at
https://github.com/openscriptures/morphhb».

Las descripciones morfológicas se traducen al español a partir de la clave
oficial `parsing/Oshm.xml` del propio proyecto; esa traducción
(`tools/hebrew.py`) es obra de este repositorio y se publica bajo la licencia
MIT del código.

## Septuaginta — edición de Swete

> *The Old Testament in Greek According to the Septuagint*, editado por
> Henry Barclay Swete (Cambridge University Press, 1887–1912).

Digitalización: **Open Greek and Latin / First1KGreek Project**
(https://github.com/OpenGreekAndLatin/First1KGreek), normalizada por
**nathans/lxx-swete** (https://github.com/nathans/lxx-swete).

Licencia: **Creative Commons Attribution-ShareAlike 4.0 International**
(https://creativecommons.org/licenses/by-sa/4.0/).

El archivo `app/src/main/assets/biblia.db` contiene una adaptación de ese texto
(reagrupado por versículos y con una columna auxiliar sin diacríticos) y se
distribuye bajo la misma licencia CC BY-SA 4.0. El script que lo genera está en
`tools/build_db.py`.

## Nuevo Testamento — Robinson–Pierpont

> *The New Testament in the Original Greek: Byzantine Textform*, edición de 2018,
> de Maurice A. Robinson y William G. Pierpont.

Fuente: **byztxt/byzantine-majority-text**
(https://github.com/byztxt/byzantine-majority-text).

Licencia: **dominio público** (Unlicense). Se usan los CSV Unicode de
`csv-unicode/ccat/no-variants`, es decir el texto sin aparato de variantes.

### Limpieza aplicada

`tools/clean.py` elimina de esta transcripción los numerales romanos de
encabezado, las siglas de manuscritos y los homóglifos latinos que dejó el OCR.
Es una adaptación del texto y, como tal, se distribuye bajo la misma licencia
CC BY-SA 4.0.

## Eclesiastés

First1KGreek todavía no ha transcrito Eclesiastés de la edición de Swete, así
que ese único libro proviene de **LukeSmithxyz/grb**
(https://github.com/LukeSmithxyz/grb), de tradición Rahlfs. Queda marcado en la
base de datos (`books.source_note`) y la app lo indica en pantalla.

Libros que Swete incluye pero que First1KGreek aún no ha digitalizado y que por
tanto faltan: las recensiones alternativas de Josué y Jueces, y el Tobías del
Códice Sinaítico.

## Interlineal y léxico

**Análisis morfológico y numeración Strong del Nuevo Testamento**: del mismo
repositorio [byztxt/byzantine-majority-text](https://github.com/byztxt/byzantine-majority-text),
en dominio público. Los códigos de Robinson se distribuyen aquí traducidos al
español; esa traducción es obra de este proyecto (`tools/morphology.py`) y se
publica bajo la licencia MIT del código.

**Diccionarios griego y hebreo de Strong** (James Strong, 1890; obra en dominio
público): versiones JSON de
[openscriptures/strongs](https://github.com/openscriptures/strongs), publicadas
por Open Scriptures bajo **CC BY-SA**. Las 14 197 entradas de léxico que viajan
en `biblia.db` conservan esa licencia.

## Léxicos de referencia

**Brown-Driver-Briggs**, *A Hebrew and English Lexicon of the Old Testament*
(1906), obra en dominio público, digitalizada por Open Scriptures en
[openscriptures/HebrewLexicon](https://github.com/openscriptures/HebrewLexicon).

**Abbott-Smith**, *A Manual Greek Lexicon of the New Testament* (1922), obra en
dominio público, digitalizada en
[translatable-exegetical-tools/Abbott-Smith](https://github.com/translatable-exegetical-tools/Abbott-Smith),
repositorio que declara expresamente el dominio público de la obra y de su
marcado.

Ambos se distribuyen en `biblia.db` como texto plano, conservando la jerarquía
de acepciones del original.

## Código de terceros

La app usa AndroidX y Jetpack Compose, bajo licencia Apache 2.0.
