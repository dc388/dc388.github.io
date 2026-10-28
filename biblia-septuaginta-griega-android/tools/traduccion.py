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

import collections
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

from modernizar import modernizar

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


# Las versalitas con que la Reina-Valera abre cada capítulo. La digitalización
# las guarda en mayúsculas de caja alta: «EN el principio era el Verbo», «Y
# ACONTECIÓ que», «MEJOR es un bocado seco». En un libro impreso eso es una
# letra capital y se lee como lo que es; en la pantalla de un teléfono, y sobre
# todo suelto en un mensaje de WhatsApp, parece una errata.
MAYUSCULAS = "A-ZÁÉÍÓÚÜÑ"
VERSALITAS = re.compile(
    r"^([¡¿«(\"']*)"                                  # signos de apertura
    rf"((?:[{MAYUSCULAS}]+[.,;:!?]?\s+)*[{MAYUSCULAS}]+[.,;:!?]?)"  # el bloque
    r"(\s)"
    rf"(?![{MAYUSCULAS}][{MAYUSCULAS}])"               # lo de después ya no lo es
    r"(?=\S)"
)


def _sin_tildes(palabra: str) -> str:
    """Quita las tildes para comparar.

    Hace falta porque `modernizar` ya le ha quitado la tilde al texto corrido
    —«fué» pasa a «fue»— pero no a la versalita, que viene en mayúsculas. Sin
    esto, «Y FUÉ a» se quedaba en «Y Fué a»: la palabra en minúscula que se
    buscaba no existía en ninguna parte.
    """
    return unicodedata.normalize("NFKD", palabra).encode("ascii", "ignore").decode()


_COMUNES: collections.Counter[str] = collections.Counter()


def _arreglar(texto: str, comunes: collections.Counter[str]) -> str | None:
    """Pone en caja normal la versalita con que abre un texto, si la trae."""
    m = VERSALITAS.match(texto)
    if m is None:
        return None
    bloque = m.group(2)
    if sum(c.isalpha() for c in bloque) < 2:
        return None  # una «Y» suelta no es una versalita
    arregladas = []
    empieza_frase = True
    for palabra in bloque.split():
        nucleo = palabra.rstrip(".,;:")
        cola = palabra[len(nucleo):]
        if empieza_frase or comunes[_sin_tildes(nucleo.lower())] < 3:
            arregladas.append(nucleo.capitalize() + cola)
        else:
            arregladas.append(nucleo.lower() + cola)
        # El «Aleph.» con que se abre cada estrofa del salmo 119 cierra frase:
        # lo que venga detrás empieza otra y lleva mayúscula.
        empieza_frase = cola.startswith((".", ":", ";"))
    return m.group(1) + " ".join(arregladas) + texto[m.end(2):]


def versalitas_a_caja_normal(texto: str) -> str:
    """El mismo arreglo, para un texto suelto.

    Lo usa `build_db` con los salmos. La Reina-Valera mete el encabezamiento y
    el cuerpo en su versículo 1 —«Salmo de David. JEHOVÁ es mi pastor»—, así
    que ahí la versalita no abre el versículo y solo queda al descubierto
    cuando `build_db` separa el título del cuerpo. Usa el recuento de la última
    lectura; sin lectura previa no hay con qué decidir y devuelve el texto tal
    cual.
    """
    return _arreglar(texto, _COMUNES) or texto


def _deshacer_versalitas(
    versiculos: dict[tuple[str, int, int], str],
) -> tuple[dict[tuple[str, int, int], str], int]:
    """Devuelve el texto con las versalitas de apertura puestas en caja normal.

    **Qué palabra lleva mayúscula y cuál no lo decide el propio texto**, no una
    lista escrita a mano. Si una palabra aparece en minúscula en el resto de la
    Biblia —«aconteció», «los», «como»— es común y va en minúscula; si no
    aparece nunca —«Jehová», «Abraham»— es nombre propio y se queda con su
    mayúscula. Así «Y ACONTECIÓ que» sale «Y aconteció que» y «Y ABRAHAM era
    viejo» sale «Y Abraham era viejo», sin decidirlo a ojo palabra por palabra.

    Solo se toca el versículo 1 de cada capítulo, que es donde la edición pone
    la capital, y solo el bloque inicial de palabras enteramente en mayúsculas
    seguido de una palabra en minúscula: lo demás se queda como está. Son 815
    versículos, uno por capítulo.
    """
    global _COMUNES
    comunes: collections.Counter[str] = collections.Counter()
    for texto in versiculos.values():
        for palabra in re.findall(rf"[a-záéíóúüñ][a-záéíóúüñ{MAYUSCULAS}]*", texto):
            comunes[_sin_tildes(palabra.lower())] += 1
    _COMUNES = comunes

    salida = dict(versiculos)
    tocados = 0
    for clave, texto in versiculos.items():
        if clave[2] != 1:
            continue
        arreglado = _arreglar(texto, comunes)
        if arreglado is not None:
            salida[clave] = arreglado
            tocados += 1
    return salida, tocados


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
                texto = modernizar(_limpiar("".join(piezas)), code, capitulo, versiculo)
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

    salida, _ = _deshacer_versalitas(salida)
    return salida
