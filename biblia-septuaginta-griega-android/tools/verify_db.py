#!/usr/bin/env python3
"""Comprueba la integridad de la base ya versionada, sin reconstruirla.

Lo usa la CI: la base de datos está en el repositorio, así que conviene
verificar en cada push que sigue siendo coherente, no solo cuando se regenera.

    python3 tools/verify_db.py
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_db import verify  # noqa: E402


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    db = root / "app/src/main/assets/biblia.db"
    if not db.exists():
        print(f"No existe {db}; ejecuta tools/build_db.py", file=sys.stderr)
        return 1

    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    counts = {
        name: con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
        for name in (
            "collections", "books", "verses", "words", "lexicon", "articles",
            "morph_codes",
        )
    }
    problems = verify(con)
    con.close()

    for name, n in counts.items():
        print(f"  {name:14s} {n:7d}")

    if problems:
        print("\nFALLOS DE INTEGRIDAD:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("\nIntegridad correcta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
