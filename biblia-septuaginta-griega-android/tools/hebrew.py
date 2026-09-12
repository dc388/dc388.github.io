"""Antiguo Testamento hebreo: lectura del OSIS de OSHB y morfología en español.

Fuente: Open Scriptures Hebrew Bible (https://github.com/openscriptures/morphhb),
el Códice de Leningrado etiquetado con números Strong y análisis morfológico,
bajo licencia CC BY 4.0.

La morfología no se reimplementa aquí: OSHB publica en `parsing/Oshm.xml` la
clave oficial de sus 3 481 códigos con la descripción de cada uno en inglés.
Este módulo traduce esas descripciones a partir de un glosario cerrado de 96
términos, y avisa si aparece cualquier palabra que no sepa traducir, de modo que
nunca se muestre al lector una etiqueta a medias.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

OSIS_NS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"
TEI_NS = "{http://www.crosswire.org/2008/TEIOSIS/namespace}"

# --- Libros: archivo OSIS -> (código, nombre español, nombre hebreo, alterno)
HEBREW_BOOKS = [
    ("Gen", "GEN", "Génesis", "בְּרֵאשִׁית", None),
    ("Exod", "EXO", "Éxodo", "שְׁמוֹת", None),
    ("Lev", "LEV", "Levítico", "וַיִּקְרָא", None),
    ("Num", "NUM", "Números", "בְּמִדְבַּר", None),
    ("Deut", "DEU", "Deuteronomio", "דְּבָרִים", None),
    ("Josh", "JOS", "Josué", "יְהוֹשֻׁעַ", None),
    ("Judg", "JUE", "Jueces", "שׁוֹפְטִים", None),
    ("1Sam", "1SA", "1 Samuel", "שְׁמוּאֵל א", None),
    ("2Sam", "2SA", "2 Samuel", "שְׁמוּאֵל ב", None),
    ("1Kgs", "1RY", "1 Reyes", "מְלָכִים א", None),
    ("2Kgs", "2RY", "2 Reyes", "מְלָכִים ב", None),
    ("Isa", "ISA", "Isaías", "יְשַׁעְיָהוּ", None),
    ("Jer", "JER", "Jeremías", "יִרְמְיָהוּ", None),
    ("Ezek", "EZE", "Ezequiel", "יְחֶזְקֵאל", None),
    ("Hos", "OSE", "Oseas", "הוֹשֵׁעַ", None),
    ("Joel", "JOE", "Joel", "יוֹאֵל", None),
    ("Amos", "AMO", "Amós", "עָמוֹס", None),
    ("Obad", "ABD", "Abdías", "עֹבַדְיָה", None),
    ("Jonah", "JON", "Jonás", "יוֹנָה", None),
    ("Mic", "MIQ", "Miqueas", "מִיכָה", None),
    ("Nah", "NAH", "Nahúm", "נַחוּם", None),
    ("Hab", "HAB", "Habacuc", "חֲבַקּוּק", None),
    ("Zeph", "SOF", "Sofonías", "צְפַנְיָה", None),
    ("Hag", "AGE", "Ageo", "חַגַּי", None),
    ("Zech", "ZAC", "Zacarías", "זְכַרְיָה", None),
    ("Mal", "MAL", "Malaquías", "מַלְאָכִי", None),
    ("Ps", "SAL", "Salmos", "תְּהִלִּים", "numeración hebrea"),
    ("Prov", "PRO", "Proverbios", "מִשְׁלֵי", None),
    ("Job", "JOB", "Job", "אִיּוֹב", None),
    ("Song", "CNT", "Cantar de los Cantares", "שִׁיר הַשִּׁירִים", None),
    ("Ruth", "RUT", "Rut", "רוּת", None),
    ("Lam", "LAM", "Lamentaciones", "אֵיכָה", None),
    ("Eccl", "ECL", "Eclesiastés", "קֹהֶלֶת", None),
    ("Esth", "EST", "Ester", "אֶסְתֵּר", None),
    ("Dan", "DAN", "Daniel", "דָּנִיֵּאל", "con secciones en arameo"),
    ("Ezra", "ESD", "Esdras", "עֶזְרָא", "con secciones en arameo"),
    ("Neh", "NEH", "Nehemías", "נְחֶמְיָה", None),
    ("1Chr", "1CR", "1 Crónicas", "דִּבְרֵי הַיָּמִים א", None),
    ("2Chr", "2CR", "2 Crónicas", "דִּבְרֵי הַיָּמִים ב", None),
]

# --- Glosario cerrado: cada palabra que puede aparecer en Oshm.xml.
TERMS = {
    "Adjective": "adjetivo", "Adverb": "adverbio", "Conjunction": "conjunción",
    "Noun": "sustantivo", "Particle": "partícula", "Preposition": "preposición",
    "Pronoun": "pronombre", "Suffix": "sufijo", "Verb": "verbo",
    "absolute": "absoluto", "active": "activo", "adjective": "adjetivo",
    "affirmation": "de afirmación", "aphel": "afel", "article": "artículo",
    "both": "ambos géneros", "cardinal": "cardinal", "cohortative": "cohortativo",
    "common": "común", "construct": "constructo", "definite": "definido",
    "demonstrative": "demostrativo", "determined": "determinado",
    "direct": "directo", "directional": "direccional", "dual": "dual",
    "exhortation": "de exhortación", "feminine": "femenino", "first": "1ª",
    "gentilic": "gentilicio", "haphel": "hafel", "he": "he", "hiphil": "hifil",
    "hishtaphel": "hishtafel", "hithpaal": "hitpaal", "hithpael": "hitpael",
    "hithpalpel": "hitpalpel", "hithpeel": "hitpeel", "hithpoel": "hitpoel",
    "hithpolel": "hitpolel", "hophal": "hofal", "hothpaal": "hotpaal",
    "imperative": "imperativo", "imperfect": "imperfecto",
    "indefinite": "indefinido", "infinitive": "infinitivo",
    "interjection": "interjección", "interrogative": "interrogativo",
    "ishtaphel": "ishtafel", "ithpaal": "itpaal", "ithpeel": "itpeel",
    "ithpoel": "itpoel", "jussive": "yusivo", "marker": "marcador",
    "masculine": "masculino", "name": "nombre", "negative": "negativo",
    "niphal": "nifal", "nithpael": "nitpael", "number": "número", "nun": "nun",
    "object": "objeto", "ordinal": "ordinal", "pael": "pael", "palel": "palel",
    "paragogic": "paragógico", "participle": "participio", "passive": "pasivo",
    "peal": "peal", "pealal": "pealal", "peil": "peil", "perfect": "perfecto",
    "person": "persona", "personal": "personal", "piel": "piel",
    "pilel": "pilel", "pilpel": "pilpel", "plural": "plural", "poal": "poal",
    "poel": "poel", "polal": "polal", "polel": "polel", "polpal": "polpal",
    "pronominal": "pronominal", "proper": "propio", "pual": "pual",
    "pulal": "pulal", "qal": "qal", "relative": "relativo", "saphel": "safel",
    "second": "2ª", "sequential": "secuencial", "shaphel": "shafel",
    "singular": "singular", "third": "3ª", "tiphil": "tifil",
}

# Frases que en español no se traducen palabra por palabra. Se resuelven sobre la
# lista de tokens, no con sustituciones de texto: cualquier marcador intercalado
# acabaría partido, porque str.split() trata como espacio también a \x1c-\x1f.
PHRASES = {
    "direct object marker": "marcador de objeto directo",
    "definite article": "artículo definido",
    "proper name": "nombre propio",
    "cardinal number": "número cardinal",
    "ordinal number": "número ordinal",
    "directional he": "he direccional",
    "paragogic he": "he paragógica",
    "paragogic nun": "nun paragógica",
    "participle active": "participio activo",
    "participle passive": "participio pasivo",
    "infinitive absolute": "infinitivo absoluto",
    "infinitive construct": "infinitivo constructo",
    "sequential perfect": "perfecto secuencial",
    "sequential imperfect": "imperfecto secuencial",
    "first person": "1ª persona",
    "second person": "2ª persona",
    "third person": "3ª persona",
}

LONGEST_PHRASE = max(len(p.split()) for p in PHRASES)


def load_morph_key(path: Path) -> dict[str, str]:
    """Código -> descripción en inglés, tal cual la publica OSHB."""
    text = path.read_text(encoding="utf-8")
    return dict(re.findall(r'<entryFree n="([^"]+)">([^<]*)</entryFree>', text))


def build_part_key(key: dict[str, str]) -> dict[str, str]:
    """Descripción de cada morfema suelto, extraída de las entradas compuestas.

    La clave de OSHB solo lista combinaciones completas, así que un sufijo como
    `HSp3fs` nunca aparece por sí mismo. Pero toda entrada compuesta empareja sus
    morfemas con sus descripciones en el mismo orden, y de ahí se deduce cada
    parte por separado.
    """
    parts: dict[str, str] = {}
    for code, description in key.items():
        language, rest = code[0], code[1:]
        head, _, body = description.partition(":")
        segments = [x.strip() for x in body.split(";")]
        codes = rest.split("/")
        if len(codes) != len(segments):
            continue
        for part, segment in zip(codes, segments):
            parts.setdefault(f"{language}{part}", f"{head.strip()}: {segment}")
    return parts


def describe(code: str, key: dict[str, str], parts: dict[str, str]) -> str | None:
    """Descripción inglesa de un código, compuesta a partir de sus morfemas si hace falta.

    La clave oficial no cubre todas las combinaciones que aparecen en el texto:
    ocho de ellas faltan. Para esas se reconstruye la descripción juntando la de
    cada morfema, en vez de dejar la palabra sin analizar.
    """
    if code in key:
        return key[code]

    language, rest = code[0], code[1:]
    pieces = []
    for part in rest.split("/"):
        described = parts.get(f"{language}{part}")
        if described is None:
            return None
        pieces.append(described.partition(":")[2].strip())

    prefix = "Aramaic" if language == "A" else "Hebrew"
    return f"{prefix}: " + "; ".join(pieces)


def translate(description: str) -> tuple[str | None, list[str]]:
    """Traduce una descripción de Oshm.xml. Devuelve (español, términos sin traducir)."""
    language = None
    if description.strip().startswith(("Hebrew:", "Aramaic:")):
        head, _, description = description.partition(":")
        language = head.strip()

    parts, unknown = [], []
    for segment in description.split(";"):
        tokens = segment.split()
        words, i = [], 0
        while i < len(tokens):
            for length in range(LONGEST_PHRASE, 1, -1):
                phrase = " ".join(tokens[i:i + length])
                if phrase in PHRASES:
                    words.append(PHRASES[phrase])
                    i += length
                    break
            else:
                token = tokens[i]
                if token in TERMS:
                    words.append(TERMS[token])
                else:
                    unknown.append(token)
                    words.append(token)
                i += 1
        if words:
            parts.append(" ".join(words))

    if unknown:
        return None, unknown

    joined = " + ".join(parts)
    # El arameo del lector importa: partes de Daniel y Esdras están en esa lengua.
    return (f"arameo · {joined}" if language == "Aramaic" else joined), []


def strong_of(lemma: str) -> tuple[str, str] | None:
    """`b/7225` -> `("H7225", "")`; `1254 a` -> `("H1254", "a")`.

    El lema es prefijo(s) + raíz, y la raíz puede llevar una letra de homónimo.
    Esa letra no es decorativa: `1254 a` es «crear» y `1254 b` es «engordar», y
    es la que permite elegir el artículo correcto en Brown-Driver-Briggs.
    """
    matches = re.findall(r"(\d+)(?:\s+([a-z]))?", lemma or "")
    if not matches:
        return None
    number, homonym = matches[-1]
    return f"H{int(number)}", homonym or ""


def read_book(path: Path) -> list[tuple[int, int, str, list[tuple[str, str, str]]]]:
    """Lee un libro OSIS.

    Devuelve [(capítulo, versículo, texto, [(palabra, lema, morfología)])].
    El texto se reconstruye respetando maqqef (־, une palabras sin espacio),
    paseq (׀) y sof pasuq (׃, cierra el versículo).
    """
    tree = ET.parse(path)
    out = []

    for verse in tree.iter(f"{OSIS_NS}verse"):
        osis_id = verse.get("osisID")
        if not osis_id:
            continue
        _, chapter, number = osis_id.split(".")

        pieces: list[str] = []
        words: list[tuple[str, str, str]] = []
        glue = False  # el maqqef pega la palabra siguiente a la anterior

        for child in verse:
            tag = child.tag
            if tag == f"{OSIS_NS}w":
                surface = "".join(child.itertext()).replace("/", "").strip()
                if not surface:
                    continue
                if pieces and not glue:
                    pieces.append(" ")
                pieces.append(surface)
                words.append((surface, child.get("lemma", ""), child.get("morph", "")))
                glue = False
            elif tag == f"{OSIS_NS}seg":
                kind = child.get("type", "")
                mark = "".join(child.itertext())
                if kind == "x-maqqef":
                    pieces.append(mark)
                    glue = True
                elif kind == "x-paseq":
                    pieces.append(f" {mark}")
                    glue = False
                else:  # sof pasuq y demás signos de cierre
                    pieces.append(mark)
                    glue = False

        text = re.sub(r"\s+", " ", "".join(pieces)).strip()
        if text:
            out.append((int(chapter), int(number), text, words))

    return out


def morph_key_path(sources: Path) -> Path:
    return sources / "morphhb" / "parsing" / "Oshm.xml"


def wlc_path(sources: Path, osis_book: str) -> Path:
    return sources / "morphhb" / "wlc" / f"{osis_book}.xml"
