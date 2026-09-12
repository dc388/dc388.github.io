#!/usr/bin/env python3
"""Construye app/src/main/assets/biblia.db a partir de textos griegos abiertos.

Fuentes:
  * Septuaginta (AT griego): edicion de H. B. Swete (Cambridge, 1887-1912),
    digitalizada por el proyecto First1KGreek y normalizada en
    https://github.com/nathans/lxx-swete  -- licencia CC BY-SA 4.0.
  * Nuevo Testamento griego: Robinson-Pierpont, "The New Testament in the
    Original Greek: Byzantine Textform" (edicion 2018),
    https://github.com/byztxt/byzantine-majority-text -- dominio publico.
  * Eclesiastes: Swete todavia no esta transcrito en First1KGreek, asi que ese
    unico libro se toma de https://github.com/LukeSmithxyz/grb (texto de
    tradicion Rahlfs). Queda marcado como tal en la columna books.source_note.
  * Interlineal del NT: el mismo repositorio de byztxt trae el texto etiquetado
    con numeros Strong y analisis morfologico de Robinson, alineado palabra a
    palabra con el texto acentuado.
  * Antiguo Testamento hebreo: Codice de Leningrado etiquetado con Strong y
    morfologia por el Open Scriptures Hebrew Bible,
    https://github.com/openscriptures/morphhb -- CC BY 4.0.
  * Lexicos griego y hebreo: diccionarios de Strong (1890) de
    https://github.com/openscriptures/strongs -- JSON bajo CC BY-SA.
  * Lexicos de referencia, ambos en dominio publico: Brown-Driver-Briggs (1906)
    para el hebreo, desde https://github.com/openscriptures/HebrewLexicon, y
    Abbott-Smith (1922) para el griego, desde
    https://github.com/translatable-exegetical-tools/Abbott-Smith.

Uso:
    python3 tools/build_db.py                 # clona las fuentes si hacen falta
    python3 tools/build_db.py --sources /ruta # reutiliza clones existentes
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clean import clean_text, count_residual  # noqa: E402
from morphology import build_table  # noqa: E402
from abbott_smith import build as build_abbott_smith  # noqa: E402
from bdb import build as build_bdb, resolve as resolve_bdb  # noqa: E402
from hebrew import (  # noqa: E402
    HEBREW_BOOKS,
    build_part_key,
    describe,
    load_morph_key,
    read_book,
    strong_of,
    translate,
    wlc_path,
)

REPOS = {
    "lxx-swete": "https://github.com/nathans/lxx-swete.git",
    "byz": "https://github.com/byztxt/byzantine-majority-text.git",
    "grb": "https://github.com/LukeSmithxyz/grb.git",
    "strongs": "https://github.com/openscriptures/strongs.git",
    "morphhb": "https://github.com/openscriptures/morphhb.git",
    "HebrewLexicon": "https://github.com/openscriptures/HebrewLexicon.git",
    "Abbott-Smith": "https://github.com/translatable-exegetical-tools/Abbott-Smith.git",
}

# --- Septuaginta: numero de archivo de Swete -> (codigo, nombre es, nombre griego, alterno)
LXX_BOOKS = {
    1:  ("GEN", "Génesis", "Γένεσις", None),
    2:  ("EXO", "Éxodo", "Ἔξοδος", None),
    3:  ("LEV", "Levítico", "Λευιτικόν", None),
    4:  ("NUM", "Números", "Ἀριθμοί", None),
    5:  ("DEU", "Deuteronomio", "Δευτερονόμιον", None),
    6:  ("JOS", "Josué", "Ἰησοῦς Ναυῆ", None),
    8:  ("JUE", "Jueces", "Κριταί", None),
    10: ("RUT", "Rut", "Ῥούθ", None),
    11: ("1RE", "1 Reinos", "Βασιλειῶν Αʹ", "1 Samuel"),
    12: ("2RE", "2 Reinos", "Βασιλειῶν Βʹ", "2 Samuel"),
    13: ("3RE", "3 Reinos", "Βασιλειῶν Γʹ", "1 Reyes"),
    14: ("4RE", "4 Reinos", "Βασιλειῶν Δʹ", "2 Reyes"),
    15: ("1PA", "1 Paralipómenos", "Παραλειπομένων Αʹ", "1 Crónicas"),
    16: ("2PA", "2 Paralipómenos", "Παραλειπομένων Βʹ", "2 Crónicas"),
    17: ("1ES", "1 Esdras", "Ἔσδρας Αʹ", "Esdras A"),
    18: ("2ES", "2 Esdras", "Ἔσδρας Βʹ", "Esdras–Nehemías"),
    19: ("EST", "Ester", "Ἐσθήρ", None),
    20: ("JDT", "Judit", "Ἰουδίθ", None),
    21: ("TOB", "Tobías", "Τωβίτ", "Tobit"),
    23: ("1MA", "1 Macabeos", "Μακκαβαίων Αʹ", None),
    24: ("2MA", "2 Macabeos", "Μακκαβαίων Βʹ", None),
    25: ("3MA", "3 Macabeos", "Μακκαβαίων Γʹ", None),
    26: ("4MA", "4 Macabeos", "Μακκαβαίων Δʹ", None),
    27: ("SAL", "Salmos", "Ψαλμοί", None),
    28: ("ODA", "Odas", "ᾨδαί", None),
    29: ("PRO", "Proverbios", "Παροιμίαι", None),
    30: ("ECL", "Eclesiastés", "Ἐκκλησιαστής", None),
    31: ("CNT", "Cantar de los Cantares", "Ἆσμα Ἀσμάτων", None),
    32: ("JOB", "Job", "Ἰώβ", None),
    33: ("SAB", "Sabiduría de Salomón", "Σοφία Σαλωμῶνος", None),
    34: ("SIR", "Eclesiástico", "Σοφία Σιράχ", "Sirácida"),
    35: ("SSA", "Salmos de Salomón", "Ψαλμοὶ Σαλωμῶντος", None),
    36: ("OSE", "Oseas", "Ὡσηέ", None),
    37: ("AMO", "Amós", "Ἀμώς", None),
    38: ("MIQ", "Miqueas", "Μιχαίας", None),
    39: ("JOE", "Joel", "Ἰωήλ", None),
    40: ("ABD", "Abdías", "Ἀβδιού", None),
    41: ("JON", "Jonás", "Ἰωνᾶς", None),
    42: ("NAH", "Nahúm", "Ναούμ", None),
    43: ("HAB", "Habacuc", "Ἀμβακούμ", None),
    44: ("SOF", "Sofonías", "Σοφονίας", None),
    45: ("AGE", "Ageo", "Ἀγγαῖος", None),
    46: ("ZAC", "Zacarías", "Ζαχαρίας", None),
    47: ("MAL", "Malaquías", "Μαλαχίας", None),
    48: ("ISA", "Isaías", "Ἠσαΐας", None),
    49: ("JER", "Jeremías", "Ἰερεμίας", None),
    50: ("BAR", "Baruc", "Βαρούχ", None),
    51: ("LAM", "Lamentaciones", "Θρῆνοι", None),
    52: ("CJE", "Carta de Jeremías", "Ἐπιστολὴ Ἰερεμίου", None),
    53: ("EZE", "Ezequiel", "Ἰεζεκιήλ", None),
    54: ("SUS", "Susana (LXX)", "Σουσάννα", None),
    55: ("SUT", "Susana (Teodoción)", "Σουσάννα (Θ)", None),
    56: ("DAN", "Daniel (LXX)", "Δανιήλ", None),
    57: ("DAT", "Daniel (Teodoción)", "Δανιήλ (Θ)", None),
    58: ("BEL", "Bel y el Dragón (LXX)", "Βὴλ καὶ Δράκων", None),
    59: ("BET", "Bel y el Dragón (Teodoción)", "Βὴλ καὶ Δράκων (Θ)", None),
}

# --- Nuevo Testamento: archivo CSV de byztxt -> (codigo, nombre es, nombre griego)
NT_BOOKS = [
    ("MAT", "MAT", "Mateo", "Κατὰ Ματθαῖον"),
    ("MAR", "MAR", "Marcos", "Κατὰ Μάρκον"),
    ("LUK", "LUC", "Lucas", "Κατὰ Λουκᾶν"),
    ("JOH", "JUA", "Juan", "Κατὰ Ἰωάννην"),
    ("ACT", "HEC", "Hechos", "Πράξεις Ἀποστόλων"),
    ("ROM", "ROM", "Romanos", "Πρὸς Ῥωμαίους"),
    ("1CO", "1CO", "1 Corintios", "Πρὸς Κορινθίους Αʹ"),
    ("2CO", "2CO", "2 Corintios", "Πρὸς Κορινθίους Βʹ"),
    ("GAL", "GAL", "Gálatas", "Πρὸς Γαλάτας"),
    ("EPH", "EFE", "Efesios", "Πρὸς Ἐφεσίους"),
    ("PHP", "FIL", "Filipenses", "Πρὸς Φιλιππησίους"),
    ("COL", "COL", "Colosenses", "Πρὸς Κολοσσαεῖς"),
    ("1TH", "1TE", "1 Tesalonicenses", "Πρὸς Θεσσαλονικεῖς Αʹ"),
    ("2TH", "2TE", "2 Tesalonicenses", "Πρὸς Θεσσαλονικεῖς Βʹ"),
    ("1TI", "1TI", "1 Timoteo", "Πρὸς Τιμόθεον Αʹ"),
    ("2TI", "2TI", "2 Timoteo", "Πρὸς Τιμόθεον Βʹ"),
    ("TIT", "TIT", "Tito", "Πρὸς Τίτον"),
    ("PHM", "FLM", "Filemón", "Πρὸς Φιλήμονα"),
    ("HEB", "HEB", "Hebreos", "Πρὸς Ἑβραίους"),
    ("JAM", "SAN", "Santiago", "Ἰακώβου"),
    ("1PE", "1PE", "1 Pedro", "Πέτρου Αʹ"),
    ("2PE", "2PE", "2 Pedro", "Πέτρου Βʹ"),
    ("1JO", "1JN", "1 Juan", "Ἰωάννου Αʹ"),
    ("2JO", "2JN", "2 Juan", "Ἰωάννου Βʹ"),
    ("3JO", "3JN", "3 Juan", "Ἰωάννου Γʹ"),
    ("JUD", "JUD", "Judas", "Ἰούδα"),
    ("REV", "APO", "Apocalipsis", "Ἀποκάλυψις Ἰωάννου"),
]

SCHEMA = """
PRAGMA journal_mode = DELETE;
CREATE TABLE meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
CREATE TABLE collections (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    short_name  TEXT NOT NULL,
    edition     TEXT NOT NULL,
    license     TEXT NOT NULL,
    source_url  TEXT NOT NULL,
    language    TEXT NOT NULL,
    rtl         INTEGER NOT NULL DEFAULT 0,
    sort_order  INTEGER NOT NULL
);
CREATE TABLE books (
    id             INTEGER PRIMARY KEY,
    collection_id  TEXT NOT NULL REFERENCES collections(id),
    code           TEXT NOT NULL,
    name_es        TEXT NOT NULL,
    name_orig      TEXT NOT NULL,
    alt_name       TEXT,
    source_note    TEXT,
    sort_order     INTEGER NOT NULL,
    chapter_count  INTEGER NOT NULL,
    verse_count    INTEGER NOT NULL
);
CREATE TABLE verses (
    id        INTEGER PRIMARY KEY,
    book_id   INTEGER NOT NULL REFERENCES books(id),
    chapter   INTEGER NOT NULL,
    verse     INTEGER NOT NULL,
    suffix    TEXT NOT NULL DEFAULT '',
    text      TEXT NOT NULL,
    text_norm TEXT NOT NULL
);
CREATE TABLE words (
    id        INTEGER PRIMARY KEY,
    verse_id  INTEGER NOT NULL REFERENCES verses(id),
    position  INTEGER NOT NULL,
    surface   TEXT NOT NULL,
    strong    TEXT NOT NULL,
    -- Letra que distingue homónimos del mismo número Strong: «1254 a» es crear
    -- y «1254 b» es engordar. Vacía cuando el lema no la trae.
    homonym   TEXT NOT NULL DEFAULT '',
    morph     TEXT NOT NULL
);
CREATE TABLE lexicon (
    strong     TEXT PRIMARY KEY,
    lemma      TEXT NOT NULL,
    translit   TEXT,
    derivation TEXT,
    definition TEXT,
    kjv_usage  TEXT
);
-- Artículos de léxico de referencia: Brown-Driver-Briggs para el hebreo y
-- Abbott-Smith para el griego. Una fila por cada palabra distinta del texto,
-- con el respaldo de homónimo ya resuelto en la importación.
CREATE TABLE articles (
    strong   TEXT NOT NULL,
    homonym  TEXT NOT NULL,
    source   TEXT NOT NULL,
    headword TEXT,
    gloss    TEXT,
    pos      TEXT,
    article  TEXT NOT NULL,
    PRIMARY KEY (strong, homonym)
);
CREATE TABLE morph_codes (
    code        TEXT PRIMARY KEY,
    description TEXT NOT NULL
);
CREATE INDEX idx_verses_loc  ON verses(book_id, chapter, verse, suffix);
CREATE INDEX idx_books_order ON books(collection_id, sort_order);
CREATE INDEX idx_words_verse ON words(verse_id, position);
CREATE INDEX idx_words_strong ON words(strong);
"""

TAGGED_RE = re.compile(r"(\S+)\s+(\d+)\s+\{([^}]+)\}")

VERSE_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)([a-zA-Z]*)$")

# Versículos que aún mezclan latín y griego tras la limpieza (OCR irrecuperable).
RESIDUAL = 0


def normalize(text: str) -> str:
    """Minúsculas sin diacríticos: permite buscar «λογος» y hallar «λόγος»."""
    decomposed = unicodedata.normalize("NFD", text.lower())
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    stripped = stripped.replace("ς", "σ")
    # signos de puntuación griegos y latinos fuera del índice de búsqueda
    stripped = re.sub(r"[^\w\s]", " ", stripped, flags=re.UNICODE)
    return re.sub(r"\s+", " ", stripped).strip()


def clean_verse(text: str) -> str:
    text = text.replace("¶", "").replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def prepare(text: str, scrub: bool) -> str:
    """Normaliza espacios y, en la LXX, quita los artefactos de OCR de Swete."""
    text = clean_verse(text)
    return clean_text(text) if scrub else text


def ensure_sources(sources: Path) -> None:
    sources.mkdir(parents=True, exist_ok=True)
    for name, url in REPOS.items():
        target = sources / name
        if target.exists():
            continue
        print(f"  clonando {url} -> {target}")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", url, str(target)],
            check=True,
        )


def read_swete(path: Path) -> list[tuple[int, int, str, str]]:
    """Devuelve [(capitulo, versiculo, sufijo, texto)] desde un archivo de palabra por linea."""
    verses: dict[tuple[int, int, str], list[str]] = {}
    order: list[tuple[int, int, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        ref, _, word = line.partition(" ")
        m = VERSE_RE.match(ref)
        if not m or not word:
            continue
        key = (int(m.group(2)), int(m.group(3)), m.group(4))
        if key not in verses:
            verses[key] = []
            order.append(key)
        verses[key].append(word)
    return [(c, v, s, " ".join(verses[(c, v, s)])) for (c, v, s) in order]


def read_grb_book(grb_tsv: Path, book_name: str) -> list[tuple[int, int, str, str]]:
    out: list[tuple[int, int, str, str]] = []
    with grb_tsv.open(encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) >= 6 and row[0] == book_name:
                out.append((int(row[3]), int(row[4]), "", row[5]))
    return out


def read_byz_csv(path: Path) -> list[tuple[int, int, str, str]]:
    out: list[tuple[int, int, str, str]] = []
    with path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            out.append((int(row["chapter"]), int(row["verse"]), "", row["text"]))
    return out


def insert_book(
    con: sqlite3.Connection,
    collection: str,
    code: str,
    name_es: str,
    name_orig: str,
    alt_name: str | None,
    source_note: str | None,
    order: int,
    verses: list[tuple[int, int, str, str]],
    scrub: bool = False,
) -> int | None:
    """Inserta el libro y sus versículos; devuelve el id del libro."""
    if not verses:
        return None
    chapters = len({c for c, _, _, _ in verses})
    cur = con.execute(
        "INSERT INTO books (collection_id, code, name_es, name_orig, alt_name, source_note,"
        " sort_order, chapter_count, verse_count) VALUES (?,?,?,?,?,?,?,?,?)",
        (collection, code, name_es, name_orig, alt_name, source_note, order, chapters, len(verses)),
    )
    book_id = cur.lastrowid
    prepared = [(c, v, s, prepare(t, scrub)) for (c, v, s, t) in verses]
    con.executemany(
        "INSERT INTO verses (book_id, chapter, verse, suffix, text, text_norm)"
        " VALUES (?,?,?,?,?,?)",
        [(book_id, c, v, s, t, normalize(t)) for (c, v, s, t) in prepared],
    )
    globals()["RESIDUAL"] += sum(1 for (_, _, _, t) in prepared if count_residual(t))
    return book_id


def read_tagged(path: Path) -> dict[tuple[int, int], list[tuple[str, str]]]:
    """Lee el CSV etiquetado: (capítulo, versículo) -> [(Strong, morfología)]."""
    out: dict[tuple[int, int], list[tuple[str, str]]] = {}
    with path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = (int(row["chapter"]), int(row["verse"]))
            out[key] = [
                (f"G{num}", morph) for _, num, morph in TAGGED_RE.findall(row["text"])
            ]
    return out


def insert_words(
    con: sqlite3.Connection,
    book_id: int,
    tagged: dict[tuple[int, int], list[tuple[str, str]]],
) -> tuple[int, int]:
    """Alinea el texto acentuado ya insertado con el etiquetado Strong/morfología.

    Devuelve (palabras insertadas, versículos que no alinearon). Un versículo cuyo
    número de palabras no coincida se omite entero: es preferible quedarse sin
    interlineal en ese versículo a mostrar una palabra con el análisis de otra.
    """
    rows, skipped = [], 0
    cursor = con.execute(
        "SELECT id, chapter, verse, text FROM verses WHERE book_id = ? ORDER BY id",
        (book_id,),
    )
    for verse_id, chapter, verse, text in cursor.fetchall():
        tags = tagged.get((chapter, verse))
        if tags is None:
            skipped += 1
            continue
        surfaces = text.split()
        if len(surfaces) != len(tags):
            skipped += 1
            continue
        for position, (surface, (strong, morph)) in enumerate(zip(surfaces, tags), 1):
            rows.append((verse_id, position, surface, strong, morph))

    con.executemany(
        "INSERT INTO words (verse_id, position, surface, strong, morph) VALUES (?,?,?,?,?)",
        rows,
    )
    return len(rows), skipped


def insert_hebrew(
    con: sqlite3.Connection,
    sources: Path,
    order: int,
    osis_book: str,
    code: str,
    name_es: str,
    name_he: str,
    alt: str | None,
) -> tuple[int, int, int]:
    """Inserta un libro del Antiguo Testamento hebreo con su interlineal.

    Devuelve (versículos, palabras con interlineal, palabras del texto). A
    diferencia del griego, aquí el texto y el análisis vienen del mismo archivo
    OSIS, así que no hay nada que alinear.
    """
    path = wlc_path(sources, osis_book)
    if not path.exists():
        print(f"  AVISO: falta {path}")
        return 0, 0, 0

    chapters = read_book(path)
    if not chapters:
        return 0, 0, 0

    verse_rows = [(c, v, "", text) for (c, v, text, _) in chapters]
    book_id = insert_book(con, "at", code, name_es, name_he, alt, None, order, verse_rows)
    if book_id is None:
        return 0, 0, 0

    ids = {
        (chapter, number): verse_id
        for verse_id, chapter, number in con.execute(
            "SELECT id, chapter, verse FROM verses WHERE book_id = ?", (book_id,)
        )
    }

    words = []
    seen = 0
    for chapter, number, _text, tokens in chapters:
        verse_id = ids.get((chapter, number))
        if verse_id is None:
            continue
        for position, (surface, lemma, morph) in enumerate(tokens, 1):
            seen += 1
            parsed = strong_of(lemma)
            if parsed is None or not morph:
                # Sin número Strong no hay nada que consultar en el léxico:
                # se deja fuera del interlineal en vez de inventar una entrada.
                continue
            strong, homonym = parsed
            words.append((verse_id, position, surface, strong, homonym, morph))

    con.executemany(
        "INSERT INTO words (verse_id, position, surface, strong, homonym, morph)"
        " VALUES (?,?,?,?,?,?)",
        words,
    )
    return len(verse_rows), len(words), seen


def insert_articles(con: sqlite3.Connection, sources: Path) -> tuple[int, int]:
    """Artículos de léxico para cada palabra distinta del texto etiquetado.

    Hebreo con Brown-Driver-Briggs y griego con Abbott-Smith. Se inserta una fila
    por cada par (Strong, homónimo) que realmente aparece, resolviendo aquí el
    respaldo de homónimo: así la consulta del lector es un JOIN directo y nunca
    se queda sin artículo por una distinción que el léxico no hace.
    """
    rows: list[tuple[str, str, str, str | None, str | None, str | None, str]] = []

    hebrew_dir = sources / "HebrewLexicon"
    hebrew_count = 0
    if (hebrew_dir / "LexicalIndex.xml").exists():
        articles = build_bdb(hebrew_dir)
        used = con.execute(
            "SELECT DISTINCT w.strong, w.homonym FROM words w"
            " JOIN verses v ON v.id = w.verse_id"
            " JOIN books b ON b.id = v.book_id"
            " WHERE b.collection_id = 'at'"
        ).fetchall()
        for strong, homonym in used:
            found = resolve_bdb(articles, strong, homonym)
            if found:
                rows.append(
                    (
                        strong,
                        homonym,
                        "Brown-Driver-Briggs",
                        None,
                        found["gloss"] or None,
                        found["pos"] or None,
                        found["text"],
                    )
                )
                hebrew_count += 1
    else:
        print("  AVISO: falta HebrewLexicon; se omite Brown-Driver-Briggs")

    greek_file = sources / "Abbott-Smith" / "abbott-smith.tei.xml"
    greek_count = 0
    if greek_file.exists():
        articles = build_abbott_smith(greek_file)
        used = con.execute(
            "SELECT DISTINCT w.strong FROM words w"
            " JOIN verses v ON v.id = w.verse_id"
            " JOIN books b ON b.id = v.book_id"
            " WHERE b.collection_id = 'nt'"
        ).fetchall()
        for (strong,) in used:
            found = articles.get(strong)
            if found:
                gloss = found["gloss"]
                rows.append(
                    (
                        strong,
                        "",
                        "Abbott-Smith",
                        found["headword"] or None,
                        gloss or found["pos"] or None,
                        found["pos"] or None,
                        found["article"],
                    )
                )
                greek_count += 1
    else:
        print("  AVISO: falta Abbott-Smith; se omite el léxico griego de referencia")

    con.executemany(
        "INSERT OR REPLACE INTO articles"
        " (strong, homonym, source, headword, gloss, pos, article)"
        " VALUES (?,?,?,?,?,?,?)",
        rows,
    )
    return hebrew_count, greek_count


def coverage(con: sqlite3.Connection, collection: str) -> float:
    """Porcentaje de palabras de una colección que tienen artículo de léxico."""
    total, with_article = con.execute(
        "SELECT COUNT(*), COUNT(a.strong) FROM words w"
        " JOIN verses v ON v.id = w.verse_id"
        " JOIN books b ON b.id = v.book_id"
        " LEFT JOIN articles a ON a.strong = w.strong AND a.homonym = w.homonym"
        " WHERE b.collection_id = ?",
        (collection,),
    ).fetchone()
    return 100.0 * with_article / total if total else 0.0


def insert_lexicon(con: sqlite3.Connection, sources: Path) -> int:
    """Diccionarios de Strong, griego y hebreo, distribuidos como JSON en un .js."""
    total = 0
    for language in ("greek", "hebrew"):
        path = sources / "strongs" / language / f"strongs-{language}-dictionary.js"
        if not path.exists():
            print(f"  AVISO: falta el diccionario Strong de {language}")
            continue
        raw = path.read_text(encoding="utf-8")
        entries = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
        con.executemany(
            "INSERT OR IGNORE INTO lexicon"
            " (strong, lemma, translit, derivation, definition, kjv_usage)"
            " VALUES (?,?,?,?,?,?)",
            [
                (
                    strong,
                    (e.get("lemma") or "").strip(),
                    # el griego usa «translit» y el hebreo «xlit»
                    (e.get("translit") or e.get("xlit") or "").strip() or None,
                    (e.get("derivation") or "").strip() or None,
                    (e.get("strongs_def") or "").strip() or None,
                    (e.get("kjv_def") or "").strip() or None,
                )
                for strong, e in entries.items()
            ],
        )
        total += len(entries)
    return total


def verify(con: sqlite3.Connection) -> list[str]:
    """Invariantes del interlineal. Devuelve la lista de fallos encontrados."""
    problems = []

    huerfanas = con.execute(
        "SELECT COUNT(*) FROM words w LEFT JOIN lexicon l ON l.strong = w.strong"
        " WHERE l.strong IS NULL"
    ).fetchone()[0]
    if huerfanas:
        problems.append(f"{huerfanas} palabras sin entrada en el léxico")

    sin_morf = con.execute(
        "SELECT COUNT(*) FROM words w LEFT JOIN morph_codes m ON m.code = w.morph"
        " WHERE m.code IS NULL"
    ).fetchone()[0]
    if sin_morf:
        problems.append(f"{sin_morf} palabras sin descripción morfológica")

    for collection, label in (("nt", "NT"), ("at", "AT hebreo")):
        sin_analizar = con.execute(
            "SELECT COUNT(*) FROM verses v JOIN books b ON b.id = v.book_id"
            " WHERE b.collection_id = ?"
            " AND NOT EXISTS (SELECT 1 FROM words w WHERE w.verse_id = v.id)",
            (collection,),
        ).fetchone()[0]
        if sin_analizar:
            problems.append(f"{sin_analizar} versículos del {label} sin interlineal")

    # Ningún léxico cubre absolutamente todo: H2007 (הֵנָּה, «ellas») no tiene
    # entrada propia en esta digitalización de BDB. Eso no es un fallo, así que
    # en vez de exigir el 100 % se vigila que la cobertura no se desplome, que
    # es lo que delataría una regresión de verdad.
    for collection, label, minimum in (
        ("at", "hebreas (Brown-Driver-Briggs)", 99.0),
        ("nt", "del NT (Abbott-Smith)", 99.0),
    ):
        pct = coverage(con, collection)
        if pct < minimum:
            problems.append(
                f"solo el {pct:.2f} % de las palabras {label} tiene artículo de"
                f" léxico (se esperaba más del {minimum:.0f} %)"
            )

    # Concatenar las palabras de un versículo debe devolver su texto exacto:
    # si no, alguna palabra quedaría emparejada con el análisis de otra.
    descuadre = con.execute(
        "SELECT COUNT(*) FROM ("
        "  SELECT v.id FROM verses v"
        "  JOIN books b ON b.id = v.book_id"
        "  JOIN words w ON w.verse_id = v.id"
        "  WHERE b.collection_id = 'nt'"
        "  GROUP BY v.id, v.text"
        "  HAVING GROUP_CONCAT(w.surface, ' ') <> v.text)"
    ).fetchone()[0]
    if descuadre:
        problems.append(
            f"{descuadre} versículos cuyo interlineal no reconstruye el texto"
        )

    return problems


def build(sources: Path, out: Path) -> None:
    if out.exists():
        out.unlink()
    out.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(out)
    con.executescript(SCHEMA)

    con.executemany(
        "INSERT INTO collections (id, name, short_name, edition, license, source_url,"
        " language, rtl, sort_order) VALUES (?,?,?,?,?,?,?,?,?)",
        [
            (
                "at",
                "Antiguo Testamento hebreo",
                "Hebreo",
                "Códice de Leningrado (Open Scriptures Hebrew Bible)",
                "CC BY 4.0 — openscriptures/morphhb",
                "https://github.com/openscriptures/morphhb",
                "hbo",
                1,
                1,
            ),
            (
                "lxx",
                "Septuaginta (Antiguo Testamento griego)",
                "Septuaginta",
                "H. B. Swete, Cambridge 1887–1912",
                "CC BY-SA 4.0 — First1KGreek / nathans/lxx-swete",
                "https://github.com/nathans/lxx-swete",
                "grc",
                0,
                2,
            ),
            (
                "nt",
                "Nuevo Testamento griego",
                "Nuevo Testamento",
                "Robinson–Pierpont, Texto Bizantino Mayoritario (2018)",
                "Dominio público (Unlicense)",
                "https://github.com/byztxt/byzantine-majority-text",
                "grc",
                0,
                3,
            ),
        ],
    )

    total = 0
    total_words = total_unaligned = 0

    print("Antiguo Testamento hebreo (Códice de Leningrado):")
    hebrew_words = hebrew_tagged = 0
    for order, (osis, code, name_es, name_he, alt) in enumerate(HEBREW_BOOKS, 1):
        n, w, seen = insert_hebrew(con, sources, order, osis, code, name_es, name_he, alt)
        total += n
        total_words += w
        hebrew_words += seen
        hebrew_tagged += w
        if n:
            print(f"  {name_es:32s} {n:5d} versículos  {w:6d} palabras")
    if hebrew_words:
        pct = 100 * hebrew_tagged / hebrew_words
        print(
            f"  interlineal hebreo: {hebrew_tagged} de {hebrew_words} palabras ({pct:.2f} %)."
            " El resto no lleva número Strong en OSHB (qere/ketiv y partículas sueltas)."
        )

    print("Septuaginta (Swete):")
    swete_dir = sources / "lxx-swete" / "data"
    grb_tsv = sources / "grb" / "grb.tsv"
    files = {}
    for f in sorted(swete_dir.glob("*.txt")):
        files[int(f.name.split(".", 1)[0])] = f

    for order, (num, (code, name_es, name_orig, alt)) in enumerate(sorted(LXX_BOOKS.items()), 1):
        note = None
        if num in files:
            verses = read_swete(files[num])
        elif num == 30 and grb_tsv.exists():
            # Swete aún no está transcrito para Eclesiastés en First1KGreek.
            verses = read_grb_book(grb_tsv, "Ecclesiastes")
            note = "Texto de tradición Rahlfs; Swete no disponible para este libro."
        else:
            print(f"  AVISO: sin fuente para {name_es} (archivo {num})")
            continue
        insert_book(con, "lxx", code, name_es, name_orig, alt, note, order, verses, scrub=True)
        total += len(verses)
        print(f"  {name_es:32s} {len(verses):5d} versículos" + ("  [Rahlfs]" if note else ""))

    print("Nuevo Testamento (Robinson–Pierpont):")
    byz_dir = sources / "byz" / "csv-unicode" / "ccat" / "no-variants"
    tagged_dir = sources / "byz" / "csv-unicode" / "strongs" / "with-parsing"
    for order, (src, code, name_es, name_orig) in enumerate(NT_BOOKS, 1):
        path = byz_dir / f"{src}.csv"
        if not path.exists():
            print(f"  AVISO: falta {path}")
            continue
        verses = read_byz_csv(path)
        book_id = insert_book(con, "nt", code, name_es, name_orig, None, None, order, verses)
        total += len(verses)

        tagged_path = tagged_dir / f"{src}.csv"
        words = unaligned = 0
        if book_id is not None and tagged_path.exists():
            words, unaligned = insert_words(con, book_id, read_tagged(tagged_path))
            total_words += words
            total_unaligned += unaligned
        aviso = f"  ({unaligned} sin alinear)" if unaligned else ""
        print(f"  {name_es:32s} {len(verses):5d} versículos  {words:6d} palabras{aviso}")

    print("Léxico y morfología:")
    lex = insert_lexicon(con, sources)
    hebrew_articles, greek_articles = insert_articles(con, sources)
    print(
        f"  Brown-Driver-Briggs               {hebrew_articles:5d} artículos"
        f"  ({coverage(con, 'at'):.2f} % de las palabras hebreas)"
    )
    print(
        f"  Abbott-Smith                      {greek_articles:5d} artículos"
        f"  ({coverage(con, 'nt'):.2f} % de las palabras del NT)"
    )

    print(f"  diccionarios Strong (gr. y heb.)  {lex:5d} entradas")

    # La lengua del código se decide por la colección del versículo, no por su
    # inicial: el griego tiene códigos que empiezan por A (adjetivo) y por H (HEB).
    hebrew_codes, greek_codes = set(), set()
    for morph, collection in con.execute(
        "SELECT DISTINCT w.morph, b.collection_id FROM words w"
        " JOIN verses v ON v.id = w.verse_id"
        " JOIN books b ON b.id = v.book_id"
    ):
        (hebrew_codes if collection == "at" else greek_codes).add(morph)

    table, unknown = build_table(greek_codes)

    # El hebreo no se reimplementa: OSHB publica la clave oficial de sus códigos.
    key = load_morph_key(sources / "morphhb" / "parsing" / "Oshm.xml")
    parts = build_part_key(key)
    missing_key = []
    for code in sorted(hebrew_codes):
        description = describe(code, key, parts)
        if description is None:
            missing_key.append(code)
            continue
        spanish, unresolved = translate(description)
        if spanish is None:
            unknown.extend(f"{code} ({' '.join(unresolved)})")
        else:
            table[code] = spanish

    con.executemany(
        "INSERT INTO morph_codes (code, description) VALUES (?,?)", sorted(table.items())
    )
    print(
        f"  códigos morfológicos              {len(table):5d} traducidos al español"
        f" ({len(greek_codes)} griegos, {len(hebrew_codes) - len(missing_key)} hebreos)"
    )
    if missing_key:
        print(f"  AVISO: {len(missing_key)} códigos hebreos fuera de la clave de OSHB:"
              f" {missing_key[:10]}")
    if unknown:
        print(f"  AVISO: {len(unknown)} códigos sin traducir: {unknown[:10]}")

    con.executemany(
        "INSERT INTO meta (key, value) VALUES (?,?)",
        [
            ("schema_version", "2"),
            ("verse_count", str(total)),
            ("word_count", str(total_words)),
            ("lexicon_count", str(lex)),
            ("built_by", "tools/build_db.py"),
        ],
    )
    con.commit()

    problems = verify(con)
    if problems:
        con.close()
        raise SystemExit(
            "La base no supera las comprobaciones de integridad:\n  - "
            + "\n  - ".join(problems)
        )
    print("  integridad del interlineal      correcta")

    con.execute("VACUUM")
    con.close()

    size_mb = out.stat().st_size / 1024 / 1024
    print(
        f"\nListo: {out} — {total} versículos, {total_words} palabras analizadas, "
        f"{size_mb:.1f} MB"
    )
    if total_unaligned:
        print(f"Aviso: {total_unaligned} versículos del NT quedaron sin interlineal.")
    if RESIDUAL:
        pct = 100 * RESIDUAL / total
        print(
            f"Aviso: {RESIDUAL} versículos ({pct:.2f} %) conservan palabras que el OCR de "
            "First1KGreek dejó truncadas o mezcladas con letras latinas. Son defectos de la "
            "transcripción de Swete aguas arriba, no de este importador."
        )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sources", type=Path, default=root / "build" / "sources")
    ap.add_argument("--out", type=Path, default=root / "app/src/main/assets/biblia.db")
    ap.add_argument("--no-clone", action="store_true", help="no clonar, usar lo que exista")
    args = ap.parse_args()

    if not args.no_clone:
        ensure_sources(args.sources)
    build(args.sources, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
