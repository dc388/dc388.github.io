# Ficha de Google Play — textos listos para copiar

> Las cifras de esta ficha salen de la base que se compila: 122 libros, 60 651
> versículos y 439 705 palabras analizadas. Si cambian los textos, hay que
> revisarlas aquí antes de subir una versión nueva.

## Nombre de la app (máx. 30 caracteres)

```
Biblia Griega y Hebrea
```

La app instalada se sigue llamando **Biblia Griega**, que es lo que aparece
bajo el icono del teléfono (`app_name` en `strings.xml`). Si prefieres que
coincidan, cambia ese texto antes de compilar la versión de publicación.

## Descripción breve (máx. 80 caracteres)

```
Septuaginta, NT griego y AT hebreo con interlineal. Se lee entera sin conexión.
```

## Descripción completa (máx. 4000 caracteres)

```
Biblia Griega y Hebrea reúne los tres textos originales de la Escritura en una
sola aplicación que funciona por completo sin conexión: el Antiguo Testamento
hebreo, la Septuaginta y el Nuevo Testamento griego.

122 libros y 60 651 versículos viajan dentro de la aplicación. No hace falta
descargar nada ni tener datos móviles para leer.

EN ESPAÑOL

Debajo de cada versículo va la Reina-Valera de 1909, en dominio público, para
poder leer lo que dice el original. Se puede apagar. No está en la Septuaginta:
la Reina-Valera traduce del hebreo y la numeración griega no cuadra con la suya.

TEXTOS

• Antiguo Testamento hebreo según el Códice de Leningrado, con su vocalización
  y sus acentos, en la edición digital del Open Scriptures Hebrew Bible. Se lee
  de derecha a izquierda, como debe ser.

• Septuaginta en la edición de Henry Barclay Swete (Cambridge, 1887–1912), con
  los libros deuterocanónicos: Judit, Tobías, 1–4 Macabeos, Sabiduría de
  Salomón, Eclesiástico, Salmos de Salomón, Odas, Baruc y la Carta de Jeremías.
  Incluye las versiones dobles de Susana, Daniel y Bel y el Dragón (LXX y
  Teodoción) y los 151 salmos de la numeración griega.

• Nuevo Testamento griego en el Texto Bizantino Mayoritario de Robinson y
  Pierpont (edición de 2018), en dominio público.

INTERLINEAL Y ESTUDIO

• 439 705 palabras analizadas una a una: las 140 149 del Nuevo Testamento y las
  299 556 del Antiguo Testamento hebreo, cada una con su número Strong y su
  análisis morfológico.
• El análisis gramatical está explicado en español, no en códigos: «verbo qal
  perfecto 3ª persona masculino singular», y no «HVqp3ms».
• La definición breve de los 1 196 lemas más frecuentes también está traducida
  al español: cubre el 85 % de las palabras del Nuevo Testamento y el 75 % del
  Antiguo.
• Toca cualquier palabra y verás su lema, su transliteración, su análisis, su
  definición en el Diccionario Strong y el artículo completo del léxico de
  referencia: Brown-Driver-Briggs en hebreo y Abbott-Smith en griego.
• Concordancia completa: desde una palabra, salta a todos los versículos donde
  vuelve a aparecer.
• En la Septuaginta, que se edita como texto corrido y no lleva análisis, al
  tocar una palabra se muestra lo que esa misma forma significa en el Nuevo
  Testamento, diciendo de dónde sale. Cubre el 82 % de sus palabras.

LECTURA

• Dos modos: un versículo por línea, o texto corrido en párrafo como en las
  ediciones críticas impresas.
• Tamaño de letra e interlineado ajustables.
• Tema claro, oscuro o el del sistema.
• Marcadores y notas personales por versículo, y vuelta directa a donde dejaste
  la lectura.
• Copia y comparte un versículo o un capítulo entero.

BÚSQUEDA

Busca en todo el texto sin tener que escribir los acentos politónicos ni la
vocalización hebrea: escribe «λογος» y aparecerán también «λόγος» y «λόγῳ».
Puedes limitar la búsqueda a una de las tres colecciones.

GRATIS, CON UN ANUNCIO AL PIE

La aplicación es gratuita y completa: no hay libros bloqueados ni funciones de
pago. Se sostiene con un único anuncio al pie del lector, que nunca se cruza
sobre el texto. Si prefieres leer sin él, hay una suscripción mensual que lo
quita; todo lo demás es idéntico con ella o sin ella.

PRIVACIDAD

No hace falta crear una cuenta ni dar ningún dato. Lo que lees, tus notas y tus
marcadores se quedan en tu teléfono; no hay analítica ni rastreadores. La única
conexión que hace la aplicación es para traer el anuncio y para preguntarle a
Google Play si tienes la suscripción. Con la suscripción activa no se conecta a
nada.

Ideal para estudiantes de griego koiné y de hebreo bíblico, seminaristas,
docentes y cualquiera que quiera leer las Escrituras en su lengua original.
```

## Etiquetas sugeridas

```
biblia, griego, hebreo, septuaginta, LXX, koiné, interlineal, sin conexión
```

## Categoría

Libros y obras de consulta (alternativa: Estilo de vida).

## Clasificación de contenido

Para todos.

## Recursos gráficos

| Recurso | Tamaño | Estado |
|---|---|---|
| Icono de la ficha | 512 × 512 PNG | `docs/store/icono-512.png`, listo |
| Gráfico destacado | 1024 × 500 PNG | `docs/store/grafico-destacado-1024x500.png`, listo |
| Capturas de teléfono | mín. 2, entre 320 y 3840 px de lado | **pendientes: hay que tomarlas del teléfono** |

Los PNG están generados a partir de los SVG del mismo directorio. Para volver a
exportarlos tras editar un SVG basta abrirlo en el navegador y guardarlo, o:

```bash
inkscape docs/store/icono.svg -w 512 -h 512 -o docs/store/icono-512.png
inkscape docs/store/grafico-destacado.svg -w 1024 -h 500 \
  -o docs/store/grafico-destacado-1024x500.png
```

### Las capturas hay que hacerlas en el teléfono

Google pide que las capturas muestren la aplicación de verdad, así que no
valen ni maquetas ni montajes. Con el APK instalado, en el teléfono:
**botón de encendido + bajar volumen** a la vez, en cada pantalla que quieras
enseñar. Las que mejor cuentan lo que hace la app:

1. Génesis 1 en hebreo, con el texto alineado a la derecha.
2. El interlineal de Juan 1, con la transliteración y el Strong bajo cada palabra.
3. La ficha de una palabra abierta, con el artículo del léxico.
4. La búsqueda con resultados.
5. Los capítulos de un libro, para que se vea el tamaño del corpus.
