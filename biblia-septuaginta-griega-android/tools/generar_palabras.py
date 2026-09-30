"""Una página por palabra del griego y del hebreo bíblicos.

Por qué existe esto
-------------------
En «datos/lexico» hay 14 197 entradas de diccionario —Abbott-Smith para el
griego, Brown-Driver-Briggs para el hebreo, más las definiciones de Strong,
todo traducido al español a mano y a máquina en los meses anteriores— y hasta
ahora no había ni una sola página que un buscador pudiera leer. Todo eso vivía
dentro del lector, detrás de una almohadilla, invisible para Google.

Es justo lo que más falta hace en español. Quien escribe «qué significa ágape
en griego» o «hesed significado hebreo» hoy encuentra blogs de tercera mano.
Aquí está el artículo del léxico, y además —y esto no lo tiene casi nadie— la
lista de dónde sale de verdad la palabra en el texto, sacada del análisis
palabra por palabra del corpus: 439 705 apariciones etiquetadas.

Qué se publica y qué no
-----------------------
No se hace una página por entrada y ya está. Una página con cuatro palabras
sueltas no le sirve a nadie y un buscador la cuenta como relleno, que es peor
que no tenerla. Se publica la entrada cuando hay de verdad algo que leer:

  * artículo del léxico traducido al español, o
  * definición en español y al menos cinco apariciones en el texto, que es
    cuando la concordancia ya dice algo por sí sola.

Las que no llegan se quedan fuera. Se dice cuántas son al final.

Lo que no se puede dar
----------------------
El análisis palabra por palabra solo cubre el Antiguo Testamento hebreo y el
Nuevo Testamento griego, que son los que vienen etiquetados de origen. La
Septuaginta, los Padres y los pseudoepígrafos no están etiquetados, así que
una palabra puede salir allí y esta página no contarlo. Se avisa en la página
en vez de dejar creer que la cuenta es de todo el corpus.
"""

from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import unicodedata

from generar_paginas import CSS, cabecera, escribe, recorta, urlset
from traducir_strong import traducir

BASE = "https://dc388.github.io/biblia"

# El mismo mapa de colecciones que usa generar_paginas para las carpetas del
# texto, porque desde aquí hay que enlazar allí.
SLUG_COLECCION = {"at": "hebreo", "lxx": "septuaginta", "nt": "nuevo-testamento",
                  "padres": "padres-apostolicos", "pseudo": "pseudoepigrafos"}

# Dónde se mete todo esto dentro del sitio.
CARPETA = "palabras"

LENGUAS = {
    "G": ("griego", "griego", 'lang="grc"', "Nuevo Testamento griego"),
    "H": ("hebreo", "hebreo", 'lang="he" dir="rtl"', "Antiguo Testamento hebreo"),
}

# El corpus que sí lleva análisis palabra por palabra, y de dónde sale.
CORPUS_ETIQUETADO = {"at": "Antiguo Testamento hebreo", "nt": "Nuevo Testamento griego"}

# Cuántos versículos de muestra se enseñan. Más no ayuda: la página se vuelve
# una lista y el lector se pierde. Menos no deja ver el uso de la palabra.
MUESTRAS = 12

# Cuántas apariciones se guardan por palabra antes de dejar de contar sitios.
# La cuenta total sigue siendo exacta; esto solo limita la lista de dónde.
TOPE_SITIOS = 400


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "x"


def carga_lexico(datos: pathlib.Path) -> dict:
    lexico = {}
    for p in sorted((datos / "lexico").glob("*.json")):
        lexico.update(json.loads(p.read_text(encoding="utf-8")))
    return lexico


def carga_concordancia(datos: pathlib.Path, orden: dict) -> tuple[dict, dict]:
    """Dónde sale cada palabra, leyendo el análisis palabra por palabra.

    Devuelve dos cosas: cuántas veces sale cada número de Strong (exacto) y
    hasta TOPE_SITIOS sitios concretos, en el orden del canon. Se guarda
    también la forma tal como aparece allí, que es medio motivo de la página:
    ver que ἀγάπη sale como ἀγάπην o como ἀγάπῃ según el caso.
    """
    cuenta: dict[str, int] = {}
    sitios: dict[str, list] = {}
    for cid in CORPUS_ETIQUETADO:
        carpeta = datos / cid
        if not carpeta.is_dir():
            continue
        # En el orden del canon, no en el alfabético del código de carpeta:
        # así la muestra de cada palabra empieza por donde empieza la Biblia.
        for libro in sorted(carpeta.iterdir(),
                            key=lambda d: orden.get((cid, d.name), 9999)):
            if not libro.is_dir():
                continue
            archivos = sorted(libro.glob("*.palabras.json"),
                              key=lambda p: int(p.name.split(".")[0]))
            for archivo in archivos:
                cap = int(archivo.name.split(".")[0])
                d = json.loads(archivo.read_text(encoding="utf-8"))
                for vers in sorted(d, key=lambda x: (len(x), x)):
                    for palabra in d[vers]:
                        forma, strong = palabra[0], palabra[1]
                        if not strong:
                            continue
                        cuenta[strong] = cuenta.get(strong, 0) + 1
                        lista = sitios.setdefault(strong, [])
                        if len(lista) < TOPE_SITIOS:
                            lista.append((cid, libro.name, cap, vers, forma))
    return cuenta, sitios


class Versiculos:
    """Lee los capítulos del corpus según se piden, y se los guarda.

    Sin esto, sacar doce versículos de muestra para once mil palabras abriría
    el mismo archivo miles de veces.
    """

    def __init__(self, datos: pathlib.Path):
        self.datos = datos
        self.cache: dict[tuple, dict] = {}

    def __call__(self, cid: str, libro: str, cap: int) -> dict:
        clave = (cid, libro, cap)
        if clave not in self.cache:
            ruta = self.datos / cid / libro / f"{cap}.json"
            try:
                bruto = json.loads(ruta.read_text(encoding="utf-8"))
            except OSError:
                bruto = []
            # El versículo se busca por número; el sufijo no lo trae el
            # análisis palabra por palabra, así que se queda el primero.
            d: dict[str, dict] = {}
            for v in bruto:
                d.setdefault(str(v.get("v")), v)
            if len(self.cache) > 300:
                self.cache.clear()
            self.cache[clave] = d
        return self.cache[clave]


# Lo que va pegado a una palabra en el texto y no es la palabra: comas, puntos
# altos, signos de interrogación griegos, guiones de los códices.
_PEGADO = " \t·,.;:!?'\"«»()[]{}\u00b7\u0387\u037e\u2014\u2013-\u05be\u05c3\u05c0"


def limpia_forma(forma: str) -> str:
    return forma.strip(_PEGADO) or forma


def reparte(sitios: list, cuantos: int) -> list:
    """Coge la muestra de libros distintos antes de repetir libro.

    Sin esto la muestra se apelotona: para ἀγάπη los doce renglones caían casi
    todos en 1 Corintios, porque los libros se recorren en orden y allí sale
    mucho. Se hace una vuelta cogiendo uno de cada libro, luego otra, y así:
    quien llega a la página ve de un vistazo que la palabra es de Pablo y de
    Juan, no solo del capítulo del amor.
    """
    por_libro: dict[tuple, list] = {}
    orden: list[tuple] = []
    for s in sitios:
        clave = (s[0], s[1])
        if clave not in por_libro:
            por_libro[clave] = []
            orden.append(clave)
        por_libro[clave].append(s)
    salida = []
    vuelta = 0
    while len(salida) < cuantos:
        puestos = 0
        for clave in orden:
            if vuelta < len(por_libro[clave]):
                salida.append(por_libro[clave][vuelta])
                puestos += 1
                if len(salida) >= cuantos:
                    break
        if not puestos:
            break
        vuelta += 1
    return salida


def repara_glosa(glosa: str) -> str:
    """Quita el jirón que dejó la fuente cuando se comió la etimología.

    En 110 de las 14 178 entradas, el dato de Strong viene ya partido: la
    etimología se perdió y la definición empieza en mitad de una frase, con un
    paréntesis que cierra y nunca abrió: «por analogía, soplar); el “aire”…».
    No es cosa de la traducción, viene así de origen. Se tira el jirón y se
    deja la definición, que sí está entera. Si al quitarlo no queda nada, se
    deja como estaba: mejor un renglón raro que ninguno.
    """
    if glosa.count(")") <= glosa.count("("):
        return glosa
    abiertos = 0
    corte = None
    for i, c in enumerate(glosa):
        if c == "(":
            abiertos += 1
        elif c == ")":
            if abiertos == 0:
                corte = i
            else:
                abiertos -= 1
    if corte is None:
        return glosa
    resto = glosa[corte + 1:].strip(" ;,.")
    return resto or glosa


def agrupa_sitios(sitios: list) -> list:
    """Un versículo, un renglón, aunque la palabra salga tres veces en él.

    En 1 Corintios 13:4 ἀγάπη sale tres veces, y sin esto la muestra gastaba
    tres de sus doce renglones en repetir el mismo versículo palabra por
    palabra. Se junta por versículo y se enseñan las formas que toma allí.
    """
    salida = []
    indice: dict[tuple, int] = {}
    for cid, libro, cap, vers, forma in sitios:
        forma = limpia_forma(forma)
        clave = (cid, libro, cap, vers)
        if clave in indice:
            formas = salida[indice[clave]][4]
            if forma not in formas:
                formas.append(forma)
        else:
            indice[clave] = len(salida)
            salida.append((cid, libro, cap, vers, [forma]))
    return salida


def limpia_articulo(texto: str) -> str:
    """El artículo del léxico viene con sangrías y asteriscos del original.

    Se quitan los adornos que no significan nada en una página web y se parte
    en renglones, pero no se toca el contenido: los corchetes del editor, las
    dagas y las citas se quedan como están.
    """
    texto = texto.replace("­", "")
    texto = re.sub(r"\*\*", "", texto)
    renglones = [r.strip() for r in texto.split("\n")]
    return "\n".join(r for r in renglones if r)


def pagina_palabra(strong, entrada, veces, sitios, libros, versiculos, vecinos) -> str:
    inicial = strong[0]
    lslug, lnombre, atributo, corpus = LENGUAS[inicial]
    lema = entrada.get("lema") or strong
    translit = entrada.get("translit") or ""
    glosa = repara_glosa((entrada.get("definicion_es") or "").strip())
    nombre_archivo = f"{slug(translit) or slug(lema)}-{strong.lower()}.html"
    url = f"{BASE}/{CARPETA}/{lslug}/{nombre_archivo}"

    rotulo = f"{lema} ({translit})" if translit else lema
    titulo = f"{rotulo} — qué significa en {lnombre} bíblico | {strong}"
    partes_desc = [f"{lema}, {strong}."]
    if glosa:
        partes_desc.append(glosa.rstrip(".") + ".")
    if veces:
        partes_desc.append(f"Sale {veces} {'vez' if veces == 1 else 'veces'} en el {corpus}.")
    desc = recorta(" ".join(partes_desc))

    migajas = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Palabras",
             "item": f"{BASE}/{CARPETA}/"},
            {"@type": "ListItem", "position": 2, "name": lnombre.capitalize(),
             "item": f"{BASE}/{CARPETA}/{lslug}/"},
            {"@type": "ListItem", "position": 3, "name": lema, "item": url},
        ],
    }, ensure_ascii=False, separators=(",", ":"))
    extra = f'<script type="application/ld+json">{migajas}</script>\n'

    p = [cabecera(titulo, desc, url, "../")]
    p.append(
        '<nav class="m"><a href="../../">Biblia griega y hebrea</a> › '
        f'<a href="../">Palabras</a> › <a href="./">{html.escape(lnombre.capitalize())}</a>'
        f' › {html.escape(lema)}</nav>\n'
    )
    p.append(f'<h1><span {atributo}>{html.escape(lema)}</span></h1>\n')

    sub = [translit] if translit else []
    sub.append(f"{lnombre} bíblico")
    sub.append(strong)
    p.append(f'<p class="sub">{html.escape(" · ".join(sub))}</p>\n')

    if glosa:
        p.append(f'<p class="gl">{html.escape(glosa)}</p>\n')

    # Los «usos» de Strong vienen en inglés. Se traducen con la misma regla de
    # siempre: si una sola palabra no se sabe, no se traduce nada y no se pone.
    # Antes que un renglón en inglés en una página en español, ninguno.
    usos = traducir((entrada.get("usos") or "").strip()) or ""
    origen = (entrada.get("origen") or "").strip()
    if origen:
        p.append(f'<p class="n"><b>De dónde viene:</b> {html.escape(origen)}</p>\n')

    # El artículo del léxico: es lo que de verdad hace falta que se lea.
    articulos = entrada.get("articulos") or {}
    puestos = 0
    for hom, art in sorted(articulos.items()):
        art = art or {}
        cuerpo = art.get("texto_es") or ""
        if not cuerpo.strip():
            continue
        fuente = art.get("fuente") or "el léxico"
        rotulo_art = "Qué dice el léxico"
        if len(articulos) > 1 and hom:
            rotulo_art += f" ({hom})"
        p.append(f"<h2>{html.escape(rotulo_art)}</h2>\n")
        p.append('<div class="art">\n')
        for renglon in limpia_articulo(cuerpo).split("\n"):
            p.append(f"<p>{html.escape(renglon)}</p>\n")
        p.append("</div>\n")
        p.append(f'<p class="n">De {html.escape(fuente)}, traducido al español '
                 f'para esta edición.</p>\n')
        puestos += 1

    if not puestos and usos:
        p.append("<h2>Cómo se suele traducir</h2>\n")
        p.append(f"<p>{html.escape(usos)}</p>\n")

    # Dónde sale de verdad, sacado del análisis palabra por palabra.
    if veces:
        p.append("<h2>Dónde sale</h2>\n")
        cuenta_libros: dict[tuple, int] = {}
        for cid, libro, cap, vers, forma in sitios:
            cuenta_libros[(cid, libro)] = cuenta_libros.get((cid, libro), 0) + 1

        nombres = []
        for (cid, libro), n in sorted(cuenta_libros.items(), key=lambda x: -x[1])[:8]:
            datos_libro = libros.get((cid, libro))
            if datos_libro:
                nombres.append(f"{datos_libro[1]} ({n})")
        frase = (f"Sale <b>{veces} {'vez' if veces == 1 else 'veces'}</b> en el "
                 f"{html.escape(corpus)}")
        if nombres:
            frase += ". Sobre todo en " + html.escape(", ".join(nombres))
        p.append(f"<p>{frase}.</p>\n")
        p.append('<p class="n">La cuenta es del texto que lleva análisis palabra '
                 "por palabra: el Antiguo Testamento hebreo y el Nuevo Testamento "
                 "griego. La Septuaginta, los Padres Apostólicos y los "
                 "pseudoepígrafos no están etiquetados, así que si la palabra "
                 "también sale allí, aquí no se cuenta.</p>\n")

        agrupados = agrupa_sitios(sitios)
        muestras = reparte(agrupados, MUESTRAS)
        if muestras:
            p.append('<ul class="ocur">\n')
            for cid, libro, cap, vers, formas in muestras:
                forma = " · ".join(formas)
                datos_libro = libros.get((cid, libro))
                if not datos_libro:
                    continue
                lslug_libro, lnombre_libro, cslug = datos_libro
                v = versiculos(cid, libro, cap).get(str(vers), {})
                texto = (v.get("es") or "").strip() or (v.get("t") or "").strip()
                marca = "es" if (v.get("es") or "").strip() else "o"
                ref = f"{lnombre_libro} {cap}:{vers}"
                enlace = f"../../texto/{cslug}/{lslug_libro}/{cap}.html"
                p.append("<li>")
                p.append(f'<a class="ref" href="{enlace}">{html.escape(ref)}</a> ')
                p.append(f'<span class="fm" {atributo}>{html.escape(forma)}</span>')
                if texto:
                    clase = "tx" if marca == "es" else "tx o"
                    atr = "" if marca == "es" else f" {atributo}"
                    p.append(f'<span class="{clase}"{atr}>{html.escape(texto)}</span>')
                p.append("</li>\n")
            p.append("</ul>\n")
            resto = len(agrupados) - len(muestras)
            if resto > 0:
                p.append(f'<p class="n">Y en {resto} '
                         f"{'versículo' if resto == 1 else 'versículos'} más.</p>\n")

    p.append(
        f'<a class="app" href="../../#/buscar/{strong}">'
        f"Buscar {html.escape(lema)} en el lector interactivo, con todas sus "
        "apariciones y el texto completo alrededor</a>\n"
    )

    if vecinos:
        p.append("<h2>Palabras de al lado</h2>\n<ul class=\"l\">\n")
        for otro_nombre, otro_lema, otra_glosa in vecinos:
            trozo = f" — {html.escape(otra_glosa)}" if otra_glosa else ""
            p.append(f'<li><a href="{otro_nombre}"><span {atributo}>'
                     f"{html.escape(otro_lema)}</span></a>{trozo}</li>\n")
        p.append("</ul>\n")

    p.append(
        '<footer>Diccionario de griego y hebreo bíblicos, en español. '
        '<a href="../">Todas las palabras</a> · '
        '<a href="../../texto/">El texto</a> · '
        '<a href="../../">Lector interactivo</a></footer>\n</div>\n</body>\n</html>\n'
    )
    return "".join(p)


def pagina_letra(lslug, lnombre, atributo, letra, entradas, letras) -> str:
    url = f"{BASE}/{CARPETA}/{lslug}/{slug_letra(letra)}.html"
    titulo = f"Palabras del {lnombre} bíblico por {letra} — diccionario en español"
    desc = recorta(
        f"Las {len(entradas)} palabras del {lnombre} bíblico que empiezan por "
        f"{letra}, con su significado en español, el artículo del léxico y dónde "
        "salen en el texto.")
    p = [cabecera(titulo, desc, url, "../")]
    p.append(
        '<nav class="m"><a href="../../">Biblia griega y hebrea</a> › '
        f'<a href="../">Palabras</a> › <a href="./">{html.escape(lnombre.capitalize())}</a>'
        f' › {html.escape(letra)}</nav>\n'
    )
    p.append(f'<h1>{html.escape(lnombre.capitalize())}: palabras por '
             f'<span {atributo}>{html.escape(letra)}</span></h1>\n')
    p.append(f'<p class="sub">{len(entradas)} palabras</p>\n')
    p.append(letrero(letras, lslug, letra))
    p.append('<ul class="l">\n')
    for archivo, lema, translit, glosa, veces in entradas:
        trozo = f" — {html.escape(glosa)}" if glosa else ""
        cuenta = (f' <span class="vc">{veces}×</span>' if veces else "")
        p.append(f'<li><a href="{archivo}"><span {atributo}>{html.escape(lema)}</span></a>'
                 f'{" <i>" + html.escape(translit) + "</i>" if translit else ""}'
                 f"{trozo}{cuenta}</li>\n")
    p.append("</ul>\n")
    p.append(
        '<footer>Diccionario de griego y hebreo bíblicos, en español. '
        '<a href="../">Todas las palabras</a> · <a href="../../texto/">El texto</a>'
        '</footer>\n</div>\n</body>\n</html>\n'
    )
    return "".join(p)


def slug_letra(letra: str) -> str:
    s = slug(letra)
    return s if s != "x" else f"u{ord(letra):04x}"


def letrero(letras, lslug, actual=None) -> str:
    piezas = []
    for letra in letras:
        destino = f"{slug_letra(letra)}.html"
        if letra == actual:
            piezas.append(f'<li><span class="aqui">{html.escape(letra)}</span></li>')
        else:
            piezas.append(f'<li><a href="{destino}">{html.escape(letra)}</a></li>')
    return '<ul class="g">' + "".join(piezas) + "</ul>\n"


def pagina_lengua(lslug, lnombre, atributo, letras, total, frecuentes) -> str:
    url = f"{BASE}/{CARPETA}/{lslug}/"
    titulo = f"Diccionario de {lnombre} bíblico en español — {total} palabras"
    desc = recorta(
        f"{total} palabras del {lnombre} bíblico con su significado en español, "
        "el artículo del léxico traducido y la lista de dónde sale cada una en "
        "el texto.")
    p = [cabecera(titulo, desc, url, "../")]
    p.append(
        '<nav class="m"><a href="../../">Biblia griega y hebrea</a> › '
        f'<a href="../">Palabras</a> › {html.escape(lnombre.capitalize())}</nav>\n'
    )
    p.append(f"<h1>Diccionario de {html.escape(lnombre)} bíblico</h1>\n")
    p.append(f'<p class="sub">{total} palabras, en español</p>\n')
    p.append(
        f"<p>Cada palabra tiene su página: lo que significa, de dónde viene, el "
        f"artículo del léxico traducido al español y la lista de los sitios donde "
        f"sale de verdad en el texto, con la forma que toma en cada uno.</p>\n"
    )
    p.append("<h2>Por letra</h2>\n")
    p.append(letrero(letras, lslug))
    if frecuentes:
        p.append("<h2>Las que más salen</h2>\n<ul class=\"l\">\n")
        for archivo, lema, translit, glosa, veces in frecuentes:
            trozo = f" — {html.escape(glosa)}" if glosa else ""
            p.append(f'<li><a href="{archivo}"><span {atributo}>{html.escape(lema)}'
                     f"</span></a>{trozo} <span class=\"vc\">{veces}×</span></li>\n")
        p.append("</ul>\n")
    p.append(
        '<footer>Diccionario de griego y hebreo bíblicos, en español. '
        '<a href="../">Todas las palabras</a> · <a href="../../texto/">El texto</a> · '
        '<a href="../../">Lector interactivo</a></footer>\n</div>\n</body>\n</html>\n'
    )
    return "".join(p)


def pagina_portada(totales, fuera) -> str:
    url = f"{BASE}/{CARPETA}/"
    total = sum(totales.values())
    titulo = "Diccionario de griego y hebreo bíblicos en español"
    desc = recorta(
        f"{total} palabras del griego y el hebreo de la Biblia, con su significado "
        "en español, el artículo del léxico traducido y dónde sale cada una en el "
        "texto.")
    p = [cabecera(titulo, desc, url, "")]
    p.append('<nav class="m"><a href="../">Biblia griega y hebrea</a> › Palabras</nav>\n')
    p.append("<h1>Las palabras</h1>\n")
    p.append(f'<p class="sub">{total} palabras del griego y del hebreo bíblicos, '
             "en español</p>\n")
    p.append(
        "<p>Leer la Biblia en su lengua se atasca siempre en el mismo sitio: una "
        "palabra que no se sabe qué es. Aquí cada una tiene su página, y no con "
        "una traducción suelta, sino con lo que dicen los léxicos —Abbott-Smith "
        "para el griego, Brown-Driver-Briggs para el hebreo—, traducido al "
        "español, y con la lista de los sitios donde sale de verdad en el texto.</p>\n"
    )
    p.append(
        "<p>Eso último es lo que no suele estar. Saber que <i>ἀγάπη</i> es «amor» "
        "ayuda poco; ver los ciento y pico sitios donde sale, y con qué forma en "
        "cada uno, ya es otra cosa.</p>\n"
    )
    p.append('<ul class="l">\n')
    for inicial, (lslug, lnombre, _, _) in LENGUAS.items():
        n = totales.get(inicial, 0)
        if not n:
            continue
        p.append(f'<li><a href="{lslug}/">Diccionario de {html.escape(lnombre)} '
                 f"bíblico</a> — {n} palabras</li>\n")
    p.append("</ul>\n")
    p.append(
        f'<p class="n">De las 14 197 entradas del léxico se publican las que '
        f"tienen algo que leer: artículo traducido, o definición en español y al "
        f"menos cinco apariciones en el texto. Las otras {fuera} se quedan dentro "
        "del lector, donde se consultan igual, pero no hacen página propia: una "
        "página con cuatro palabras sueltas no le sirve a nadie.</p>\n"
    )
    p.append(
        '<footer>Diccionario de griego y hebreo bíblicos, en español. '
        '<a href="../texto/">El texto</a> · '
        '<a href="../">Lector interactivo</a></footer>\n</div>\n</body>\n</html>\n'
    )
    return "".join(p)


CSS_EXTRA = """
.gl{font-size:1.15em;margin:0 0 1.2rem}
.art{border-inline-start:3px solid var(--b);padding-inline-start:.9rem;margin:0 0 .8rem}
.art p{margin:0 0 .55rem}
ul.ocur{list-style:none;padding:0;margin:0 0 1rem}
ul.ocur li{padding:.55rem 0;border-bottom:1px solid var(--b)}
.ref{font:600 14px/1.5 system-ui,sans-serif;text-decoration:none}
.fm{font-size:1.05em;margin-inline-start:.4rem}
.tx{display:block;color:var(--s);font-size:.95em;margin-top:.15rem}
.vc{color:var(--s);font:13px/1 system-ui,sans-serif}
ul.g .aqui{display:block;min-width:2.6rem;text-align:center;padding:.45rem .5rem;
 border:1px solid var(--a);border-radius:.35rem;font:15px/1 system-ui,sans-serif;color:var(--a)}
"""


def sustancia(entrada, veces) -> bool:
    """Si esta entrada da para una página que se pueda leer.

    El listón no es caprichoso: o hay artículo del léxico traducido, o hay
    definición en español y la palabra sale al menos cinco veces, que es
    cuando la lista de sitios ya enseña algo del uso.
    """
    arts = entrada.get("articulos") or {}
    if any(((a or {}).get("texto_es") or "").strip() for a in arts.values()):
        return True
    return bool((entrada.get("definicion_es") or "").strip()) and veces >= 5


def genera(destino: pathlib.Path) -> None:
    datos = destino / "datos"
    raiz = destino / CARPETA
    cuenta = {"escritos": 0, "iguales": 0}

    indice = json.loads((datos / "indice.json").read_text(encoding="utf-8"))
    libros = {}
    for coleccion in indice:
        cid = coleccion["id"]
        cslug = SLUG_COLECCION.get(cid)
        if not cslug:
            continue
        for libro in coleccion["libros"]:
            libros[(cid, libro["codigo"])] = (slug(libro["nombre"]),
                                              libro["nombre"], cslug)

    orden = {}
    for coleccion in indice:
        for i, libro in enumerate(coleccion["libros"]):
            orden[(coleccion["id"], libro["codigo"])] = i

    lexico = carga_lexico(datos)
    veces_de, sitios_de = carga_concordancia(datos, orden)
    versiculos = Versiculos(datos)

    escribe(raiz / "e.css", CSS + CSS_EXTRA, cuenta)

    # Primero se decide qué entra, y solo entonces se escribe: los enlaces a
    # las palabras de al lado tienen que apuntar a páginas que existan.
    elegidas: dict[str, list] = {"G": [], "H": []}
    fuera = 0
    for strong, entrada in lexico.items():
        inicial = strong[:1]
        if inicial not in LENGUAS:
            continue
        veces = veces_de.get(strong, 0)
        if not sustancia(entrada, veces):
            fuera += 1
            continue
        lema = entrada.get("lema") or strong
        translit = entrada.get("translit") or ""
        archivo = f"{slug(translit) or slug(lema)}-{strong.lower()}.html"
        elegidas[inicial].append(
            (archivo, strong, lema, translit,
             repara_glosa((entrada.get("definicion_es") or "").strip()), veces))

    urls_por_lengua: dict[str, list[str]] = {}
    totales: dict[str, int] = {}

    for inicial, lista in elegidas.items():
        if not lista:
            continue
        lslug, lnombre, atributo, _ = LENGUAS[inicial]
        lista.sort(key=lambda x: (x[2], x[1]))
        totales[inicial] = len(lista)
        urls = [f"{BASE}/{CARPETA}/{lslug}/"]

        por_letra: dict[str, list] = {}
        for i, (archivo, strong, lema, translit, glosa, veces) in enumerate(lista):
            letra = primera_letra(lema)
            por_letra.setdefault(letra, []).append(
                (archivo, lema, translit, glosa, veces))

            # Las palabras de al lado en el orden del diccionario: dan al lector
            # por dónde seguir y al buscador por dónde entrar a las páginas que
            # no salen en ningún índice de letra por arriba.
            vecinos = []
            for j in (i - 2, i - 1, i + 1, i + 2):
                if 0 <= j < len(lista) and j != i:
                    vecinos.append((lista[j][0], lista[j][2], lista[j][4]))

            pagina = pagina_palabra(
                strong, lexico[strong], veces, sitios_de.get(strong, []),
                libros, versiculos, vecinos)
            escribe(raiz / lslug / archivo, pagina, cuenta)
            urls.append(f"{BASE}/{CARPETA}/{lslug}/{archivo}")

        letras = sorted(por_letra)
        for letra in letras:
            escribe(raiz / lslug / f"{slug_letra(letra)}.html",
                    pagina_letra(lslug, lnombre, atributo, letra,
                                 por_letra[letra], letras), cuenta)
            urls.append(f"{BASE}/{CARPETA}/{lslug}/{slug_letra(letra)}.html")

        frecuentes = sorted(lista, key=lambda x: -x[5])[:30]
        frecuentes = [(a, le, tr, gl, vc) for a, st, le, tr, gl, vc in frecuentes]
        escribe(raiz / lslug / "index.html",
                pagina_lengua(lslug, lnombre, atributo, letras, len(lista),
                              frecuentes), cuenta)
        urls_por_lengua[lslug] = urls

    escribe(raiz / "index.html", pagina_portada(totales, fuera), cuenta)

    escribe_raras(destino, elegidas, veces_de, sitios_de, cuenta)

    todas = [f"{BASE}/{CARPETA}/"]
    for lslug, urls in urls_por_lengua.items():
        escribe(destino / "sitemaps" / f"palabras-{lslug}.xml",
                urlset(urls, "0.5"), cuenta)
    escribe(destino / "sitemaps" / "palabras.xml", urlset(todas, "0.7"), cuenta)

    total = sum(len(v) for v in urls_por_lengua.values()) + 1
    print(f"palabras publicadas: {sum(totales.values())}   fuera por flojas: {fuera}")
    print(f"URLs en el sitemap: {total}")
    print(f"archivos escritos: {cuenta['escritos']}   sin cambios: {cuenta['iguales']}")


def primera_letra(lema: str) -> str:
    for c in lema:
        if c.isalpha():
            return unicodedata.normalize("NFD", c)[0].lower() if c.isascii() else \
                mayuscula_base(c)
    return "?"


def mayuscula_base(c: str) -> str:
    """La letra sin acentos ni espíritus, para agrupar por inicial.

    El griego escribe ἀ, ἁ, ά, ᾳ… y todas son alfa. El hebreo no tiene ese
    problema, pero pasa por aquí igual sin estropearse.
    """
    base = unicodedata.normalize("NFD", c)
    base = "".join(x for x in base if not unicodedata.combining(x))
    return base.lower() or c



# Cuántas palabras raras se apuntan por capítulo. Diez caben en un vistazo;
# más ya es una lista que nadie lee.
RARAS_POR_CAPITULO = 10

# A partir de cuántas apariciones una palabra deja de ser rara. Cincuenta es
# donde empieza el vocabulario corriente: por debajo, encontrártela es motivo
# para ir a mirar qué es.
TOPE_RARA = 50


def escribe_raras(destino, elegidas, veces_de, sitios_de, cuenta) -> None:
    """Qué palabras poco corrientes tiene cada capítulo.

    Lo escribe aquí porque aquí están la concordancia y la lista de las
    palabras que sí tienen página; generar_paginas.py lo lee luego para poner
    en cada capítulo un puñado de enlaces al diccionario. Si este archivo no
    existe, aquel sigue funcionando y no pone nada: los dos programas van por
    su cuenta y da igual el orden en que se corran.

    Solo sale de los capítulos que llevan análisis palabra por palabra, que
    son el Antiguo Testamento hebreo y el Nuevo Testamento griego.
    """
    ficha = {}
    for inicial, lista in elegidas.items():
        lslug = LENGUAS[inicial][0]
        for archivo, strong, lema, translit, glosa, veces in lista:
            if veces and veces <= TOPE_RARA:
                ficha[strong] = (lslug, archivo, lema, glosa, veces)

    por_capitulo: dict[str, dict] = {}
    for strong, datos in ficha.items():
        for cid, libro, cap, vers, forma in sitios_de.get(strong, []):
            clave = f"{cid}/{libro}/{cap}"
            por_capitulo.setdefault(clave, {})[strong] = datos

    salida = {}
    for clave, palabras in por_capitulo.items():
        # De menos apariciones a más: primero lo que de verdad extraña.
        mejores = sorted(palabras.items(), key=lambda x: (x[1][4], x[1][2]))
        salida[clave] = [
            {"l": lslug, "a": archivo, "p": lema, "g": glosa, "n": veces}
            for _, (lslug, archivo, lema, glosa, veces)
            in mejores[:RARAS_POR_CAPITULO]
        ]

    escribe(destino / "datos" / "palabras-raras.json",
            json.dumps(salida, ensure_ascii=False, separators=(",", ":")), cuenta)
    print(f"capítulos con palabras raras apuntadas: {len(salida)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("uso: generar_palabras.py <carpeta biblia/>")
    genera(pathlib.Path(sys.argv[1]).resolve())
