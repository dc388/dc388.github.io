# Biblia Exegética Universal — evaluación técnica

Análisis de la propuesta «Proyecto: Biblia Exegética Universal» frente a lo que
ya existe en este repositorio. Todas las fuentes citadas aquí fueron clonadas y
comprobadas el 11 de septiembre de 2026; los conteos son reales, no estimados.

---

## 1. Una corrección que cambia el plan

> «el Nuevo Testamento (Nestle-Aland/Textus Receptus libres de derechos)»

**Nestle-Aland no es libre de derechos.** El texto de NA28 (y NA27) es propiedad
de la Deutsche Bibelgesellschaft y su redistribución completa exige una licencia
pagada. Publicar una app con el texto de NA28 sin ese contrato es motivo de
retirada de Google Play por reclamación de derechos de autor.

El resto de la propuesta sí acierta: Strong, BDB, Thayer, Matthew Henry y
Jamieson-Fausset-Brown están en dominio público, y el Texto Masorético también.

Alternativas reales para un texto crítico libre:

| Edición | Estado | Nota |
|---|---|---|
| **Nestle 1904** | Dominio público | La edición de Eberhard Nestle, con morfología, en [biblicalhumanities/Nestle1904](https://github.com/biblicalhumanities/Nestle1904). Es lo más cercano a «un Nestle» que se puede distribuir libremente. |
| Westcott-Hort 1881 | Dominio público | Texto crítico clásico. |
| Tischendorf 8ª | Dominio público | |
| Textus Receptus (Scrivener 1894) | Dominio público | Base del linaje Reina-Valera / KJV. |
| Robinson-Pierpont 2018 | Dominio público | **Ya incluido en esta app.** |
| SBLGNT | Libre con condiciones | Su licencia restringe la redistribución del texto completo; no conviene para tienda. |

---

## 2. Qué está hecho y qué falta

La propuesta tiene cuatro módulos. Este es el estado real de cada uno.

### Base textual crítica — parcialmente hecho

| Componente | Estado | Fuente verificada | Licencia |
|---|---|---|---|
| Septuaginta (AT griego) | **Hecho** — 29 490 versículos | Swete / First1KGreek | CC BY-SA 4.0 |
| Nuevo Testamento griego | **Hecho** — 7 953 versículos | Robinson-Pierpont 2018 | Dominio público |
| Hebreo/Arameo (Masorético) | **Hecho** — 23 213 versículos | [openscriptures/morphhb](https://github.com/openscriptures/morphhb) (OSHB) | **CC BY 4.0 — permite uso comercial** |

El Antiguo Testamento hebreo es la incorporación más rentable que queda: OSHB
trae el Códice de Leningrado completo en OSIS XML **ya etiquetado con números
Strong y claves morfológicas**, y su licencia es más permisiva que la de la
Septuaginta que ya distribuimos.

### Alineación interlinear — probada y casi gratis para el NT

Esto era el riesgo técnico principal de la propuesta. Ya no lo es.

El repositorio de Robinson-Pierpont que esta app ya clona incluye, además del
texto acentuado, una versión etiquetada en `csv-unicode/strongs/with-parsing/`:

```
Juan 1:1 →  εν 1722 {PREP}  αρχη 746 {N-DSF}  ην 1510 {V-IAI-3S}
            ο 3588 {T-NSM}  λογος 3056 {N-NSM} …
```

Comprobación hecha sobre el corpus entero: **los 7 953 versículos alinean 1:1**
entre el texto acentuado que mostramos y el etiquetado Strong/morfología.
Cero discrepancias de conteo de palabras. La vinculación palabra-por-palabra del
Nuevo Testamento es, en la práctica, un problema resuelto: es un `JOIN`, no un
proyecto de alineación lingüística.

Prototipo ya ejecutado, resolviendo Strong + morfología + glosa:

```
εν      G1722  PREP      ἐν      "in," at, (up-)on, by, etc.
αρχη    G746   N-DSF     ἀρχή    a commencement, or (concretely) chief…
ην      G1510  V-IAI-3S  εἰμί    I exist (used only when emphatic)
λογος   G3056  N-NSM     λόγος   something said (including the thought)…
```

**El hueco real está en la Septuaginta.** No existe un etiquetado morfológico de
la LXX en dominio público con licencia limpia: el de CATSS, que es el estándar,
prohíbe el uso comercial. Un interlineal de la LXX exige o negociar esa licencia,
o generar la morfología con herramientas propias. Es la parte cara del proyecto y
conviene decidirla pronto, no al final.

### Léxico integrado — disponible, calidad desigual

| Recurso | Fuente verificada | Estado |
|---|---|---|
| Strong griego | [openscriptures/strongs](https://github.com/openscriptures/strongs) | **5 523 entradas cargadas y probadas** |
| Strong hebreo | openscriptures/strongs | Disponible (XML) |
| Brown-Driver-Briggs | [openscriptures/HebrewLexicon](https://github.com/openscriptures/HebrewLexicon) | Disponible (XML) |
| Thayer | Repositorios comunitarios de poca difusión | Existe, **calidad sin auditar** |

Los tres primeros vienen de Open Scriptures y son sólidos. Thayer solo aparece en
repositorios recientes y con poco uso: antes de incorporarlo hay que cotejarlo
contra el original, no darlo por bueno.

### Motor de comentarios públicos — el módulo más caro

Los textos clásicos están en dominio público, pero solo los encontré en
repositorios comunitarios sin auditar; habría que verificar la digitalización.

El problema no es ese. El problema es el **wiki moderado**. Hoy esta app tiene una
propiedad muy valiosa: cero permisos, cero red, cero recogida de datos. Eso hace
que la declaración de seguridad de datos de Play sea trivial y que la
responsabilidad legal sea nula.

Un sistema de aportes de usuarios lo cambia todo a la vez:

- exige servidor, cuentas, backend y coste recurrente;
- obliga a declarar recogida de datos en Play y a rehacer la política de privacidad;
- somete la app a las reglas de contenido generado por usuarios de Google Play,
  que exigen moderación, sistema de denuncias y bloqueo de usuarios;
- en materia religiosa, la moderación no es un detalle técnico sino una carga de
  trabajo continua y con riesgo reputacional.

Mi recomendación: **dejarlo para el final, como producto aparte**, y no mezclarlo
con la app de lectura. Notas privadas locales dan el 80 % del valor con el 2 % del
coste, y no tocan ninguna de esas obligaciones.

---

## 3. Dónde discrepo de las tecnologías propuestas

**PostgreSQL.** Innecesario. La app es offline y el corpus completo con léxico e
interlineal cabe holgadamente en SQLite. Postgres solo tendría sentido el día que
exista el módulo comunitario con servidor, y esa decisión puede tomarse entonces.

**Flutter o React Native.** El argumento —un solo código para Android e iOS— es
legítimo, pero hay que sopesarlo: ya existe una app nativa en Kotlin funcionando,
y reescribirla la tira entera. Además, este producto es tipografía pura: griego
politónico y hebreo con vocalización y cantilación, en apilamiento de diacríticos
poco común. Es justo el terreno donde el renderizado nativo da menos sorpresas.

Lo importante: **el activo real no es la app, es la base de datos y el
importador**. Esos son idénticos en Kotlin, Flutter o Swift. Si iOS importa, la
decisión conviene tomarla ahora, antes de construir la capa exegética encima.

**OSIS/USFM como formato de datos.** De acuerdo como formato de *intercambio* —de
hecho OSHB viene en OSIS y hay que leerlo—, pero no como formato de *ejecución*.
En el dispositivo, el texto debe estar en tablas normalizadas indexadas; parsear
XML en tiempo de lectura sería lento y sin motivo.

**Un detalle concreto que la propuesta no menciona:** el hebreo se escribe de
derecha a izquierda. Ya está resuelto: el manifiesto declara `supportsRtl` y el
cuerpo del capítulo se dibuja en la dirección que marca la lengua del texto,
mientras la interfaz en español se queda de izquierda a derecha.

---

## 4. Orden de trabajo propuesto

Ordenado por valor entregado sobre coste, no por el orden de la propuesta.

1. ~~**Interlineal del Nuevo Testamento.**~~ **Hecho.** 140 149 palabras con
   Strong y morfología, sin un solo versículo sin analizar, y los 1 055 códigos
   de Robinson traducidos al español.
2. ~~**Léxico Strong griego.**~~ **Hecho.** 5 523 entradas, con concordancia:
   desde cualquier palabra se ve dónde más aparece.
3. ~~**Antiguo Testamento hebreo (OSHB).**~~ **Hecho.** 39 libros, 23 213
   versículos y 299 556 palabras analizadas (98,05 % del texto), con el arameo
   de Daniel y Esdras marcado. Lector de derecha a izquierda.
4. **Léxico hebreo.** Strong hebreo **hecho** (8 674 entradas). Falta
   Brown-Driver-Briggs, que da definiciones mucho más ricas.
5. **Notas personales locales.** Sin servidor, sin cambiar la privacidad.
6. **Comentarios clásicos.** Previa auditoría de la digitalización.
7. **Interlineal de la Septuaginta.** Requiere resolver antes la licencia de la
   morfología.
8. **Comunidad y wiki.** Producto aparte, con servidor y moderación.

Los pasos 1 a 4 ya están implementados. La base pasó de 18,4 MB a 59 MB (unos
20 MB comprimidos en el APK).

La decisión sobre iOS sigue abierta, pero cada vez pesa menos: el activo es la
base de datos y el importador, que no cambian de lenguaje.

---

## 5. Fuentes verificadas

Comprobadas por clonación directa, no por referencia:

| Repositorio | Contenido | Licencia |
|---|---|---|
| `openscriptures/morphhb` | Códice de Leningrado + morfología + Strong | CC BY 4.0 |
| `openscriptures/strongs` | Diccionarios Strong griego y hebreo | Dominio público (JSON CC BY-SA) |
| `openscriptures/HebrewLexicon` | Brown-Driver-Briggs | Dominio público |
| `byztxt/byzantine-majority-text` | NT griego + Strong + morfología | Dominio público |
| `biblicalhumanities/Nestle1904` | NT crítico Nestle 1904 + morfología | Dominio público |
| `nathans/lxx-swete` | Septuaginta de Swete | CC BY-SA 4.0 |
