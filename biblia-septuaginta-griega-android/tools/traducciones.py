"""Las traducciones a otros idiomas, en los tres formatos en que vienen.

La aplicación trae el texto en su lengua —hebreo y griego—, que es lo que no
cambia con el idioma de quien lee. La traducción sí cambia, y hay una libre para
cada idioma de esta lista, todas de https://github.com/seven1m/open-bibles.

Vienen en tres formatos distintos, con tres maneras distintas de marcar dónde
empieza un versículo y de nombrar los libros. Este módulo los lee los tres y
devuelve siempre lo mismo: {(código de libro, capítulo, versículo): texto}.

Pesan 4,8 MB cada una, así que no viajan dentro de la aplicación: se publica un
archivo por idioma y se descarga el que haga falta. Ver docs/PLAN_IDIOMAS.md.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import NamedTuple

from canon import POR_USFX, POR_ZEFANIA, desde_osis

Versiculos = dict[tuple[str, int, int], str]


class Traduccion(NamedTuple):
    codigo: str    # el código de idioma de Android: es, en, pt-BR…
    idioma: str    # cómo se llama el idioma en su propio idioma
    archivo: str   # el archivo en open-bibles
    formato: str   # usfx | osis | zefania
    version: str   # cómo se llama esta traducción
    licencia: str


# Las traducciones que se publican. El código es el que Android usa para elegir
# idioma; el nombre está en el propio idioma porque quien lo busca lo busca así.
CATALOGO: tuple[Traduccion, ...] = (
    Traduccion("sq", "Shqip", "sqi-albanian.osis.xml", "osis", "Albanian Bible", "Dominio público"),
    Traduccion("de", "Deutsch", "deu-luther1912.osis.xml", "osis", "Luther 1912", "Dominio público"),
    Traduccion("bg", "Български", "bul-bulgarian.osis.xml", "osis", "Bulgarian Bible", "Dominio público"),
    Traduccion("cs", "Čeština", "cze-bkr.zefania.xml", "zefania", "Bible kralická", "Dominio público"),
    Traduccion("chr", "ᏣᎳᎩ", "chr-cherokee.usfx.xml", "usfx", "Cherokee New Testament", "Dominio público"),
    Traduccion("zh-CN", "简体中文", "chi-cuv-simp.usfx.xml", "usfx", "和合本", "Dominio público"),
    Traduccion("zh-TW", "繁體中文", "chi-cuv.usfx.xml", "usfx", "和合本", "Dominio público"),
    Traduccion("ko", "한국어", "kor-korean.osis.xml", "osis", "Korean Bible", "Dominio público"),
    Traduccion("hr", "Hrvatski", "hrv-croatian.osis.xml", "osis", "Croatian Bible", "Dominio público"),
    Traduccion("da", "Dansk", "dan-danish.osis.xml", "osis", "Danish Bible", "Dominio público"),
    Traduccion("sk", "Slovenčina", "", "", "", ""),  # sin fuente libre localizada
    Traduccion("es", "Español", "spa-rv1909.usfx.xml", "usfx", "Reina-Valera 1909", "Dominio público"),
    Traduccion("fi", "Suomi", "fin-biblia.osis.xml", "osis", "Finnish Bible", "Dominio público"),
    Traduccion("fr", "Français", "fra-ostervald.osis.xml", "osis", "Ostervald 1996", "Dominio público"),
    Traduccion("nl", "Nederlands", "dut-statenvertaling.zefania.xml", "zefania", "Statenvertaling 1637", "Dominio público"),
    Traduccion("hu", "Magyar", "hun-karoli.osis.xml", "osis", "Károli", "Dominio público"),
    Traduccion("en", "English", "eng-kjv.osis.xml", "osis", "King James Version", "Dominio público"),
    Traduccion("it", "Italiano", "ita-riveduta.osis.xml", "osis", "Riveduta 1927", "Dominio público"),
    Traduccion("ja", "日本語", "jpn-kougo.osis.xml", "osis", "口語訳", "Dominio público"),
    Traduccion("la", "Latina", "lat-clementine.usfx.xml", "usfx", "Vulgata Clementina", "Dominio público"),
    Traduccion("lv", "Latviešu", "lav-latvian.osis.xml", "osis", "Latvian Bible", "Dominio público"),
    Traduccion("mi", "Māori", "mri-maori.osis.xml", "osis", "Maori Bible", "Dominio público"),
    Traduccion("nb", "Norsk", "nor-norwegian.osis.xml", "osis", "Norwegian Bible", "Dominio público"),
    Traduccion("pl", "Polski", "pol-gdanska.osis.xml", "osis", "Biblia Gdańska", "Dominio público"),
    Traduccion("pt", "Português", "por-almeida.usfx.xml", "usfx", "João Ferreira de Almeida", "Dominio público"),
    Traduccion("ro", "Română", "ron-rccv.usfx.xml", "usfx", "Cornilescu corregida", "Dominio público"),
    Traduccion("ru", "Русский", "rus-synodal.zefania.xml", "zefania", "Синодальный перевод", "Dominio público"),
    Traduccion("sw", "Kiswahili", "swa-swahili.osis.xml", "osis", "Swahili Bible", "Dominio público"),
    Traduccion("sv", "Svenska", "swe-swedish.osis.xml", "osis", "Swedish Bible", "Dominio público"),
    Traduccion("tl", "Tagalog", "tgl-tagalog.osis.xml", "osis", "Ang Dating Biblia", "Dominio público"),
    Traduccion("th", "ไทย", "tha-thai.osis.xml", "osis", "Thai Bible", "Dominio público"),
    Traduccion("tr", "Türkçe", "tur-turkish.osis.xml", "osis", "Turkish Bible", "Dominio público"),
    Traduccion("vi", "Tiếng Việt", "vie-cadman.osis.xml", "osis", "Cadman 1934", "Dominio público"),
)

DISPONIBLES = tuple(t for t in CATALOGO if t.archivo)

# Marcas editoriales que no son el texto del versículo: notas al pie,
# referencias cruzadas, títulos de sección, encabezados de página.
FUERA_USFX = {"f", "x", "fr", "ft", "fq", "fk", "xo", "xt", "rem", "toc", "h", "id"}
FUERA_OSIS = {"note", "title", "reference", "milestone", "lb", "figure"}
FUERA_ZEFANIA = {"NOTE", "XREF", "CAPTION", "PROLOG", "REMARK", "GRAM"}


def _limpiar(texto: str) -> str:
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r"\s+([,.;:!?»])", r"\1", texto)
    return texto.strip()


def _sin_espacio(tag: str) -> str:
    """`{http://…}verse` -> `verse`. OSIS trae espacio de nombres, los otros no."""
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


# --------------------------------------------------------------------------
# USFX: los versículos son marcas, no contenedores. `<v id="1"/>` abre y el
# texto va suelto detrás, hasta la marca siguiente.
# --------------------------------------------------------------------------
def _leer_usfx(path: Path) -> Versiculos:
    raiz = ET.parse(path).getroot()
    salida: Versiculos = {}

    for libro in raiz.iter("book"):
        app = POR_USFX.get((libro.get("id") or "").strip().upper())
        if app is None:
            continue  # deuterocanónico o libro que esta aplicación no numera así
        capitulo = versiculo = 0
        piezas: list[str] = []

        def cerrar() -> None:
            if versiculo and piezas:
                texto = _limpiar("".join(piezas))
                if texto:
                    salida[(app, capitulo, versiculo)] = texto

        def recorrer(nodo: ET.Element) -> None:
            nonlocal capitulo, versiculo, piezas
            for hijo in nodo:
                etiqueta = _sin_espacio(hijo.tag)
                if etiqueta == "c":
                    cerrar()
                    piezas, versiculo = [], 0
                    capitulo = int(re.sub(r"\D", "", hijo.get("id") or "0") or 0)
                elif etiqueta == "v":
                    cerrar()
                    piezas = []
                    versiculo = int(re.sub(r"\D", "", hijo.get("id") or "0") or 0)
                elif etiqueta == "ve":
                    cerrar()
                    piezas, versiculo = [], 0
                elif etiqueta in FUERA_USFX:
                    pass
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


# --------------------------------------------------------------------------
# OSIS: de dos maneras. O el versículo contiene su texto, o es una marca con
# sID que abre y otra con eID que cierra. Hay digitalizaciones de las dos.
# --------------------------------------------------------------------------
def _leer_osis(path: Path) -> Versiculos:
    raiz = ET.parse(path).getroot()
    salida: Versiculos = {}
    abierto: tuple[str, int, int] | None = None
    piezas: list[str] = []

    def referencia(osis_id: str) -> tuple[str, int, int] | None:
        partes = osis_id.split(".")
        if len(partes) < 3:
            return None
        app = desde_osis(partes[0])
        if app is None:
            return None
        try:
            return app, int(partes[1]), int(re.sub(r"\D", "", partes[2]) or 0)
        except ValueError:
            return None

    def cerrar() -> None:
        nonlocal abierto, piezas
        if abierto and piezas:
            texto = _limpiar("".join(piezas))
            if texto:
                salida[abierto] = texto
        abierto, piezas = None, []

    def texto_de(nodo: ET.Element) -> str:
        """Todo el texto de dentro, saltando notas y títulos."""
        trozos = [nodo.text or ""]
        for hijo in nodo:
            if _sin_espacio(hijo.tag) not in FUERA_OSIS:
                trozos.append(texto_de(hijo))
            trozos.append(hijo.tail or "")
        return "".join(trozos)

    def recorrer(nodo: ET.Element) -> None:
        nonlocal abierto, piezas
        for hijo in nodo:
            etiqueta = _sin_espacio(hijo.tag)
            if etiqueta == "verse":
                if hijo.get("eID"):
                    cerrar()
                elif hijo.get("sID"):
                    cerrar()
                    abierto = referencia(hijo.get("osisID") or "")
                else:
                    # Versículo contenedor: se lee entero y se cierra solo.
                    cerrar()
                    ref = referencia(hijo.get("osisID") or "")
                    if ref:
                        texto = _limpiar(texto_de(hijo))
                        if texto:
                            salida[ref] = texto
                if hijo.tail and abierto:
                    piezas.append(hijo.tail)
                continue
            if etiqueta in FUERA_OSIS:
                if hijo.tail and abierto:
                    piezas.append(hijo.tail)
                continue
            if abierto and hijo.text:
                piezas.append(hijo.text)
            recorrer(hijo)
            if hijo.tail and abierto:
                piezas.append(hijo.tail)

    recorrer(raiz)
    cerrar()
    return salida


# --------------------------------------------------------------------------
# Zefania: los libros no se nombran, se numeran del 1 al 66.
# --------------------------------------------------------------------------
def _leer_zefania(path: Path) -> Versiculos:
    raiz = ET.parse(path).getroot()
    salida: Versiculos = {}

    def texto_de(nodo: ET.Element) -> str:
        trozos = [nodo.text or ""]
        for hijo in nodo:
            if _sin_espacio(hijo.tag).upper() not in FUERA_ZEFANIA:
                trozos.append(texto_de(hijo))
            trozos.append(hijo.tail or "")
        return "".join(trozos)

    for libro in raiz.iter("BIBLEBOOK"):
        try:
            app = POR_ZEFANIA.get(int(libro.get("bnumber") or 0))
        except ValueError:
            continue
        if app is None:
            continue
        for capitulo in libro.iter("CHAPTER"):
            try:
                c = int(capitulo.get("cnumber") or 0)
            except ValueError:
                continue
            for verso in capitulo.iter("VERS"):
                try:
                    v = int(re.sub(r"\D", "", verso.get("vnumber") or "0") or 0)
                except ValueError:
                    continue
                texto = _limpiar(texto_de(verso))
                if c and v and texto:
                    salida[(app, c, v)] = texto

    return salida


LECTORES = {"usfx": _leer_usfx, "osis": _leer_osis, "zefania": _leer_zefania}


def leer(carpeta: Path, traduccion: Traduccion) -> Versiculos:
    """Lee una traducción y la devuelve en la forma común."""
    lector = LECTORES.get(traduccion.formato)
    if lector is None:
        raise ValueError(f"formato desconocido: {traduccion.formato}")
    return lector(carpeta / traduccion.archivo)
