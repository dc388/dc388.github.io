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
footer{margin-top:3rem;border-top:1px solid var(--b);padding-top:1rem;
 font:13px/1.6 system-ui,sans-serif;color:var(--s)}
"""


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
    '<a href="{raiz}index.html">Todos los libros</a></footer>\n'
    "</div>\n</body>\n</html>\n"
)


def genera(destino: pathlib.Path) -> None:
    indice = json.loads((destino / "datos" / "indice.json").read_text(encoding="utf-8"))
    propias = carga_propias()
    cuenta = {"escritos": 0, "iguales": 0}
    raiz_salida = destino / "texto"

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
                pagina_libro(libro, cslug, lslug, caps, cnombre, clengua, propia),
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

    escribe(raiz_salida / "index.html", pagina_maestra(indice, libros_por_coleccion), cuenta)
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


def pagina_capitulo(coleccion, libro, cslug, lslug, cap, caps, pos,
                    versiculos, atributo, clengua, cnombre, propia) -> str:
    nombre = libro["nombre"]
    titulo = f"{nombre} {cap} — {clengua} y español interlineal"
    url = f"{BASE}/texto/{cslug}/{lslug}/{cap}.html"
    primeros = " ".join(v.get("es", "") for v in versiculos[:3])
    desc = recorta(f"{nombre} {cap} en {clengua} y español, versículo por versículo. {primeros}")

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

    sub = f"{cnombre} · texto en {clengua} y traducción al español"
    if propia:
        sub += " · traducción hecha directamente del griego para esta edición"
    partes.append(f'<p class="sub">{html.escape(sub)}</p>\n')

    for v in versiculos:
        numero = f"{v['v']}{v.get('s', '')}"
        original = html.escape(v.get("t", ""))
        espanol = html.escape(v.get("es", ""))
        partes.append(
            f'<p class="v"><b>{numero}</b>'
            f'<span class="o" {atributo}>{original}</span>'
            f'<span class="e">{espanol}</span></p>\n'
        )

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


def pagina_libro(libro, cslug, lslug, caps, cnombre, clengua, propia) -> str:
    nombre = libro["nombre"]
    titulo = f"{nombre} — {clengua} y español, capítulo por capítulo"
    url = f"{BASE}/texto/{cslug}/{lslug}/"
    trozos = [f"{nombre} completo en {clengua} y español, los {len(caps)} capítulos."]
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
            "española de dominio público.</p>\n"
        )

    partes.append("<h2>Capítulos</h2>\n<ul class=\"g\">\n")
    for cap in caps:
        partes.append(f'<li><a href="{cap}.html">{cap}</a></li>')
    partes.append("\n</ul>\n")
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


def pagina_maestra(indice, libros_por_coleccion) -> str:
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

    filas = "".join(f"<sitemap><loc>{h}</loc></sitemap>\n" for h in hijos)
    escribe(
        destino / "sitemap.xml",
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{filas}</sitemapindex>\n",
        cuenta,
    )
    print(f"sitemaps: {len(hijos)} archivos + el índice")


if __name__ == "__main__":
    ruta = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "biblia")
    if not (ruta / "datos" / "indice.json").exists():
        sys.exit(f"no encuentro {ruta}/datos/indice.json")
    genera(ruta)
