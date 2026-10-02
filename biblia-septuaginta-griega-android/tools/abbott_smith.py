"""Léxico griego de Abbott-Smith.

Fuente: https://github.com/translatable-exegetical-tools/Abbott-Smith — el
*Manual Greek Lexicon of the New Testament* de G. Abbott-Smith (1922), que el
propio repositorio declara en dominio público.

Es el equivalente griego de Brown-Driver-Briggs: donde Strong da una línea,
Abbott-Smith da el artículo con sus acepciones y las citas de cada una. La
propuesta original pedía Thayer; Abbott-Smith cubre la misma necesidad y está
mucho mejor digitalizado y con licencia inequívoca.

Cada entrada declara sus números Strong en el atributo `n`, con la forma
`Ἀαρών|G2`, así que el enlace con el texto etiquetado es directo. Una misma
entrada puede cubrir varios números a la vez —`αὐτός|G846|G4571|G4671|…`, porque
Strong numeró por separado formas flexionadas del mismo lema— y todos ellos
apuntan al mismo artículo.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

# Metadatos editoriales que no son parte del artículo.
DROP_NOTE_TYPES = {"occurrencesNT", "editorial"}


def _clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s+([,;:.\)\]])", r"\1", text)
    text = re.sub(r"([\(\[])\s+", r"\1", text)
    return text


def _localname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _flatten(entry: ET.Element) -> str:
    """Texto del artículo conservando la jerarquía de acepciones."""
    pieces: list[str] = []

    def emit(text: str | None) -> None:
        if text:
            pieces.append(text)

    def walk(node: ET.Element, depth: int) -> None:
        tag = _localname(node.tag)

        if tag == "note" and node.get("type") in DROP_NOTE_TYPES:
            emit(node.tail)
            return

        if tag == "sense":
            number = (node.get("n") or "").strip()
            emit("\n" + "   " * depth + (f"{number} " if number else ""))
            emit(node.text)
            for child in node:
                walk(child, depth + 1)
            emit(node.tail)
            return

        emit(node.text)
        for child in node:
            walk(child, depth)
        emit(node.tail)

    emit(entry.text)
    for child in entry:
        walk(child, 0)

    lines = []
    for line in "".join(pieces).split("\n"):
        indent = len(line) - len(line.lstrip(" "))
        body = _clean(line).strip()
        if body:
            lines.append(" " * indent + body)
    return "\n".join(lines)


def _text_of(node: ET.Element) -> str:
    return _clean("".join(node.itertext())).strip(" ,;.")


def _part_of_speech(entry: ET.Element) -> str:
    for node in entry.iter():
        if _localname(node.tag) == "pos":
            text = _text_of(node)
            if text:
                return text
    return ""


def _gloss(entry: ET.Element) -> str:
    """Definición breve para el interlineal: la primera glosa del artículo.

    Se toma tal cual la da Abbott-Smith, sin heurísticas. En las palabras de
    contenido acierta siempre («λόγος» → *a word*, «ἀγάπη» → *love*). En unas
    pocas funcionales la primera glosa es la de la acepción con que la obra abre,
    que no es la más corriente: `ὁ` sale como *he*, porque Abbott-Smith empieza
    por el uso demostrativo homérico. Se prefiere esa rareza a inventar una
    traducción que la fuente no dice; el artículo completo está a un toque.
    """
    for node in entry.iter():
        if _localname(node.tag) == "gloss":
            text = _text_of(node)
            if text:
                return text
    return _part_of_speech(entry)


def build(path: Path) -> dict[str, dict[str, str]]:
    """Número Strong griego -> {headword, gloss, pos, article}."""
    out: dict[str, dict[str, str]] = {}

    for entry in ET.parse(path).getroot().iter():
        if _localname(entry.tag) != "entry":
            continue
        name = entry.get("n") or ""
        headword, *codes = name.split("|")
        strongs = [c for c in codes if re.fullmatch(r"G\d+", c)]
        if not strongs:
            continue

        article = _flatten(entry)
        if not article:
            continue

        data = {
            "headword": headword.strip(),
            "gloss": _gloss(entry),
            "pos": _part_of_speech(entry),
            "article": article,
        }
        # Un número Strong puede repetirse en varias entradas; gana la primera.
        for strong in strongs:
            out.setdefault(strong, data)
    return out
