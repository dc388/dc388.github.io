#!/usr/bin/env python3
"""Genera las páginas estáticas que sí puede leer un buscador.

La aplicación de biblia/index.html navega por almohadilla (#/lxx/1MA/4). Google
descarta todo lo que va después del #, así que para el buscador los 138 libros y
los casi cuatro mil capítulos son una sola página: la portada. Este script
escribe, al lado de la aplicación, una página HTML de verdad por cada capítulo,
con el texto original y el español dentro del HTML, enlazada y con su sitemap.

La aplicación no se toca. Estas páginas son la puerta de entrada desde el
buscador; cada una lleva un enlace al lector interactivo.

    python3 generar_paginas.py [ruta-a-biblia]

Vuelve a escribir un archivo solo si su contenido cambió, para que regenerar no
llene el historial de git de versiones idénticas.
"""

from __future__ import annotations

import html
import json
import pathlib
import re
import sys
import unicodedata

BASE = "https://dc388.github.io/biblia"

# Cómo se llama cada colección en la URL y en la página.
COLECCIONES = {
    "at":     ("hebreo",             "Antiguo Testamento hebreo", "hebreo"),
    "lxx":    ("septuaginta",        "Septuaginta",               "griego"),
    "nt":     ("nuevo-testamento",   "Nuevo Testamento griego",   "griego"),
    "padres": ("padres-apostolicos", "Padres Apostólicos",        "griego"),
    "pseudo": ("pseudoepigrafos",    "Pseudoepígrafos",           "griego"),
}

LENGUA_HTML = {"hbo": ('lang="he" dir="rtl"', "hebreo"), "grc": ('lang="grc"', "griego")}

CANON_ETIQUETA = {
    "canon": "Libro canónico",
    "deuterocanonico": "Libro deuterocanónico",
    "septuaginta": "Propio de la Septuaginta",
    "pseudoepigrafo": "Pseudoepígrafo",
    "padres": "Padres Apostólicos",
}

CSS = """\
:root{--f:#fff;--t:#17181a;--s:#5c6066;--b:#e3e5e8;--a:#0b5c9e;--o:#f4f6f8}
@media(prefers-color-scheme:dark){:root{--f:#111315;--t:#e8eaed;--s:#9aa0a6;--b:#2a2d31;--a:#7fb4e6;--o:#1a1d20}}
*{box-sizing:border-box}
body{margin:0;background:var(--f);color:var(--t);font:17px/1.65 Georgia,"Times New Roman",serif;
 -webkit-text-size-adjust:100%}
.w{max-width:44rem;margin:0 auto;padding:1.5rem 1rem 4rem}
a{color:var(--a)}
nav.m{font:14px/1.5 system-ui,sans-serif;color:var(--s);margin-bottom:1.5rem}
nav.m a{text-decoration:none}nav.m a:hover{text-decoration:underline}
h1{font-size:1.65rem;line-height:1.25;margin:.2rem 0 .35rem}
h2{font-size:1.15rem;margin:2.2rem 0 .6rem}
.sub{color:var(--s);font:14px/1.5 system-ui,sans-serif;margin:0 0 1.4rem}
.o{display:block;margin:0 0 .2rem;font-size:1.06em}
.e{display:block;margin:0}
p.v{margin:0 0 1.15rem}
p.v>b{color:var(--s);font:600 12px/1 system-ui,sans-serif;vertical-align:.35em;margin-inline-end:.35rem}
.app{display:block;background:var(--o);border:1px solid var(--b);border-radius:.5rem;
 padding:.8rem 1rem;margin:1.6rem 0;font:15px/1.5 system-ui,sans-serif;text-decoration:none}
.pn{display:flex;justify-content:space-between;gap:1rem;margin:2.5rem 0 0;
 border-top:1px solid var(--b);padding-top:1rem;font:15px/1.5 system-ui,sans-serif}
ul.g{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.4rem}
ul.g a{display:block;min-width:2.6rem;text-align:center;padding:.45rem .5rem;border:1px solid var(--b);
 border-radius:.35rem;text-decoration:none;font:15px/1 system-ui,sans-serif}
ul.l{list-style:none;padding:0;margin:0}
ul.l li{padding:.45rem 0;border-bottom:1px solid var(--b);font:16px/1.4 system-ui,sans-serif}
ul.l a{text-decoration:none}
.n{color:var(--s);font:14px/1.6 system-ui,sans-serif}
.par{border-inline-start:3px solid var(--b);padding:.15rem 0 .15rem .9rem;margin:1.6rem 0;
 color:var(--s);font:15px/1.6 system-ui,sans-serif}
.nt p{margin:0 0 1rem}
.nt{font-size:.97em}
ul.c{margin:0 0 1rem;padding-left:1.2rem}
ul.c li{margin:0 0 .5rem}
h3{font-size:1.05rem;margin:1.6rem 0 .2rem}
footer{margin-top:3rem;border-top:1px solid var(--b);padding-top:1rem;
 font:13px/1.6 system-ui,sans-serif;color:var(--s)}
"""


# Libro de la Septuaginta -> (slug, nombre, capítulos) del mismo libro en el
# Antiguo Testamento hebreo. Se llena en genera() leyendo el índice, porque los
# códigos de libro son los mismos en las dos colecciones cuando el libro es el
# mismo. Sirve para mandar al lector adonde sí hay español.
PARALELO_HEBREO: dict[str, tuple[str, str, list]] = {}

# Las palabras poco corrientes de cada capítulo, que escribe generar_palabras.py
# junto con las páginas del diccionario. Si no está, no se pone nada: los dos
# programas van por su cuenta y da igual en qué orden se corran.
RARAS: dict[str, list] = {}

# Libros donde la Septuaginta y el texto hebreo no numeran igual. En los Salmos
# la Septuaginta junta el 9 y el 10 y a partir de ahí va una unidad por detrás;
# en Jeremías el orden de los oráculos contra las naciones es otro. Se avisa en
# vez de callarlo, porque el enlace puede caer en un capítulo que no es.
NUMERACION_DISTINTA = {"SAL", "JER"}


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def recorta(s: str, n: int = 155) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n:
        return s
    return s[: s.rfind(" ", 0, n - 1)].rstrip(" ,;:.—-") + "…"


def escribe(ruta: pathlib.Path, texto: str, cuenta: dict) -> None:
    """Escribe solo si cambió, para no ensuciar el historial de git."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if ruta.exists() and ruta.read_text(encoding="utf-8") == texto:
        cuenta["iguales"] += 1
        return
    ruta.write_text(texto, encoding="utf-8")
    cuenta["escritos"] += 1


def cabecera(titulo: str, desc: str, url: str, raiz: str, extra: str = "") -> str:
    return (
        "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
        f"<title>{html.escape(titulo)}</title>\n"
        f"<meta name=\"description\" content=\"{html.escape(desc)}\">\n"
        f"<link rel=\"canonical\" href=\"{url}\">\n"
        "<meta name=\"robots\" content=\"index,follow\">\n"
        "<meta property=\"og:type\" content=\"article\">\n"
        f"<meta property=\"og:title\" content=\"{html.escape(titulo)}\">\n"
        f"<meta property=\"og:description\" content=\"{html.escape(desc)}\">\n"
        f"<meta property=\"og:url\" content=\"{url}\">\n"
        f"<link rel=\"stylesheet\" href=\"{raiz}e.css\">\n"
        f"{extra}</head>\n<body>\n<div class=\"w\">\n"
    )


def migas(raiz: str, piezas: list[tuple[str, str | None]]) -> str:
    salida = [f'<a href="{raiz}../">Biblia griega y hebrea</a>']
    for texto, destino in piezas:
        salida.append(
            f'<a href="{destino}">{html.escape(texto)}</a>' if destino else html.escape(texto)
        )
    return '<nav class="m">' + " › ".join(salida) + "</nav>\n"


PIE = (
    '<footer>Texto original y traducción al español. '
    '<a href="{raiz}../">Lector interactivo</a> · '
    '<a href="{raiz}index.html">Todos los libros</a> · '
    '<a href="{raiz}../palabras/">Las palabras</a></footer>\n'
    "</div>\n</body>\n</html>\n"
)


def genera(destino: pathlib.Path) -> None:
    indice = json.loads((destino / "datos" / "indice.json").read_text(encoding="utf-8"))
    propias = carga_propias()
    comentarios = carga_comentarios()
    cuenta = {"escritos": 0, "iguales": 0}
    raiz_salida = destino / "texto"

    RARAS.clear()
    ficha_raras = destino / "datos" / "palabras-raras.json"
    if ficha_raras.exists():
        RARAS.update(json.loads(ficha_raras.read_text(encoding="utf-8")))

    PARALELO_HEBREO.clear()
    for coleccion in indice:
        if coleccion["id"] != "at":
            continue
        for libro in coleccion["libros"]:
            PARALELO_HEBREO[libro["codigo"]] = (
                slug(libro["nombre"]), libro["nombre"], libro["capitulos"])

    escribe(raiz_salida / "e.css", CSS, cuenta)

    urls_indices: list[str] = [f"{BASE}/texto/"]
    urls_por_coleccion: dict[str, list[str]] = {}
    libros_por_coleccion: dict[str, list[tuple]] = {}
    total_caps = 0

    for coleccion in indice:
        cid = coleccion["id"]
        if cid not in COLECCIONES:
            continue
        cslug, cnombre, clengua = COLECCIONES[cid]
        atributo, _ = LENGUA_HTML.get(coleccion["lengua"], ('lang="grc"', "griego"))
        urls = []
        libros = []

        for libro in coleccion["libros"]:
            lslug = slug(libro["nombre"])
            caps = libro["capitulos"]
            propia = (cid, libro["codigo"]) in propias
            libros.append((lslug, libro, propia))
            urls_indices.append(f"{BASE}/texto/{cslug}/{lslug}/")

            for pos, cap in enumerate(caps):
                ruta_json = destino / "datos" / cid / libro["codigo"] / f"{cap}.json"
                if not ruta_json.exists():
                    continue
                versiculos = json.loads(ruta_json.read_text(encoding="utf-8"))
                pagina = pagina_capitulo(
                    coleccion, libro, cslug, lslug, cap, caps, pos,
                    versiculos, atributo, clengua, cnombre, propia,
                )
                escribe(raiz_salida / cslug / lslug / f"{cap}.html", pagina, cuenta)
                urls.append(f"{BASE}/texto/{cslug}/{lslug}/{cap}.html")
                total_caps += 1

            escribe(
                raiz_salida / cslug / lslug / "index.html",
                pagina_libro(libro, cslug, lslug, caps, cnombre, clengua, propia,
                             comentarios.get((cid, libro["codigo"]), []),
                             primeros_versiculos(destino, cid, libro, caps, atributo)),
                cuenta,
            )

        escribe(
            raiz_salida / cslug / "index.html",
            pagina_coleccion(coleccion, cslug, cnombre, clengua, libros),
            cuenta,
        )
        urls_indices.append(f"{BASE}/texto/{cslug}/")
        urls_por_coleccion[cslug] = urls
        libros_por_coleccion[cslug] = libros

    versiculos_propios = sum(
        libro.get("versiculos", 0)
        for coleccion in indice
        if coleccion["id"] in COLECCIONES
        for libro in coleccion["libros"]
        if (coleccion["id"], libro["codigo"]) in propias
    )
    escribe(
        raiz_salida / "traducciones-propias.html",
        pagina_propias(indice, comentarios, libros_por_coleccion, versiculos_propios),
        cuenta,
    )
    urls_indices.insert(1, f"{BASE}/texto/traducciones-propias.html")

    escribe(raiz_salida / "index.html",
            pagina_maestra(indice, libros_por_coleccion, versiculos_propios), cuenta)
    escribe_sitemaps(destino, urls_indices, urls_por_coleccion)

    total_urls = len(urls_indices) + sum(len(v) for v in urls_por_coleccion.values())
    print(f"capítulos: {total_caps}   URLs en el sitemap: {total_urls}")
    print(f"archivos escritos: {cuenta['escritos']}   sin cambios: {cuenta['iguales']}")


def carga_propias() -> set[tuple[str, str]]:
    """Qué libros llevan traducción hecha a mano desde el griego."""
    registro = pathlib.Path(__file__).with_name("traducciones_propias.py")
    if not registro.exists():
        return set()
    texto = registro.read_text(encoding="utf-8")
    return {
        (c, l) for c, l in re.findall(r'\(\s*"(\w+)"\s*,\s*"(\w+)"\s*\)\s*:', texto)
    }


def carga_comentarios() -> dict[tuple[str, str], list]:
    """Saca a la luz las notas del traductor.

    Cada módulo de traducción abre con una cabecera que explica qué es el libro,
    por qué importa y qué defectos tiene la edición griega de la que se tradujo.
    Son varios miles de palabras escritas a mano que hasta ahora solo se leían
    abriendo el código. Aquí se recogen para ponerlas en la página del libro,
    que es donde sirven de algo: es lo único de este sitio que no está en
    ninguna otra parte.

    Devuelve, por libro, una lista de bloques ("p", texto) o ("ul", [puntos]).
    """
    carpeta = pathlib.Path(__file__).parent
    registro = carpeta / "traducciones_propias.py"
    if not registro.exists():
        return {}
    texto = registro.read_text(encoding="utf-8")

    # from judit_es import JUDIT_ES        ->  JUDIT_ES pertenece a judit_es
    modulo_de = {}
    for modulo, constantes in re.findall(r"^from (\w+) import (.+)$", texto, re.M):
        for c in constantes.split(","):
            modulo_de[c.strip()] = modulo

    # ("lxx", "JDT"): _con_sufijo(JUDIT_ES)  ->  ese libro usa ese módulo
    comentarios = {}
    cache = {}
    for col, cod, const in re.findall(
        r'\(\s*"(\w+)"\s*,\s*"(\w+)"\s*\)\s*:[^(]*\((\w+)\)', texto
    ):
        modulo = modulo_de.get(const)
        if not modulo:
            continue
        if modulo not in cache:
            archivo = carpeta / f"{modulo}.py"
            cabecera = ""
            if archivo.exists():
                m = re.match(r'\s*"""(.*?)"""', archivo.read_text(encoding="utf-8"), re.S)
                cabecera = m.group(1) if m else ""
            cache[modulo] = bloques(cabecera)
        if cache[modulo]:
            comentarios[(col, cod)] = cache[modulo]

    # Los 104 libros que no tienen traducción propia y por tanto no tienen
    # cabecera que sacar: su introducción se escribió aparte. Sin esto, su
    # página son cuarenta palabras de navegación y nada que leer.
    try:
        from introducciones import INTRODUCCIONES
    except ImportError:
        return comentarios
    for clave, texto in INTRODUCCIONES.items():
        comentarios.setdefault(clave, bloques(texto))
    return comentarios


def bloques(cabecera: str) -> list:
    """Convierte el texto plano de una cabecera en párrafos y listas."""
    salida = []
    for trozo in re.split(r"\n\s*\n", cabecera.strip()):
        lineas = [l.rstrip() for l in trozo.splitlines() if l.strip()]
        if not lineas:
            continue
        if lineas[0].lstrip().startswith("- "):
            puntos = []
            for linea in lineas:
                if linea.lstrip().startswith("- "):
                    puntos.append(linea.lstrip()[2:].strip())
                elif puntos:
                    puntos[-1] += " " + linea.strip()
            salida.append(("ul", puntos))
        else:
            salida.append(("p", " ".join(l.strip() for l in lineas)))
    return salida


def pinta_bloques(bs: list) -> str:
    partes = []
    for tipo, cuerpo in bs:
        if tipo == "p":
            partes.append(f"<p>{html.escape(cuerpo)}</p>\n")
        else:
            puntos = "".join(f"<li>{html.escape(x)}</li>" for x in cuerpo)
            partes.append(f'<ul class="c">{puntos}</ul>\n')
    return "".join(partes)


def pagina_capitulo(coleccion, libro, cslug, lslug, cap, caps, pos,
                    versiculos, atributo, clengua, cnombre, propia) -> str:
    nombre = libro["nombre"]
    url = f"{BASE}/texto/{cslug}/{lslug}/{cap}.html"

    # Casi mil capítulos de la Septuaginta todavía no tienen traducción propia:
    # son los que también están en el canon hebreo, donde el español ya se lee
    # en la otra colección. Esas páginas decían en el título «griego y español
    # interlineal» y abajo solo había griego. Prometer lo que no se da es lo
    # peor que se puede hacer con un buscador y con un lector, así que el
    # título dice lo que hay: texto en griego, y nada más.
    hay_es = any((v.get("es") or "").strip() for v in versiculos)
    if hay_es:
        titulo = f"{nombre} {cap} — {clengua} y español interlineal"
        primeros = " ".join(v.get("es", "") for v in versiculos[:3])
        desc = recorta(
            f"{nombre} {cap} en {clengua} y español, versículo por versículo. {primeros}")
    else:
        titulo = f"{nombre} {cap} — texto en {clengua}"
        primeros = " ".join(v.get("t", "") for v in versiculos[:2])
        desc = recorta(
            f"{nombre} {cap} en {clengua}, versículo por versículo, con análisis "
            f"palabra por palabra en el lector. {primeros}")

    anterior = caps[pos - 1] if pos > 0 else None
    siguiente = caps[pos + 1] if pos + 1 < len(caps) else None
    enlaces = ""
    if anterior is not None:
        enlaces += f'<link rel="prev" href="{BASE}/texto/{cslug}/{lslug}/{anterior}.html">\n'
    if siguiente is not None:
        enlaces += f'<link rel="next" href="{BASE}/texto/{cslug}/{lslug}/{siguiente}.html">\n'

    migajas = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": cnombre,
             "item": f"{BASE}/texto/{cslug}/"},
            {"@type": "ListItem", "position": 2, "name": nombre,
             "item": f"{BASE}/texto/{cslug}/{lslug}/"},
            {"@type": "ListItem", "position": 3, "name": f"{nombre} {cap}", "item": url},
        ],
    }, ensure_ascii=False, separators=(",", ":"))
    enlaces += f'<script type="application/ld+json">{migajas}</script>\n'

    partes = [cabecera(titulo, desc, url, "../../", enlaces)]
    partes.append(migas("../../", [(cnombre, "../"), (nombre, "./"), (str(cap), None)]))
    partes.append(f"<h1>{html.escape(nombre)} {cap}</h1>\n")

    if hay_es:
        sub = f"{cnombre} · texto en {clengua} y traducción al español"
        if propia:
            sub += " · traducción hecha directamente del griego para esta edición"
    else:
        sub = f"{cnombre} · texto en {clengua}"
    partes.append(f'<p class="sub">{html.escape(sub)}</p>\n')

    # Sin español aquí, pero el mismo libro está en el Antiguo Testamento
    # hebreo y allí sí lo hay: se dice y se enlaza, que para eso está.
    paralelo = None if hay_es else PARALELO_HEBREO.get(libro["codigo"])
    if paralelo:
        pslug, pnombre, pcaps = paralelo
        destino_cap = cap if cap in pcaps else None
        aviso = ""
        if libro["codigo"] in NUMERACION_DISTINTA:
            aviso = (" La Septuaginta y el hebreo no numeran igual los capítulos, "
                     "así que puede no caer en el mismo sitio.")
        if destino_cap is not None:
            partes.append(
                f'<p class="par">Este capítulo todavía no tiene traducción propia al '
                f'español. El mismo libro está en el Antiguo Testamento hebreo, y allí '
                f'sí: <a href="../../hebreo/{pslug}/{destino_cap}.html">'
                f'{html.escape(pnombre)} {destino_cap} en hebreo y español</a>.{aviso}</p>\n'
            )
        else:
            partes.append(
                f'<p class="par">Este capítulo todavía no tiene traducción propia al '
                f'español. El mismo libro está en el Antiguo Testamento hebreo, y allí '
                f'sí: <a href="../../hebreo/{pslug}/">'
                f'{html.escape(pnombre)} en hebreo y español</a>.{aviso}</p>\n'
            )

    for v in versiculos:
        numero = f"{v['v']}{v.get('s', '')}"
        original = html.escape(v.get("t", ""))
        espanol = html.escape(v.get("es", ""))
        partes.append(
            f'<p class="v"><b>{numero}</b>'
            f'<span class="o" {atributo}>{original}</span>'
            f'<span class="e">{espanol}</span></p>\n'
        )

    raras = RARAS.get(f'{coleccion["id"]}/{libro["codigo"]}/{cap}') or []
    if raras:
        partes.append("<h2>Palabras poco corrientes de este capítulo</h2>\n")
        partes.append(
            '<p class="n">De las que salen pocas veces en toda la Biblia. '
            "Encontrarse una es motivo para ir a mirar qué es.</p>\n"
        )
        partes.append('<ul class="l">\n')
        for r in raras:
            veces = r["n"]
            cuantas = "solo aquí" if veces == 1 else f"{veces} veces en total"
            glosa = f' — {html.escape(r["g"])}' if r.get("g") else ""
            partes.append(
                f'<li><a href="../../../palabras/{r["l"]}/{r["a"]}">'
                f'<span {atributo}>{html.escape(r["p"])}</span></a>{glosa} '
                f'<span class="n">({cuantas})</span></li>\n'
            )
        partes.append("</ul>\n")

    partes.append(
        f'<a class="app" href="../../../#/{coleccion["id"]}/{libro["codigo"]}/{cap}">'
        f"Abrir {html.escape(nombre)} {cap} en el lector interactivo, con el análisis "
        "palabra por palabra y el diccionario</a>\n"
    )

    izquierda = (
        f'<a href="{anterior}.html">‹ {html.escape(nombre)} {anterior}</a>'
        if anterior is not None else "<span></span>"
    )
    derecha = (
        f'<a href="{siguiente}.html">{html.escape(nombre)} {siguiente} ›</a>'
        if siguiente is not None else "<span></span>"
    )
    partes.append(f'<nav class="pn">{izquierda}{derecha}</nav>\n')
    partes.append(PIE.format(raiz="../../"))
    return "".join(partes)


class Muestra(list):
    """Los primeros versículos de un libro, con el atributo de lengua a cuestas.

    Se lleva el atributo pegado porque el hebreo hay que marcarlo de derecha a
    izquierda y la página de libro no tiene de dónde sacarlo si no.
    """

    def __init__(self, versiculos, atributo):
        super().__init__(versiculos)
        self.atributo = atributo


def primeros_versiculos(destino, cid, libro, caps, atributo, cuantos=3):
    """Una muestra del texto, para que se vea qué hay antes de entrar.

    La página de libro era hasta ahora una rejilla de números: no enseñaba ni
    una línea de lo que el lector viene a leer. Tres versículos bastan para
    saber si es esto lo que buscaba.
    """
    if not caps:
        return Muestra([], atributo)
    ruta = destino / "datos" / cid / libro["codigo"] / f"{caps[0]}.json"
    if not ruta.exists():
        return Muestra([], atributo)
    return Muestra(
        json.loads(ruta.read_text(encoding="utf-8"))[:cuantos], atributo
    )


def pagina_libro(libro, cslug, lslug, caps, cnombre, clengua, propia, comentario,
                 muestra=()) -> str:
    nombre = libro["nombre"]
    url = f"{BASE}/texto/{cslug}/{lslug}/"

    # Lo mismo que en la página de capítulo: si el libro no lleva español, el
    # título no lo promete. Se mira la muestra, que sale del primer capítulo.
    hay_es = any((v.get("es") or "").strip() for v in muestra)
    if hay_es:
        titulo = f"{nombre} — {clengua} y español, capítulo por capítulo"
        trozos = [f"{nombre} completo en {clengua} y español, los {len(caps)} capítulos."]
    else:
        titulo = f"{nombre} — texto en {clengua}, capítulo por capítulo"
        trozos = [f"{nombre} completo en {clengua}, los {len(caps)} capítulos, "
                  f"con análisis palabra por palabra en el lector."]
    if libro.get("nota"):
        trozos.append(libro["nota"])
    desc = recorta(" ".join(trozos))

    partes = [cabecera(titulo, desc, url, "../../")]
    partes.append(migas("../../", [(cnombre, "../"), (nombre, None)]))
    partes.append(f"<h1>{html.escape(nombre)}</h1>\n")

    sub = [cnombre]
    if libro.get("original"):
        sub.append(libro["original"])
    if libro.get("alterno"):
        sub.append(libro["alterno"])
    sub.append(CANON_ETIQUETA.get(libro.get("canon", ""), ""))
    sub.append(f"{len(caps)} capítulos, {libro.get('versiculos', '?')} versículos")
    partes.append('<p class="sub">' + html.escape(" · ".join(x for x in sub if x)) + "</p>\n")

    if libro.get("nota"):
        partes.append(f'<p class="n">{html.escape(libro["nota"])}</p>\n')
    if propia:
        partes.append(
            '<p class="n">La traducción española de este libro se hizo directamente '
            "del griego para esta edición, porque no existe en ninguna Biblia "
            'española de dominio público. <a href="../../traducciones-propias.html">'
            "Los demás libros traducidos así</a>.</p>\n"
        )

    partes.append("<h2>Capítulos</h2>\n<ul class=\"g\">\n")
    for cap in caps:
        partes.append(f'<li><a href="{cap}.html">{cap}</a></li>')
    partes.append("\n</ul>\n")

    paralelo = None if hay_es else PARALELO_HEBREO.get(libro["codigo"])
    if paralelo and cslug != "hebreo":
        pslug, pnombre, _ = paralelo
        partes.append(
            f'<p class="par">Este libro todavía no tiene traducción propia al español. '
            f'El mismo libro está en el Antiguo Testamento hebreo, y allí sí: '
            f'<a href="../../hebreo/{pslug}/">{html.escape(pnombre)} en hebreo y '
            f'español</a>.</p>\n'
        )

    if muestra:
        primero = caps[0]
        partes.append(f"<h2>Así empieza</h2>\n")
        for v in muestra:
            numero = f"{v['v']}{v.get('s', '')}"
            partes.append(
                f'<p class="v"><b>{numero}</b>'
                f'<span class="o" {muestra.atributo}>{html.escape(v.get("t", ""))}</span>'
                f'<span class="e">{html.escape(v.get("es", ""))}</span></p>\n'
            )
        partes.append(
            f'<p class="n"><a href="{primero}.html">Seguir leyendo '
            f'{html.escape(libro["nombre"])} {primero}</a></p>\n'
        )

    if comentario:
        partes.append(
            "<h2>Sobre este libro"
            f"{' y sobre esta traducción' if propia else ''}</h2>\n"
        )
        partes.append('<div class="nt">\n')
        partes.append(pinta_bloques(comentario))
        partes.append("</div>\n")

    partes.append(PIE.format(raiz="../../"))
    return "".join(partes)


def pagina_coleccion(coleccion, cslug, cnombre, clengua, libros) -> str:
    titulo = f"{cnombre} en {clengua} y español — índice de libros"
    url = f"{BASE}/texto/{cslug}/"
    desc = recorta(
        f"Los {len(libros)} libros de {cnombre} en {clengua} con traducción al "
        f"español, versículo por versículo. Edición: {coleccion.get('edicion', '')}"
    )
    partes = [cabecera(titulo, desc, url, "../")]
    partes.append(migas("../", [(cnombre, None)]))
    partes.append(f"<h1>{html.escape(cnombre)}</h1>\n")
    partes.append(
        f'<p class="sub">{html.escape(str(coleccion.get("edicion", "")))} · '
        f"{len(libros)} libros</p>\n"
    )
    partes.append('<ul class="l">\n')
    for lslug, libro, propia in libros:
        marca = " · traducción propia del griego" if propia else ""
        partes.append(
            f'<li><a href="{lslug}/">{html.escape(libro["nombre"])}</a> '
            f'<span class="n">{len(libro["capitulos"])} cap.{html.escape(marca)}</span></li>\n'
        )
    partes.append("</ul>\n")
    partes.append(PIE.format(raiz="../"))
    return "".join(partes)


def pagina_maestra(indice, libros_por_coleccion, versiculos_propios=0) -> str:
    total = sum(len(v) for v in libros_por_coleccion.values())
    titulo = "Biblia en griego, hebreo y español — todos los libros, capítulo por capítulo"
    url = f"{BASE}/texto/"
    desc = recorta(
        f"Los {total} libros de la Biblia griega y hebrea con traducción al español: "
        "Septuaginta, Nuevo Testamento griego, Antiguo Testamento hebreo, "
        "Padres Apostólicos y pseudoepígrafos."
    )
    partes = [cabecera(titulo, desc, url, "")]
    partes.append('<nav class="m"><a href="../">Biblia griega y hebrea</a> › Todos los libros</nav>\n')
    partes.append("<h1>Todos los libros</h1>\n")
    partes.append(
        f'<p class="sub">{total} libros en griego, hebreo y español, '
        "capítulo por capítulo.</p>\n"
    )
    partes.append(
        '<a class="app" href="traducciones-propias.html">'
        f"Los libros que no encontrarás en otra Biblia española: {versiculos_propios} "
        "versículos traducidos del griego a mano para esta edición, porque ninguna "
        "Biblia española de dominio público los trae</a>\n"
    )
    partes.append(
        '<a class="app" href="../palabras/">'
        "El diccionario: cada palabra del griego y del hebreo bíblicos con su "
        "significado en español, el artículo del léxico traducido y la lista de "
        "dónde sale de verdad en el texto</a>\n"
    )
    for coleccion in indice:
        cid = coleccion["id"]
        if cid not in COLECCIONES:
            continue
        cslug, cnombre, _ = COLECCIONES[cid]
        libros = libros_por_coleccion.get(cslug, [])
        partes.append(f'<h2><a href="{cslug}/">{html.escape(cnombre)}</a></h2>\n')
        partes.append('<ul class="l">\n')
        for lslug, libro, propia in libros:
            marca = " · traducción propia del griego" if propia else ""
            partes.append(
                f'<li><a href="{cslug}/{lslug}/">{html.escape(libro["nombre"])}</a> '
                f'<span class="n">{len(libro["capitulos"])} cap.'
                f"{html.escape(marca)}</span></li>\n"
            )
        partes.append("</ul>\n")
    partes.append(PIE.format(raiz=""))
    return "".join(partes)


DESCARGO = "Para las Asambleas de Dios no es canon; se ofrece para estudio."


def entradilla(comentario: list) -> str:
    """El primer párrafo que dice algo del libro, sin la advertencia de canon.

    Todas las cabeceras abren igual —el título y el descargo sobre el canon—, y
    repetir eso en las treinta y tres entradas del índice se lee fatal y parece
    una plantilla. Aquí se salta hasta lo que de verdad distingue al libro.
    """
    for tipo, cuerpo in comentario[1:]:
        if tipo != "p":
            continue
        texto = cuerpo.strip()
        if texto.startswith(DESCARGO):
            texto = texto[len(DESCARGO):].strip()
        if len(texto) > 40:
            return texto
    return ""


def pagina_propias(indice, comentarios, libros_por_coleccion, versiculos_propios) -> str:
    """La página que sostiene todo lo demás.

    Es lo único que este sitio tiene y los grandes no: los libros que ninguna
    Biblia española gratuita trae, traducidos del griego uno por uno. Si alguien
    va a llegar aquí desde un buscador, será por esto.
    """
    slug_col = {c["id"]: COLECCIONES[c["id"]][0] for c in indice if c["id"] in COLECCIONES}
    filas = []
    for coleccion in indice:
        cid = coleccion["id"]
        if cid not in COLECCIONES:
            continue
        cslug, cnombre, _ = COLECCIONES[cid]
        for lslug, libro, propia in libros_por_coleccion.get(cslug, []):
            if propia:
                filas.append((cslug, cnombre, lslug, libro, comentarios.get((cid, libro["codigo"]), [])))

    titulo = ("Libros que no están en ninguna otra Biblia española gratis — "
              "traducidos del griego")
    url = f"{BASE}/texto/traducciones-propias.html"
    desc = recorta(
        f"{len(filas)} libros griegos traducidos al español a mano para esta edición: "
        "Tobías, Judit, Sabiduría, Eclesiástico, los cuatro Macabeos, el Libro de Enoc, "
        "las Odas, los Salmos de Salomón y los Padres Apostólicos. "
        "Ninguna Biblia española de dominio público los trae."
    )

    partes = [cabecera(titulo, desc, url, "")]
    partes.append('<nav class="m"><a href="../">Biblia griega y hebrea</a> › '
                  '<a href="index.html">Todos los libros</a> › Traducciones propias</nav>\n')
    partes.append("<h1>Los libros que no encontrarás en otra Biblia española</h1>\n")
    partes.append(
        f'<p class="sub">{len(filas)} libros · {versiculos_propios} versículos '
        "traducidos del griego a mano para esta edición</p>\n"
    )
    partes.append(
        "<p>La Reina-Valera cubre los 66 libros del canon protestante y nada más. "
        "Lo comprobé contra las cuatro Biblias que existen en español en dominio "
        "público —Reina-Valera 1909, Biblia en Español Sencillo, Palabra de Dios "
        "para Ti y Versión Biblia Libre—: las cuatro traen los mismos 66 libros y "
        "ninguno más. Así que los apócrifos, los pseudoepígrafos y los Padres "
        "Apostólicos no tenían traducción española libre que copiar.</p>\n"
    )
    partes.append(
        "<p>Están traducidos aquí, del griego que se ve al lado y no de una "
        "traducción inglesa intermedia. Las lagunas del manuscrito van marcadas "
        "con […] en vez de coserlas en silencio, los corchetes del editor griego "
        "se conservan, y los defectos de cada edición —versículos mal numerados, "
        "transposiciones, epígrafes desplazados— se explican en la página de cada "
        "libro en vez de corregirlos a escondidas.</p>\n"
    )

    coleccion_actual = None
    for cslug, cnombre, lslug, libro, comentario in filas:
        if cnombre != coleccion_actual:
            partes.append(f'<h2>{html.escape(cnombre)}</h2>\n')
            coleccion_actual = cnombre
        entrada = entradilla(comentario)
        partes.append(
            f'<h3><a href="{cslug}/{lslug}/">{html.escape(libro["nombre"])}</a></h3>\n'
        )
        meta = [f'{len(libro["capitulos"])} capítulos',
                f'{libro.get("versiculos", "?")} versículos']
        if libro.get("original"):
            meta.insert(0, libro["original"])
        partes.append(f'<p class="n">{html.escape(" · ".join(meta))}</p>\n')
        if entrada:
            partes.append(f"<p>{html.escape(recorta(entrada, 420))}</p>\n")

    partes.append(PIE.format(raiz=""))
    return "".join(partes)


def urlset(urls: list[str], prioridad: str) -> str:
    filas = "".join(
        f"<url><loc>{u}</loc><changefreq>monthly</changefreq>"
        f"<priority>{prioridad}</priority></url>\n"
        for u in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{filas}</urlset>\n"
    )


def escribe_sitemaps(destino: pathlib.Path, urls_indices, urls_por_coleccion) -> None:
    cuenta = {"escritos": 0, "iguales": 0}
    carpeta = destino / "sitemaps"
    hijos = []

    escribe(carpeta / "indices.xml", urlset([f"{BASE}/"] + urls_indices, "0.9"), cuenta)
    hijos.append(f"{BASE}/sitemaps/indices.xml")

    for cslug, urls in urls_por_coleccion.items():
        if not urls:
            continue
        escribe(carpeta / f"{cslug}.xml", urlset(urls, "0.7"), cuenta)
        hijos.append(f"{BASE}/sitemaps/{cslug}.xml")

    # Las páginas de palabra las escribe generar_palabras.py, que va por su
    # cuenta. Se recogen aquí si están, para que el índice de sitemaps no
    # dependa de en qué orden se hayan corrido los dos programas.
    for suelto in sorted(carpeta.glob("palabras*.xml")):
        hijos.append(f"{BASE}/sitemaps/{suelto.name}")

    escribe(destino / "sitemap.xml", indice_sitemaps(hijos), cuenta)

    # Y el de la raíz del dominio, que es el que lee Google.
    #
    # Aquí estaba el fallo que dejaba Search Console en «No se ha podido
    # obtener» con cero páginas: /sitemap.xml era un índice que apuntaba a
    # /biblia/sitemap.xml, y ese también era un índice. El protocolo de
    # sitemaps no deja meter un índice dentro de otro —un índice solo puede
    # listar listas de páginas—, así que el de arriba no llevaba a ninguna
    # URL y Google no encontraba nada que rastrear.
    #
    # Ahora el de la raíz lista directamente las listas de páginas. El de
    # /biblia/ se queda porque por sí solo es válido y puede haber quien lo
    # tenga guardado, pero ya no cuelga de ningún otro índice.
    raiz_dominio = destino.parent
    sueltos = []
    for otro in sorted(raiz_dominio.glob("sitemap-*.xml")):
        sueltos.append(f"{BASE.rsplit('/', 1)[0]}/{otro.name}")
    escribe(raiz_dominio / "sitemap.xml", indice_sitemaps(hijos + sueltos), cuenta)

    print(f"sitemaps: {len(hijos)} archivos + {len(sueltos)} del resto del sitio "
          f"+ los dos índices")


def indice_sitemaps(hijos: list[str]) -> str:
    filas = "".join(f"<sitemap><loc>{h}</loc></sitemap>\n" for h in hijos)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{filas}</sitemapindex>\n"
    )


if __name__ == "__main__":
    ruta = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "biblia")
    if not (ruta / "datos" / "indice.json").exists():
        sys.exit(f"no encuentro {ruta}/datos/indice.json")
    genera(ruta)
