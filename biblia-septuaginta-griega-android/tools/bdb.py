"""Léxico Brown-Driver-Briggs para el hebreo.

Fuente: https://github.com/openscriptures/HebrewLexicon — el *Brown-Driver-Briggs
Hebrew and English Lexicon* (1906), obra en dominio público, digitalizada por
Open Scriptures.

Strong da una definición de una línea; BDB da el artículo completo, con matices,
derivaciones y las citas donde aparece cada acepción. Es la diferencia entre
saber que una palabra significa «padre» y ver sus siete acepciones documentadas.

El enlace entre ambos sale de `LexicalIndex.xml`, que para cada entrada del
léxico declara `<xref bdb="a.ae.ab" strong="1"/>`, además de una glosa corta muy
útil para el interlineal.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "{http://openscriptures.github.com/morphhb/namespace}"

# Etiquetas cuyo contenido no es parte del artículo: el estado editorial de
# Open Scriptures y los saltos de página del libro impreso.
DROP = {f"{NS}status", f"{NS}page"}


def _clean(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s+([,;:.\)\]])", r"\1", text)
    text = re.sub(r"([\(\[])\s+", r"\1", text)
    return text


def _flatten(element: ET.Element) -> str:
    """Convierte una entrada de BDB en texto, conservando sus acepciones.

    BDB anida `<sense n="1">` con `<sense n="a">` dentro, y esa jerarquía es la
    mitad del valor del artículo: sin ella las acepciones se leen como una sola
    frase corrida. Cada acepción sale en su propia línea, sangrada según su
    profundidad.
    """
    pieces: list[str] = []

    def emit(text: str | None) -> None:
        if text:
            pieces.append(text)

    def walk(node: ET.Element, depth: int) -> None:
        if node.tag in DROP:
            emit(node.tail)
            return

        if node.tag == f"{NS}sense":
            number = node.get("n")
            emit("\n" + "   " * depth + (f"{number}. " if number else ""))
            emit(node.text)
            for child in node:
                walk(child, depth + 1)
            emit(node.tail)
            return

        if node.tag == f"{NS}stem":
            emit("\n" + "   " * depth)
            emit(node.text)
            emit(" ")
            for child in node:
                walk(child, depth)
            emit(node.tail)
            return

        emit(node.text)
        for child in node:
            walk(child, depth)
        emit(node.tail)

    emit(element.text)
    for child in element:
        walk(child, 1)

    lines = []
    for line in "".join(pieces).split("\n"):
        indent = len(line) - len(line.lstrip(" "))
        body = _clean(line).strip()
        if body:
            lines.append(" " * indent + body)
    return "\n".join(lines)


def load_index(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    """(Strong, homónimo) -> {bdb, gloss, pos, xlit} desde LexicalIndex.xml."""
    index: dict[tuple[str, str], dict[str, str]] = {}
    for entry in ET.parse(path).getroot().iter(f"{NS}entry"):
        xref = entry.find(f"{NS}xref")
        if xref is None:
            continue
        strong = xref.get("strong")
        bdb = xref.get("bdb")
        if not strong or not bdb:
            continue
        if not strong.isdigit():
            # Ocho entradas usan una letra en vez de número: son los prefijos
            # hebreos (b, c, d, k, l, m, s, i), que OSHB tampoco numera y que
            # nunca llegan a `words.strong`.
            continue

        word = entry.find(f"{NS}w")
        definition = entry.find(f"{NS}def")
        pos = entry.find(f"{NS}pos")

        # `aug` distingue los homónimos de un mismo número Strong.
        key = (f"H{int(strong)}", xref.get("aug") or "")
        index.setdefault(
            key,
            {
                "bdb": bdb,
                "gloss": (definition.text or "").strip() if definition is not None else "",
                "pos": (pos.text or "").strip() if pos is not None else "",
                "xlit": (word.get("xlit") or "") if word is not None else "",
            },
        )
    return index


def load_entries(path: Path) -> dict[str, str]:
    """Identificador de entrada BDB -> artículo en texto plano."""
    entries: dict[str, str] = {}
    for entry in ET.parse(path).getroot().iter(f"{NS}entry"):
        entry_id = entry.get("id")
        if not entry_id:
            continue
        text = _flatten(entry)
        if text:
            entries[entry_id] = text
    return entries


def build(lexicon_dir: Path) -> dict[tuple[str, str], dict[str, str]]:
    """(Strong, homónimo) -> {bdb, gloss, pos, xlit, text} con el artículo resuelto."""
    index = load_index(lexicon_dir / "LexicalIndex.xml")
    entries = load_entries(lexicon_dir / "BrownDriverBriggs.xml")

    out: dict[tuple[str, str], dict[str, str]] = {}
    for key, data in index.items():
        text = entries.get(data["bdb"])
        if text:
            out[key] = {**data, "text": text}
    return out


def resolve(
    articles: dict[tuple[str, str], dict[str, str]],
    strong: str,
    homonym: str,
) -> dict[str, str] | None:
    """Artículo para una palabra concreta, con respaldo si falta el homónimo exacto."""
    exact = articles.get((strong, homonym))
    if exact:
        return exact
    for candidate in ("a", ""):
        found = articles.get((strong, candidate))
        if found:
            return found
    for (other_strong, _), data in articles.items():
        if other_strong == strong:
            return data
    return None
