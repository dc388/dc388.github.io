# Biblia en lenguas originales — hebreo y griego

Aplicación Android nativa (Kotlin + Jetpack Compose) para leer sin conexión el
**Antiguo Testamento hebreo**, la **Septuaginta** y el **Nuevo Testamento
griego**, con interlineal, análisis morfológico en español y los léxicos de
referencia de cada lengua.

Todo viaja dentro del APK: **60 656 versículos en 122 libros** y **439 705
palabras analizadas**. La app no pide permisos, no usa internet y no recoge
ningún dato.

## Qué incluye

| Colección | Edición | Libros | Versículos | Palabras analizadas | Licencia |
|---|---|---|---|---|---|
| Antiguo Testamento hebreo | Códice de Leningrado (OSHB) | 39 | 23 213 | 299 556 | CC BY 4.0 |
| Septuaginta | H. B. Swete, Cambridge 1887–1912 | 56 | 29 490 | — | CC BY-SA 4.0 |
| Nuevo Testamento | Robinson–Pierpont, Bizantino 2018 | 27 | 7 953 | 140 149 | Dominio público |

El Antiguo Testamento hebreo incluye las secciones en **arameo** de Daniel y
Esdras, marcadas como tales en el análisis. El texto se lee de derecha a
izquierda, con la interfaz en español de izquierda a derecha.

La Septuaginta trae los deuterocanónicos y las recensiones dobles que trae Swete:
Judit, Tobías, 1–4 Macabeos, Sabiduría, Eclesiástico, Salmos de Salomón, Odas,
Baruc, Carta de Jeremías, y las versiones LXX y de Teodoción de Susana, Daniel y
Bel y el Dragón. La numeración de Salmos es la de la LXX (151 salmos).

## Calidad del texto

La transcripción de Swete hecha por First1KGreek arrastra restos de OCR:
numerales romanos de encabezado pegados a las palabras, siglas de manuscritos
sueltas y letras latinas confundidas con griegas. `tools/clean.py` los elimina
durante la importación y baja los versículos afectados de **450 a 91**
(0,24 % del total).

Los 91 restantes son palabras a las que el OCR les comió letras (`Αἴγυπτον` →
`Μrπτον`); repararlas exigiría cotejar con la edición impresa, así que se dejan
tal cual en lugar de inventar texto. El importador los cuenta al terminar.

Si prefieres completitud textual sobre claridad de licencia, existe una
alternativa: el texto de tradición **Rahlfs** que distribuye
[LukeSmithxyz/grb](https://github.com/LukeSmithxyz/grb) tiene un 0,39 % de
artefactos y no le faltan pasajes, pero su transcripción digital no declara
licencia (el texto de Rahlfs de 1935 sí está en dominio público en las
jurisdicciones de vida + 70 años). Por eso aquí se usa Swete por defecto.
De ese origen ya viene Eclesiastés, porque Swete no está digitalizado para
ese libro.

## Léxicos

Cada palabra analizada enlaza con dos obras: el **Diccionario Strong** (1890),
que da la definición de una línea, y el léxico de referencia de su lengua, que
da el artículo completo con sus acepciones numeradas y las citas de cada una.

| Lengua | Léxico de referencia | Artículos | Cobertura | Licencia |
|---|---|---|---|---|
| Hebreo | Brown-Driver-Briggs (1906) | 9 247 | 99,98 % de las palabras | Dominio público |
| Griego | Abbott-Smith (1922) | 5 363 | 99,89 % de las palabras del NT | Dominio público |

La propuesta original pedía Thayer para el griego; Abbott-Smith cubre la misma
necesidad, está mucho mejor digitalizado y su licencia es inequívoca.

En hebreo, el enlace respeta los **homónimos**: el lema de OSHB distingue
`1254 a` («crear», el de Génesis 1:1) de `1254 b` («engordar»), y esa letra
decide qué artículo se muestra. Afecta a 59 092 palabras, una de cada cinco del
Antiguo Testamento.

Bajo cada palabra del interlineal aparece además una **definición breve**. En
hebreo sale del índice de BDB; en griego, de la primera glosa de Abbott-Smith,
tal cual la da la obra. En unas pocas palabras funcionales esa primera glosa es
la de la acepción con que el léxico abre y no la más corriente —`ὁ` sale como
*he*, porque Abbott-Smith empieza por el uso demostrativo homérico—. Se prefiere
esa rareza a inventar una traducción que la fuente no dice.

## Interlineal

Las 140 149 palabras del Nuevo Testamento llevan su número Strong y su análisis
morfológico de Robinson, alineados palabra a palabra con el texto acentuado. Las
299 556 del Antiguo Testamento hebreo (98,05 % del texto) traen los suyos desde
OSHB; el resto son qere/ketiv y partículas a las que OSHB no asigna número
Strong.

Al tocar una palabra se abre su ficha: lema, transliteración, análisis
gramatical **en español**, definición del Diccionario Strong y concordancia
completa de dónde más aparece esa misma palabra.

```
Ἐν      ἀρχῇ            ἦν                          ὁ          λόγος,
en      archḗ           eimí                        ho         lógos
G1722   G746            G1510                       G3588      G3056
prep.   dativo sing.    imperfecto, voz activa,     artículo   nominativo
        femenino        indicativo, 3ª pers. sing.  nom. s. m. sing. masc.
```

Los **4 490 códigos morfológicos** distintos del corpus están traducidos al
español, y la traducción se valida en cada compilación: si apareciera un código
desconocido, el importador avisa en vez de mostrar una etiqueta inventada.

- Griego (1 055 códigos): `tools/morphology.py` decodifica el esquema de
  Robinson.
- Hebreo y arameo (3 435): la gramática no se reimplementa. OSHB publica en
  `parsing/Oshm.xml` la clave oficial de sus códigos, y `tools/hebrew.py`
  traduce esas descripciones con un glosario cerrado de 96 términos. Las ocho
  combinaciones que faltan en la propia clave se reconstruyen componiendo la
  descripción de cada morfema.

## Funciones

- Lector con dos modos: versículo por línea o texto corrido en párrafo, con
  dirección de escritura según la lengua del texto.
- Modo interlineal con lema, transliteración y número Strong bajo cada palabra.
- Ficha de palabra con la definición de Strong, el artículo completo del léxico
  de referencia y la concordancia de todas sus apariciones.
- Tamaño de letra e interlineado ajustables; tema claro, oscuro o del sistema.
- Búsqueda en todo el texto **sin escribir acentos y por comienzo de palabra**:
  `λογ` encuentra `λόγος`, `λόγῳ` y `λόγον`, pero no `φλογός`. En hebreo la
  misma normalización quita niqqud y cantilación, así que se busca por
  consonantes. Se puede limitar a una colección.
- Marcadores por versículo y «continuar leyendo».
- **Notas personales** por versículo, guardadas solo en el dispositivo.
- Copiar y compartir versículo o capítulo completo.

## Compilar

Requiere JDK 17. El SDK de Android lo resuelve Gradle.

```bash
./gradlew assembleDebug        # APK de depuración
./gradlew bundleRelease        # AAB para Google Play (necesita firma)
```

También hay CI: cada push compila el APK de depuración y lo publica como
artefacto (`.github/workflows/build.yml`). Al empujar una etiqueta `v*` se
genera el AAB firmado (`.github/workflows/release.yml`).

### Comprobar la sintaxis sin SDK

```bash
./tools/check_kotlin.sh
```

Baja el compilador de Kotlin de Maven Central y pasa el parser sobre las fuentes.
Sirve donde no se puede compilar de verdad —sin SDK de Android, o sin acceso a
dl.google.com para AGP y Compose—: señala paréntesis sin cerrar, comas de más y
plantillas de cadena mal formadas, que es justo lo que se escapa al revisar a
ojo. No comprueba nada que dependa de resolver símbolos; de eso se encarga CI.

## Regenerar la base de datos

`app/src/main/assets/biblia.db` está versionada en el repositorio, pero se puede
reconstruir desde las fuentes originales:

```bash
python3 tools/build_db.py
```

El script clona los repositorios de origen en `build/sources/`, normaliza los
textos y arma el SQLite. Solo necesita Python 3.9+ y `git`.

Esquema: `collections` → `books` → `verses` → `words`, más `lexicon`,
`articles` y `morph_codes`. Cada versículo guarda además `text_norm`, una copia en
minúsculas, sin diacríticos y sin puntuación, que es la que hace posible buscar
sin acentos.

El importador comprueba siete invariantes y aborta si alguna se rompe: que cada
palabra tenga entrada de léxico y descripción morfológica, que ningún versículo
del Nuevo Testamento ni del Antiguo hebreo quede sin analizar, que concatenar
las palabras de un versículo del NT reproduzca su texto carácter por carácter, y
que la cobertura de los léxicos de referencia no baje del 99 % en ninguna de las
dos lenguas.
`tools/verify_db.py` repite esas comprobaciones en CI sobre la base versionada.

La base ocupa 63 MB, unos 21 MB comprimidos dentro del APK.

## Publicar en Google Play

Ver [docs/PUBLICAR_EN_PLAY.md](docs/PUBLICAR_EN_PLAY.md): creación del almacén de
claves, secretos de GitHub Actions, ficha de la tienda y declaración de
seguridad de datos.

## Estructura

```
app/src/main/
  assets/biblia.db                 texto bíblico completo (SQLite)
  java/com/dc388/bibliagriega/
    MainActivity.kt                navegación
    data/                          repositorio SQLite, preferencias, modelos
    ui/                            ViewModel, tema, pantallas Compose
tools/build_db.py                  generador de la base de datos
tools/clean.py                     limpieza de artefactos de OCR
tools/morphology.py                códigos de Robinson traducidos al español
tools/hebrew.py                    OSIS de OSHB y morfología hebrea en español
tools/bdb.py                       léxico Brown-Driver-Briggs
tools/abbott_smith.py              léxico griego de Abbott-Smith
tools/verify_db.py                 comprobaciones de integridad para CI
tools/check_kotlin.sh              parser de Kotlin sin SDK de Android
docs/                              guía de publicación y ficha de la tienda
```

## Hacia una Biblia exegética

[docs/PLAN_EXEGETICO.md](docs/PLAN_EXEGETICO.md) evalúa la ampliación del
proyecto a interlineal con números Strong, morfología, léxicos y Antiguo
Testamento hebreo: fuentes verificadas, licencias, y qué partes son baratas y
cuáles caras.

Los cinco primeros pasos de esa hoja de ruta **ya están implementados**,
más las notas personales: interlineal del NT, léxico Strong griego, Antiguo
Testamento hebreo, léxico hebreo, los léxicos de referencia de ambas lenguas y
las notas locales. Lo siguiente serían los comentarios clásicos.

## Licencias

El código es MIT. Los textos conservan las suyas: ver
[NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).
