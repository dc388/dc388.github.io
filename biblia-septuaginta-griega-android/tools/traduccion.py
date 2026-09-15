"""Reina-Valera de 1909, para leer en español lo que dice el original.

La aplicación trae los tres textos en su lengua: hebreo, griego de la
Septuaginta y griego del Nuevo Testamento. Eso sirve para estudiarlos, pero no
para leerlos, y quien abre un capítulo quiere entender qué dice. Esta es la
traducción al español que se pone al lado.

Es la Reina-Valera de 1909, en dominio público. Se descartaron las revisiones
modernas: la de 1960 y las posteriores son propiedad de las Sociedades Bíblicas
Unidas y no se pueden distribuir con una aplicación. De las libres, la de 1909
es la que sigue el mismo tipo de texto que lleva esta aplicación —el masorético
en el Antiguo Testamento y el mayoritario en el Nuevo—, así que casa versículo a
versículo casi siempre.

Fuente: https://github.com/seven1m/open-bibles, archivo `spa-rv1909.usfx.xml`,
en formato USFX. Esa digitalización viene además etiquetada con números Strong,
que aquí no se usan: se guarda solo el texto.

Qué NO cubre: la Septuaginta. La Reina-Valera traduce del hebreo, y la
numeración de la Septuaginta se aparta de la hebrea en los Salmos, en Jeremías
y en varios libros más, además de traer libros que la Reina-Valera no tiene. Se
importa solo para el Antiguo Testamento hebreo y el Nuevo Testamento, donde la
correspondencia es fiable.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Código de esta aplicación -> código USFX estándar.
LIBROS_AT = {
    "GEN": "GEN", "EXO": "EXO", "LEV": "LEV", "NUM": "NUM", "DEU": "DEU",
    "JOS": "JOS", "JUE": "JDG", "1SA": "1SA", "2SA": "2SA", "1RY": "1KI",
    "2RY": "2KI", "ISA": "ISA", "JER": "JER", "EZE": "EZK", "OSE": "HOS",
    "JOE": "JOL", "AMO": "AMO", "ABD": "OBA", "JON": "JON", "MIQ": "MIC",
    "NAH": "NAM", "HAB": "HAB", "SOF": "ZEP", "AGE": "HAG", "ZAC": "ZEC",
    "MAL": "MAL", "SAL": "PSA", "PRO": "PRO", "JOB": "JOB", "CNT": "SNG",
    "RUT": "RUT", "LAM": "LAM", "ECL": "ECC", "EST": "EST", "DAN": "DAN",
    "ESD": "EZR", "NEH": "NEH", "1CR": "1CH", "2CR": "2CH",
}
LIBROS_NT = {
    "MAT": "MAT", "MAR": "MRK", "LUC": "LUK", "JUA": "JHN", "HEC": "ACT",
    "ROM": "ROM", "1CO": "1CO", "2CO": "2CO", "GAL": "GAL", "EFE": "EPH",
    "FIL": "PHP", "COL": "COL", "1TE": "1TH", "2TE": "2TH", "1TI": "1TI",
    "2TI": "2TI", "TIT": "TIT", "FLM": "PHM", "HEB": "HEB", "SAN": "JAS",
    "1PE": "1PE", "2PE": "2PE", "1JN": "1JN", "2JN": "2JN", "3JN": "3JN",
    "JUD": "JUD", "APO": "REV",
}

# Marcas editoriales de la digitalización que no son texto bíblico.
FUERA = {"f", "x", "fr", "ft", "fq", "fk", "xo", "xt", "rem", "toc", "h", "id"}


def _limpiar(texto: str) -> str:
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r"\s+([,.;:!?»])", r"\1", texto)
    return texto.strip()


def leer(path: Path) -> dict[tuple[str, int, int], str]:
    """Devuelve {(código USFX, capítulo, versículo): texto en español}."""
    raiz = ET.parse(path).getroot()
    salida: dict[tuple[str, int, int], str] = {}

    for libro in raiz.iter("book"):
        code = libro.get("id") or ""
        capitulo = 0
        versiculo = 0
        piezas: list[str] = []

        def cerrar() -> None:
            if versiculo and piezas:
                texto = _limpiar("".join(piezas))
                if texto:
                    salida[(code, capitulo, versiculo)] = texto

        def recorrer(nodo: ET.Element) -> None:
            nonlocal capitulo, versiculo, piezas
            for hijo in nodo:
                etiqueta = hijo.tag
                if etiqueta == "c":
                    cerrar()
                    piezas = []
                    versiculo = 0
                    capitulo = int(hijo.get("id") or 0)
                elif etiqueta == "v":
                    cerrar()
                    piezas = []
                    versiculo = int(re.sub(r"\D", "", hijo.get("id") or "0") or 0)
                elif etiqueta == "ve":
                    cerrar()
                    piezas = []
                    versiculo = 0
                elif etiqueta in FUERA:
                    pass  # nota al pie o referencia cruzada: no es el versículo
                else:
                    if hijo.text:
                        piezas.append(hijo.text)
                    recorrer(hijo)
                if hijo.tail and versiculo:
                    piezas.append(hijo.tail)

        if libro.text:
            piezas.append(libro.text)
        recorrer(libro)
        cerrar()

    return salida
