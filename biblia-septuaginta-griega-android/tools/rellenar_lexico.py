#!/usr/bin/env python3
"""Rellena la glosa española del diccionario: la que se ve al tocar una palabra.

Cuando tocas una palabra en el lector, lo primero que sale es el renglón del
lema: la palabra griega o hebrea, su transliteración y una glosa corta en
español. Esa glosa vive en el campo `es` del léxico y solo la tenían 1184 de
14197 entradas: en el 92 % de las palabras el renglón salía cojo.

La materia prima estaba ahí sin usar. Cada artículo de Brown-Driver-Briggs y de
Abbott-Smith trae su glosa corta en inglés —«a wall», «to overturn»—, que es
exactamente lo que hace falta. Este módulo las pasa por el traductor de
traducir_strong.py.

Lo que NO se traduce, y por qué
-------------------------------

El traductor resuelve palabra a palabra, y eso con el inglés lexicográfico
funciona bien hasta que aparecen tres cosas. Se midieron sobre las 10 237
glosas que el traductor aceptaba, y se descartan las tres:

1. Verbos con partícula. «to take out» no es «tomar fuera», es «sacar»;
   «worn out» no es «gastado fuera». Palabra a palabra salen disparates que
   además suenan convincentes. Cualquier glosa con una de esas partículas se
   descarta entera.

2. Glosas largas. A partir de tres palabras de contenido la sintaxis inglesa
   deja de calcar bien: «a place of safe keeping» salía «un lugar de seguro
   guardar». El corte está en dos palabras de contenido, sin contar artículos
   ni preposiciones.

3. Nombres propios solos. «Ithamar» se quedaba «Ithamar» donde el español
   escribe «Itamar». Y no se pierde nada quitándolos: la definición de Strong,
   que va justo debajo y sí está traducida entera, ya dice «Arab, un lugar de
   Palestina».

Se descarta además el patrón «to X» que sale como «a X», que es el traductor
tomando el verbo por sustantivo, y se cortan los remites editoriales del léxico
(«Kabzeel. Compare») que no son parte de la glosa.

De 10 237 glosas que el traductor daba por buenas, pasan 6 009. Las otras 4 228
no se escriben: más vale un hueco, que se ve, que una glosa inventada, que no.

Tampoco se pisa lo que ya estaba: las glosas que ya tenían español vienen de
otra parte y se respetan.

Lo que queda fuera del alcance de esto: la concordancia de género («a female
disciple» sale «un discípulo femenino») y ser/estar («be sick» sale «ser
enfermo» donde toca «estar enfermo»). Son pocas y para arreglarlas hace falta
análisis sintáctico, no una tabla.

    python3 rellenar_lexico.py [ruta-a-biblia/datos]

Trabaja sobre el léxico ya publicado en la web, igual que rellenar_web.py, para
no necesitar la base de datos. La aplicación de Android lo recoge en la
siguiente reconstrucción de biblia.db.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from traducir_strong import traducir

PARTICULAS = {
    "out", "forth", "off", "down", "up", "back", "through", "together", "away",
    "over", "under", "about", "along", "around", "aside", "apart", "upon", "on",
    "into", "onto", "beforehand", "besides", "behind", "beyond", "within", "without",
}

# Palabras que no cuentan para medir cuánto dice una glosa.
VACIAS = {"to", "a", "an", "the", "of", "or", "and", "in"}

# «Kabzeel. Compare», «Ornan. See»: remite del léxico, no glosa.
REMITE = re.compile(r"\s*[.,;]?\s*\b(?:Compare|See|Cf|cf)\b.*$", re.I)

SOLO_NOMBRE = re.compile(r"[A-ZÁÉÍÓÚÑ][\w'’\-]*(?:\s+[A-ZÁÉÍÓÚÑ][\w'’\-]*)*\s*")


def utilizable(glosa: str) -> str | None:
    """Devuelve la glosa lista para traducir, o None si no conviene tocarla."""
    limpia = REMITE.sub("", glosa).strip(" .,;")
    if not limpia:
        return None
    if SOLO_NOMBRE.fullmatch(limpia):
        return None
    piezas = [w.lower() for w in re.findall(r"[A-Za-z]+", limpia)]
    if any(w in PARTICULAS for w in piezas):
        return None
    if len([w for w in piezas if w not in VACIAS]) > 2:
        return None
    return limpia


def rellena(carpeta: pathlib.Path) -> None:
    lexico = carpeta / "lexico"
    if not lexico.is_dir():
        sys.exit(f"no encuentro {lexico}")

    entradas = antes = puestas = respetadas = 0
    descartadas = {"no traducible": 0, "descartada por las reglas": 0, "infinitivo torcido": 0}
    tocados = 0

    for archivo in sorted(lexico.glob("*.json")):
        cubo = json.loads(archivo.read_text(encoding="utf-8"))
        cambiado = False

        for entrada in cubo.values():
            entradas += 1
            es = entrada.get("es") or {}
            tenia = bool(es)
            if tenia:
                antes += 1

            for hom, articulo in (entrada.get("articulos") or {}).items():
                if es.get(hom):
                    respetadas += 1
                    continue
                glosa = articulo.get("glosa")
                if not glosa:
                    continue
                buena = utilizable(glosa)
                if buena is None:
                    descartadas["descartada por las reglas"] += 1
                    continue
                espanol = traducir(buena)
                if not espanol:
                    descartadas["no traducible"] += 1
                    continue
                # «to X» que sale «a X» es el traductor tomando el verbo por
                # sustantivo: «to want further» → «a carecer de además».
                if buena.lower().startswith("to ") and re.match(r"a\s", espanol):
                    descartadas["infinitivo torcido"] += 1
                    continue
                es[hom] = espanol
                puestas += 1
                cambiado = True

            if es and not tenia:
                entrada["es"] = es

        if cambiado:
            archivo.write_text(
                json.dumps(cubo, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
            tocados += 1

    ahora = sum(
        1
        for archivo in sorted(lexico.glob("*.json"))
        for entrada in json.loads(archivo.read_text(encoding="utf-8")).values()
        if entrada.get("es")
    )

    print(f"entradas del léxico              {entradas:>8,}")
    print(f"con glosa española antes         {antes:>8,}  ({100 * antes / entradas:.1f}%)")
    print(f"con glosa española ahora         {ahora:>8,}  ({100 * ahora / entradas:.1f}%)")
    print()
    print(f"glosas puestas                   {puestas:>8,}")
    print(f"glosas que ya estaban, intactas  {respetadas:>8,}")
    for razon, n in descartadas.items():
        print(f"sin poner: {razon:<22}{n:>8,}")
    print(f"archivos reescritos              {tocados:>8,}")


if __name__ == "__main__":
    ruta = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "biblia/datos")
    rellena(ruta)
