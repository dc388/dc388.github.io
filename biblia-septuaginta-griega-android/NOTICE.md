# Atribuciones

Esta aplicación redistribuye textos preparados por terceros. Estas son las
atribuciones exigidas por sus licencias.

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

## Código de terceros

La app usa AndroidX y Jetpack Compose, bajo licencia Apache 2.0.
