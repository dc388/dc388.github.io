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

Uso:
    python3 tools/build_db.py                 # clona las fuentes si hacen falta
    python3 tools/build_db.py --sources /ruta # reutiliza clones existentes
"""

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clean import clean_text, count_residual  # noqa: E402

REPOS = {
    "lxx-swete": "https://github.com/nathans/lxx-swete.git",
    "byz": "https://github.com/byztxt/byzantine-majority-text.git",
    "grb": "https://github.com/LukeSmithxyz/grb.git",
}

# --- Septuaginta: numero de archivo de Swete -> (codigo, nombre es, nombre gr, alterno)
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

# --- Nuevo Testamento: archivo CSV de byztxt -> (codigo, nombre es, nombre gr)
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
    sort_order  INTEGER NOT NULL
);
CREATE TABLE books (
    id             INTEGER PRIMARY KEY,
    collection_id  TEXT NOT NULL REFERENCES collections(id),
    code           TEXT NOT NULL,
    name_es        TEXT NOT NULL,
    name_gr        TEXT NOT NULL,
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
CREATE INDEX idx_verses_loc  ON verses(book_id, chapter, verse, suffix);
CREATE INDEX idx_books_order ON books(collection_id, sort_order);
"""

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
    name_gr: str,
    alt_name: str | None,
    source_note: str | None,
    order: int,
    verses: list[tuple[int, int, str, str]],
    scrub: bool = False,
) -> int:
    if not verses:
        return 0
    chapters = len({c for c, _, _, _ in verses})
    cur = con.execute(
        "INSERT INTO books (collection_id, code, name_es, name_gr, alt_name, source_note,"
        " sort_order, chapter_count, verse_count) VALUES (?,?,?,?,?,?,?,?,?)",
        (collection, code, name_es, name_gr, alt_name, source_note, order, chapters, len(verses)),
    )
    book_id = cur.lastrowid
    prepared = [(c, v, s, prepare(t, scrub)) for (c, v, s, t) in verses]
    con.executemany(
        "INSERT INTO verses (book_id, chapter, verse, suffix, text, text_norm)"
        " VALUES (?,?,?,?,?,?)",
        [(book_id, c, v, s, t, normalize(t)) for (c, v, s, t) in prepared],
    )
    globals()["RESIDUAL"] += sum(1 for (_, _, _, t) in prepared if count_residual(t))
    return len(verses)


def build(sources: Path, out: Path) -> None:
    if out.exists():
        out.unlink()
    out.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(out)
    con.executescript(SCHEMA)

    con.executemany(
        "INSERT INTO collections (id, name, short_name, edition, license, source_url, sort_order)"
        " VALUES (?,?,?,?,?,?,?)",
        [
            (
                "lxx",
                "Septuaginta (Antiguo Testamento griego)",
                "Septuaginta",
                "H. B. Swete, Cambridge 1887–1912",
                "CC BY-SA 4.0 — First1KGreek / nathans/lxx-swete",
                "https://github.com/nathans/lxx-swete",
                1,
            ),
            (
                "nt",
                "Nuevo Testamento griego",
                "Nuevo Testamento",
                "Robinson–Pierpont, Texto Bizantino Mayoritario (2018)",
                "Dominio público (Unlicense)",
                "https://github.com/byztxt/byzantine-majority-text",
                2,
            ),
        ],
    )

    total = 0
    print("Septuaginta (Swete):")
    swete_dir = sources / "lxx-swete" / "data"
    grb_tsv = sources / "grb" / "grb.tsv"
    files = {}
    for f in sorted(swete_dir.glob("*.txt")):
        files[int(f.name.split(".", 1)[0])] = f

    for order, (num, (code, name_es, name_gr, alt)) in enumerate(sorted(LXX_BOOKS.items()), 1):
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
        n = insert_book(con, "lxx", code, name_es, name_gr, alt, note, order, verses, scrub=True)
        total += n
        print(f"  {name_es:32s} {n:5d} versículos" + ("  [Rahlfs]" if note else ""))

    print("Nuevo Testamento (Robinson–Pierpont):")
    byz_dir = sources / "byz" / "csv-unicode" / "ccat" / "no-variants"
    for order, (src, code, name_es, name_gr) in enumerate(NT_BOOKS, 1):
        path = byz_dir / f"{src}.csv"
        if not path.exists():
            print(f"  AVISO: falta {path}")
            continue
        verses = read_byz_csv(path)
        n = insert_book(con, "nt", code, name_es, name_gr, None, None, order, verses)
        total += n
        print(f"  {name_es:32s} {n:5d} versículos")

    con.executemany(
        "INSERT INTO meta (key, value) VALUES (?,?)",
        [
            ("schema_version", "1"),
            ("verse_count", str(total)),
            ("built_by", "tools/build_db.py"),
        ],
    )
    con.commit()
    con.execute("VACUUM")
    con.close()

    size_mb = out.stat().st_size / 1024 / 1024
    print(f"\nListo: {out} — {total} versículos, {size_mb:.1f} MB")
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
