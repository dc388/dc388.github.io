"""Saca de la base los datos que necesita la versión web.

La aplicación de Android lleva la base entera dentro y la consulta con SQLite.
En el navegador eso no vale: son 72 MB y nadie espera a que bajen para leer un
salmo. Aquí se parte en archivos pequeños —uno por capítulo— que el servidor
manda sueltos y el navegador guarda en su caché.

Se exporta el texto y el aparato de estudio: el análisis palabra por palabra
va en un archivo por capítulo, al lado del texto, y el léxico en cubos por
millar de número Strong, para que al tocar una palabra el navegador baje unos
cientos de kilobytes y no el diccionario entero.

    python3 tools/exportar_web.py ../biblia-web/datos
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import UTC, datetime
from pathlib import Path

import canonicidad

BASE = Path(__file__).resolve().parent.parent / "app/src/main/assets/biblia.db"


def exportar(destino: Path) -> None:
    con = sqlite3.connect(BASE)
    con.row_factory = sqlite3.Row
    destino.mkdir(parents=True, exist_ok=True)

    indice: list[dict] = []
    for col in con.execute(
        "SELECT id, name, short_name, edition, license, source_url, language, rtl"
        " FROM collections ORDER BY sort_order"
    ):
        libros = []
        for libro in con.execute(
            "SELECT id, code, name_es, name_orig, alt_name, source_note, chapter_list,"
            " verse_count FROM books WHERE collection_id = ? ORDER BY sort_order",
            (col["id"],),
        ):
            libros.append({
                "codigo": libro["code"],
                # canon o no, y según qué: la biblioteca agrupa por esto
                "canon": canonicidad.clase(col["id"], libro["code"]),
                "nombre": libro["name_es"],
                "original": libro["name_orig"],
                "alterno": libro["alt_name"],
                "nota": libro["source_note"],
                "capitulos": [int(c) for c in libro["chapter_list"].split(",")],
                "versiculos": libro["verse_count"],
            })
            # La carpeta lleva la colección delante porque los códigos se
            # repiten: «GEN» es Génesis en hebreo y también en la Septuaginta,
            # y son textos distintos. Sin esto uno pisaba al otro.
            exportar_libro(
                con, destino, libro["id"], col["id"], libro["code"], libro["chapter_list"]
            )

        indice.append({
            "id": col["id"],
            "nombre": col["name"],
            "corto": col["short_name"],
            "edicion": col["edition"],
            "licencia": col["license"],
            "fuente": col["source_url"],
            "lengua": col["language"],
            "rtl": bool(col["rtl"]),
            "libros": libros,
        })

    escribir(destino / "indice.json", indice)
    total = sum(len(c["libros"]) for c in indice)
    print(f"{len(indice)} colecciones, {total} libros")

    # Sello de la exportación. El navegador guarda en caché los archivos de
    # datos —que es lo que se quiere, porque son inmutables entre versiones—,
    # pero entonces una traducción nueva no le llega nunca. El lector lee este
    # sello sin caché y lo cuelga de las demás direcciones, así que al cambiar
    # la exportación cambian todas y se vuelven a pedir.
    escribir(destino / "version.json", {"sello": datetime.now(UTC).strftime("%Y%m%d%H%M%S")})

    exportar_lexico(con, destino)
    exportar_formas(con, destino)
    exportar_morfologia(con, destino)


def cubo(strong: str) -> str:
    """Cubo del léxico: la letra y el millar. G746 -> G0, G3056 -> G3."""
    letra, numero = strong[0], strong[1:]
    return f"{letra}{int(numero) // 1000}"


def exportar_lexico(con: sqlite3.Connection, destino: Path) -> None:
    """El diccionario, repartido en cubos por millar.

    Un archivo por entrada serían catorce mil archivos, que hacen lenta la
    publicación del sitio; uno solo obligaría a bajar el diccionario entero
    para mirar una palabra. Por millar salen una veintena de archivos de unos
    cientos de kilobytes: se baja el cubo la primera vez y ya queda en caché.
    """
    entradas: dict[str, dict] = {}
    for f in con.execute(
        "SELECT strong, lemma, translit, derivation_es, definition, definition_es,"
        " kjv_usage FROM lexicon"
    ):
        entradas[f["strong"]] = {
            "lema": f["lemma"],
            "translit": f["translit"],
            "origen": f["derivation_es"],
            "definicion": f["definition"],
            "definicion_es": f["definition_es"],
            "usos": f["kjv_usage"],
        }

    for f in con.execute("SELECT strong, homonym, gloss_es FROM glosario"):
        e = entradas.setdefault(f["strong"], {})
        e.setdefault("es", {})[f["homonym"]] = f["gloss_es"]

    for f in con.execute(
        "SELECT strong, homonym, source, headword, gloss, pos, article,"
        " article_es FROM articles"
    ):
        e = entradas.setdefault(f["strong"], {})
        e.setdefault("articulos", {})[f["homonym"]] = {
            "fuente": f["source"],
            "entrada": f["headword"],
            "glosa": f["gloss"],
            "categoria": f["pos"],
            "texto": f["article"],
            "texto_es": f["article_es"],
        }

    cubos: dict[str, dict] = {}
    for strong, datos in entradas.items():
        cubos.setdefault(cubo(strong), {})[strong] = datos
    carpeta = destino / "lexico"
    carpeta.mkdir(parents=True, exist_ok=True)
    for nombre, datos in cubos.items():
        escribir(carpeta / f"{nombre}.json", datos)
    print(f"  léxico: {len(entradas)} entradas en {len(cubos)} cubos")


def exportar_formas(con: sqlite3.Connection, destino: Path) -> None:
    """El puente de formas del Nuevo Testamento, para el griego sin analizar.

    Se reparte por la primera letra de la forma ya normalizada, que es como la
    busca el lector.
    """
    cubos: dict[str, dict] = {}
    for f in con.execute("SELECT form, strong, morph, n FROM nt_forms ORDER BY form, n DESC"):
        inicial = f["form"][0]
        cubos.setdefault(inicial, {}).setdefault(f["form"], []).append(
            [f["strong"], f["morph"]]
        )
    carpeta = destino / "formas"
    carpeta.mkdir(parents=True, exist_ok=True)
    for inicial, datos in cubos.items():
        escribir(carpeta / f"{ord(inicial)}.json", datos)
    print(f"  formas del NT: {sum(len(d) for d in cubos.values())} en {len(cubos)} cubos")


def exportar_morfologia(con: sqlite3.Connection, destino: Path) -> None:
    """Los códigos morfológicos ya traducidos al español."""
    codigos = {f["code"]: f["description"] for f in con.execute(
        "SELECT code, description FROM morph_codes")}
    escribir(destino / "morfologia.json", codigos)
    print(f"  morfología: {len(codigos)} códigos")


def exportar_libro(
    con: sqlite3.Connection,
    destino: Path,
    libro_id: int,
    coleccion: str,
    codigo: str,
    capitulos: str,
) -> None:
    carpeta = destino / coleccion / codigo
    carpeta.mkdir(parents=True, exist_ok=True)
    for numero in (int(c) for c in capitulos.split(",")):
        versiculos = []
        for fila in con.execute(
            "SELECT v.verse, v.suffix, v.text, t.text AS espanol"
            " FROM verses v"
            " LEFT JOIN translation t"
            "   ON t.book_id = v.book_id AND t.chapter = v.chapter"
            "  AND t.verse = v.verse AND t.suffix = v.suffix"
            " WHERE v.book_id = ? AND v.chapter = ?"
            " ORDER BY v.verse, v.suffix",
            (libro_id, numero),
        ):
            entrada = {"v": fila["verse"], "t": fila["text"]}
            if fila["suffix"]:
                entrada["s"] = fila["suffix"]
            # La Reina-Valera solo cubre el hebreo y el Nuevo Testamento; en el
            # resto la clave sencillamente no va, y así no pesa.
            if fila["espanol"]:
                entrada["es"] = fila["espanol"]
            versiculos.append(entrada)
        escribir(carpeta / f"{numero}.json", versiculos)
        exportar_palabras(con, carpeta, libro_id, numero)


def exportar_palabras(
    con: sqlite3.Connection, carpeta: Path, libro_id: int, capitulo: int
) -> None:
    """El análisis palabra por palabra, en su propio archivo.

    Va aparte del texto para que quien solo lee no cargue con él: pesa más que
    el texto y la mayoría de las visitas no lo abren.
    """
    palabras: dict[str, list] = {}
    for f in con.execute(
        "SELECT v.verse, v.suffix, w.position, w.surface, w.strong, w.homonym, w.morph"
        " FROM words w JOIN verses v ON v.id = w.verse_id"
        " WHERE v.book_id = ? AND v.chapter = ?"
        " ORDER BY v.verse, v.suffix, w.position",
        (libro_id, capitulo),
    ):
        clave = f"{f['verse']}{f['suffix']}"
        palabras.setdefault(clave, []).append(
            [f["surface"], f["strong"], f["homonym"], f["morph"]]
        )
    # Sin análisis no se escribe nada: el lector pide el archivo y, si no está,
    # cae al puente de formas del Nuevo Testamento. Así la Septuaginta, los
    # Padres y los pseudoepígrafos no se llenan de archivos vacíos.
    if palabras:
        escribir(carpeta / f"{capitulo}.palabras.json", palabras)


def escribir(ruta: Path, datos: object) -> None:
    # Sin espacios entre las claves: en 1 400 archivos, cada byte se nota.
    ruta.write_text(
        json.dumps(datos, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def main() -> int:
    destino = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("../biblia-web/datos")
    if not BASE.exists():
        print(f"Falta la base: {BASE}. Ejecuta antes tools/build_db.py")
        return 1
    exportar(destino.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
