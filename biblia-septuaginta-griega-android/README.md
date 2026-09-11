# Biblia Griega — Septuaginta y Nuevo Testamento

Aplicación Android nativa (Kotlin + Jetpack Compose) para leer la **Septuaginta**
(Antiguo Testamento griego) y el **Nuevo Testamento griego** sin conexión.

El texto completo viaja dentro del APK: **37 443 versículos en 83 libros**.
La app no pide permisos, no usa internet y no recoge ningún dato.

## Qué incluye

| Colección | Edición | Libros | Versículos | Licencia |
|---|---|---|---|---|
| Septuaginta | H. B. Swete, Cambridge 1887–1912 | 56 | 29 490 | CC BY-SA 4.0 |
| Nuevo Testamento | Robinson–Pierpont, Texto Bizantino Mayoritario 2018 | 27 | 7 953 | Dominio público |

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

## Funciones

- Lector con dos modos: versículo por línea o texto corrido en párrafo.
- Tamaño de letra e interlineado ajustables; tema claro, oscuro o del sistema.
- Búsqueda en todo el texto **sin escribir acentos y por comienzo de palabra**:
  `λογ` encuentra `λόγος`, `λόγῳ` y `λόγον`, pero no `φλογός`. Se puede limitar
  a una colección.
- Marcadores por versículo y «continuar leyendo».
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

## Regenerar la base de datos

`app/src/main/assets/biblia.db` está versionada en el repositorio, pero se puede
reconstruir desde las fuentes originales:

```bash
python3 tools/build_db.py
```

El script clona los repositorios de origen en `build/sources/`, normaliza los
textos y arma el SQLite. Solo necesita Python 3.9+ y `git`.

Esquema: `collections` → `books` → `verses`. Cada versículo guarda además
`text_norm`, una copia en minúsculas, sin diacríticos y sin puntuación, que es
la que hace posible buscar sin acentos.

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
docs/                              guía de publicación y ficha de la tienda
```

## Licencias

El código es MIT. Los textos griegos conservan las suyas: ver
[NOTICE.md](NOTICE.md) y [LICENSE](LICENSE).
