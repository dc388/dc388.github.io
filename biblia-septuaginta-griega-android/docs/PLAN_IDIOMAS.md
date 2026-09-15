# Que la app hable el idioma de quien la abre

La 1.0 está enteramente en español: los textos de la interfaz son literales en
el código, y la única traducción del texto bíblico es la Reina-Valera de 1909.
Este documento explica cómo pasa a hablar 31 idiomas y, sobre todo, qué cuesta
cada capa, porque no cuestan lo mismo ni de lejos.

## Las tres capas

| Capa | Qué es | Coste real |
|---|---|---|
| Interfaz | ~200 textos: «Ajustes», «Capítulo 3 de 16» | Mecánico |
| Texto bíblico | Una traducción completa por idioma | Ya existe, hay que procesarla |
| Léxico y glosas | 1 196 glosas + 14 197 artículos Strong | **Aquí está el trabajo** |

La tercera es la que no se puede resolver con un traductor automático. Una glosa
es una sola palabra que enseña qué significa un lema griego; si dice «amor» donde
debía decir «afecto», alguien que está aprendiendo aprende mal. El español está
hecho a mano. El inglés no hay que traducirlo: el diccionario Strong **está
escrito en inglés**, así que para el inglés basta con dejar de traducir.

Para los demás idiomas, mientras las glosas no estén revisadas, se cae al inglés
y se avisa en pantalla. Es honesto y es útil; fingir una traducción no lo sería.

## Las 31 traducciones y su licencia

Todas de `seven1m/open-bibles`. Dominio público salvo donde se indique.

| Idioma | Versión |
|---|---|
| Albanés | Albanian Bible |
| Alemán | Lutero 1912 |
| Búlgaro | Bulgarian Bible |
| Checo | Bible kralická |
| Cheroqui | Nuevo Testamento — **solo NT** |
| Chino simplificado | Chinese Union Version |
| Chino tradicional | Chinese Union Version |
| Coreano | Korean Bible |
| Croata | Croatian Bible |
| Danés | Danish Bible — **sin Abdías, Filemón, 1 Juan, 2 Juan ni Judas** |
| Español | Reina-Valera 1909 |
| Finés | Finnish Bible |
| Francés | Ostervald 1996 |
| Holandés | Statenvertaling (1637) |
| Húngaro | Károli |
| Inglés | King James 1769 y World English Bible |
| Italiano | Riveduta 1927 |
| Japonés | Kougo |
| Latín | Vulgata Clementina |
| Letón | Latvian Bible — **solo NT** |
| Maorí | Maori Bible |
| Noruego | Norwegian Bible — **sin Proverbios ni Cantares** |
| Polaco | Gdańska |
| Portugués | João Ferreira de Almeida |
| Rumano | Cornilescu corregida |
| Ruso | Sinodal |
| Suajili | Swahili Bible — **solo NT, y sin Filipenses** |
| Sueco | Swedish Bible |
| Tagalo | Ang Dating Biblia |
| Tailandés | Thai Bible |
| Turco | Turkish Bible — **sin Abdías** |
| Vietnamita | Cadman 1934 |

## Por qué se descargan y no viajan dentro

Medido, no estimado:

- una traducción suelta: entre **1,0 y 12,2 MB** en disco, **1,6 MB** comprimida
  de media (el tailandés es el más pesado; el griego politónico y la escritura
  tailandesa ocupan más bytes por letra que el alfabeto latino)
- las 32 juntas: **154 MB** en disco, **48 MB** comprimidas, encima de los 73 MB
  que ya pesa la base

Una aplicación de 220 MB no se instala: se abandona a la mitad de la descarga.
Y nadie necesita 31 traducciones; necesita **una**.

Así que la app trae el griego, el hebreo, el léxico y la morfología —lo que no
cambia con el idioma— y cada traducción se descarga aparte, en unos segundos,
desde `dc388.github.io`. Ese sitio ya está publicado, no cuesta nada y es del
mismo dueño que la app: ni servidor que mantener ni factura que pagar.

La app **no deja de funcionar sin conexión**. El griego y el hebreo, que son el
producto, siguen dentro. Lo que se descarga una vez se queda para siempre.

## Cómo queda por dentro

- Cada idioma es un archivo SQLite pequeño, `traduccion-<código>.db`, con una
  sola tabla. Se enchufa con `ATTACH DATABASE` a la base principal.
- El primer arranque propone el idioma del teléfono. Si no hay traducción para
  ese idioma, se ofrece el inglés y se dice por qué.
- En Ajustes se puede añadir o quitar traducciones; quitar una borra su archivo.
- La interfaz usa `strings.xml` de Android, que elige sola según el teléfono.

## El orden en que se hace

1. **Sacar la interfaz a `strings.xml`.** Hoy son literales en el código. Sin
   esto no hay nada que traducir. Ninguna función cambia.
2. **Generalizar `tools/traduccion.py`** para que lea los tres formatos de
   `open-bibles` —USFX, OSIS y Zefania— y emita un `.db` por idioma.
3. **Publicar los `.db`** en el sitio, con un índice JSON que diga qué hay,
   cuánto pesa y con qué firma, para que la app compruebe lo que baja.
4. **Descarga y gestión** dentro de la app.
5. **Traducir la interfaz**, empezando por inglés y portugués.
6. **Glosas en inglés** (es dejar de traducir) y luego las demás.

Los pasos 1 y 2 no tocan nada de lo que ya funciona y se pueden hacer mientras
la 1.0 está en pruebas.

## Lo que hay que vigilar

- **La numeración no cuadra entre tradiciones.** Ya pasa con la Septuaginta y la
  Reina-Valera, y por eso la traducción no se muestra ahí. Cada idioma nuevo hay
  que comprobarlo libro por libro, no darlo por bueno.
- **Idiomas que no leo.** Puedo procesar el tailandés o el cheroqui, pero no
  puedo juzgar si la interfaz traducida suena natural. Para esos, lo honesto es
  dejar la interfaz en inglés hasta que alguien que lo hable la revise.
- **Derecha a izquierda.** El hebreo ya lo maneja la app. El árabe no está en la
  lista; si algún día entra, hay que revisar la maquetación entera.


## Lo que se encontró al procesarlas de verdad

Las 32 se leen y Juan 3:16 sale correcto en todas. Pero seis digitalizaciones
libres están incompletas, y se comprobó que el hueco está en el archivo de
origen, no en el lector: se contaron los libros dentro del propio XML.

| Idioma | Qué le falta |
|---|---|
| Cheroquí | Solo Nuevo Testamento (así se publicó) |
| Letón | Solo Nuevo Testamento |
| Suajili | Solo Nuevo Testamento, y sin Filipenses |
| Danés | Abdías, Filemón, 1 Juan, 2 Juan, Judas |
| Noruego | Proverbios, Cantares |
| Turco | Abdías |

**Eso se dice antes de descargar, no después.** El índice que publica el
generador lleva un campo `resumen` con «completa», «solo Nuevo Testamento» o
«faltan N libros», y la lista exacta de los que faltan. Quien elige turco tiene
derecho a saber que Abdías se quedará en griego antes de bajar el archivo.

Seis idiomas tienen **más** versículos que los 31 102 de referencia: alemán,
checo, francés, latín, ruso y croata. No es un error: cada tradición numera
distinto los títulos de los Salmos y algún versículo largo partido en dos.

## Lo que ya está hecho

- `tools/canon.py` — los 66 libros y cómo los nombra cada formato, en un solo
  sitio, para que un error de correspondencia se arregle en una línea.
- `tools/traducciones.py` — lee USFX, OSIS y Zefania, incluidos los OSIS que
  marcan los versículos con `sID`/`eID` en vez de contenerlos.
- `tools/build_traducciones.py` — genera un `.db` por idioma más un
  `index.json` con peso, cobertura y `sha256` de cada uno.

Nada de esto toca la aplicación todavía: son herramientas que se pueden correr
y comprobar mientras la 1.0 está en pruebas.
