"""Lector de los textos griegos en TEI de First1KGreek.

La codificación es siempre la misma: una edición con divisiones de capítulo y
de sección, notas del editor intercaladas que no son texto, y a veces varias
obras en un solo archivo. Lo comparten los importadores que sacan textos de ahí.
"""

from __future__ import annotations

import re
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

TEI = "{http://www.tei-c.org/ns/1.0}"

BASE = "https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/master/data"


def url(archivo: str) -> str:
    autor, obra = archivo.split(".")[:2]
    return f"{BASE}/{autor}/{obra}/{archivo}"


def descargar(destino: Path, archivos: list[str]) -> None:
    """Trae los archivos sueltos. No clona el repositorio: pesa de más."""
    destino.mkdir(parents=True, exist_ok=True)
    for archivo in dict.fromkeys(archivos):
        ruta = destino / archivo
        if ruta.exists():
            continue
        print(f"  bajando {archivo}")
        with urllib.request.urlopen(url(archivo), timeout=60) as r:
            ruta.write_bytes(r.read())


def _texto(nodo: ET.Element) -> str:
    """Todo el texto del nodo menos las notas al pie, que son del editor."""
    partes: list[str] = []
    if nodo.text:
        partes.append(nodo.text)
    for hijo in nodo:
        if hijo.tag == TEI + "note":
            # La nota no se lee, pero lo que va detrás de ella sí: la referencia
            # bíblica se intercala a media frase y el resto del versículo viene
            # en la cola.
            if hijo.tail:
                partes.append(hijo.tail)
            continue
        partes.append(_texto(hijo))
        if hijo.tail:
            partes.append(hijo.tail)
    return "".join(partes)


def es_griego(texto: str, minimo: float = 0.6) -> bool:
    """Cierto si el párrafo está escrito en griego.

    Hace falta porque algunas ediciones imprimen el original junto a la
    traducción del editor —la de Flemming para Enoc trae el alemán— y el TEI no
    marca cuál es cuál. Separa bien: en ese archivo el 98 % de los párrafos son
    de una escritura o de la otra, sin término medio.
    """
    letras = [c for c in texto if c.isalpha()]
    if not letras:
        return False
    griegas = sum(1 for c in letras if "GREEK" in unicodedata.name(c, ""))
    return griegas / len(letras) >= minimo


def _parrafos(nodo: ET.Element, solo_griego: bool) -> list[str]:
    textos = [_texto(p) for p in nodo.iter(TEI + "p")]
    return [t for t in textos if not solo_griego or es_griego(t)]


def _numero(nodo: ET.Element) -> int | None:
    n = (nodo.get("n") or "").strip()
    m = re.match(r"\d+", n)
    return int(m.group()) if m else None


def leer(
    ruta: Path,
    parte: int | None = None,
    solo_griego: bool = False,
) -> list[tuple[int, int, str, str]]:
    """Devuelve [(capítulo, versículo, sufijo, texto)] desde el TEI.

    Con «parte» se lee solo una de las obras del archivo, que es como vienen
    las siete cartas de Ignacio. Con «solo_griego» se descartan los párrafos
    que no lo están, para las ediciones que imprimen también la traducción.
    """
    raiz = ET.parse(ruta).getroot()
    edicion = raiz.find(f".//{TEI}body/{TEI}div")
    if edicion is None:
        return []

    if parte is not None:
        edicion = next(
            (d for d in edicion.iter(TEI + "div")
             if d.get("subtype") == "epistle" and _numero(d) == parte),
            None,
        )
        if edicion is None:
            return []

    # Los capítulos son los «textpart» de tipo chapter, estén al primer nivel
    # o —como en Hermas— dentro de una parte mayor. Se recorren en orden de
    # documento, que es el de la edición impresa.
    capitulos = [
        d for d in edicion.iter(TEI + "div")
        if d.get("subtype") == "chapter"
    ]

    versiculos: list[tuple[int, int, str, str]] = []
    for indice, capitulo in enumerate(capitulos, 1):
        # Si los capítulos no se reinician, se respeta el número de la fuente;
        # si se repiten —Hermas— se usa el orden, que es la numeración continua.
        propio = _numero(capitulo)
        numero = propio if propio is not None else indice

        secciones = [
            d for d in capitulo.iter(TEI + "div")
            if d.get("subtype") == "section"
        ]
        if not secciones:
            texto = " ".join(_parrafos(capitulo, solo_griego))
            if texto.strip():
                versiculos.append((numero, 1, "", texto))
            continue

        for orden, seccion in enumerate(secciones, 1):
            verso = _numero(seccion) or orden
            texto = " ".join(_parrafos(seccion, solo_griego))
            if texto.strip():
                versiculos.append((numero, verso, "", texto))

    # Hermas repite los números de capítulo en cada una de sus tres partes, así
    # que ahí el número de la fuente no vale como clave: se renumera de corrido.
    claves = [(c, v) for c, v, _, _ in versiculos]
    if len(set(claves)) != len(claves):
        renumerado: list[tuple[int, int, str, str]] = []
        corrido = 0
        anterior = None
        for c, v, s, t in versiculos:
            if c != anterior:
                corrido += 1
                anterior = c
            renumerado.append((corrido, v, s, t))
        versiculos = renumerado

    return versiculos
