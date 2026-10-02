"""Limpieza de artefactos de transcripción en el texto griego.

La digitalización de Swete hecha por First1KGreek arrastra restos de OCR:
numerales romanos de encabezado pegados a las palabras (`IXκαὶ`), siglas de
manuscritos sueltas (`B`, `D`, `om`) y letras latinas confundidas con griegas
dentro de una palabra (`Aἴγυπτον` con A latina).

Estas funciones quitan lo que es demostrablemente ajeno al texto y corrigen los
homóglifos. Lo que no se puede arreglar aquí son las palabras a las que el OCR
les comió letras (`καταπαύσουσιν` → `κατα`): reponerlas exigiría cotejar con la
edición impresa, así que se dejan como están y se cuentan en el informe.
"""

from __future__ import annotations

import re

# Latina -> griega, solo para letras que el OCR confunde por su forma.
HOMOGLYPHS = str.maketrans({
    "A": "Α", "B": "Β", "E": "Ε", "Z": "Ζ", "H": "Η", "I": "Ι", "K": "Κ",
    "M": "Μ", "N": "Ν", "O": "Ο", "P": "Ρ", "T": "Τ", "X": "Χ", "Y": "Υ",
    "a": "α", "e": "ε", "o": "ο", "p": "ρ", "k": "κ", "u": "υ", "v": "ν",
    "x": "χ", "i": "ι", "t": "τ",
})

GREEK = re.compile(r"[Ͱ-Ͽἀ-῿]")
LATIN = re.compile(r"[A-Za-z]")
# Dos letras o más: una sola «I» pegada a griego suele ser una iota mal leída,
# no el numeral de un encabezado, así que esa se deja al mapa de homóglifos.
ROMAN_PREFIX = re.compile(r"^[IVXLCDM]{2,}(?=[Ͱ-Ͽἀ-῿])")
ROMAN_SUFFIX = re.compile(r"(?<=[Ͱ-Ͽἀ-῿])[IVXLCDM]{2,}$")
ONLY_LATIN = re.compile(r"^[A-Za-z]+[.,;:·]?$")


def clean_token(token: str) -> str | None:
    """Devuelve el token limpio, o None si hay que descartarlo entero."""
    if not GREEK.search(token):
        # Sin una sola letra griega: sigla de manuscrito, numeral de capítulo o
        # abreviatura del aparato crítico. Nada de eso es texto bíblico.
        if ONLY_LATIN.match(token):
            return None
        return token

    # Numerales romanos de encabezado pegados al principio o al final.
    token = ROMAN_PREFIX.sub("", token)
    token = ROMAN_SUFFIX.sub("", token)

    if LATIN.search(token):
        token = token.translate(HOMOGLYPHS)

    return token or None


def clean_text(text: str) -> str:
    tokens = [clean_token(t) for t in text.split()]
    return " ".join(t for t in tokens if t)


def count_residual(text: str) -> int:
    """Palabras que siguen mezclando latín y griego tras la limpieza."""
    return sum(1 for t in text.split() if LATIN.search(t))
