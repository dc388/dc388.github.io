"""Las variantes textuales del Nuevo Testamento, atadas a su sitio del versículo.

El texto que publica la aplicación es el Bizantino Mayoritario de
Robinson-Pierpont. byztxt lo distribuye en dos formas, `no-variants` y
`with-variants`, y la segunda trae el aparato incrustado en la propia línea:

    Σαλμὼν δὲ ἐγέννησεν τὸν Βοὸζ {NA Βοὸζ ἐκ > Βόες ἐκ } ἐκ τῆς Ῥαχάβ·

Dentro de las llaves va la sigla de la edición que discrepa, la lectura
bizantina, una flecha y la lectura de esa otra edición. Un guion a la derecha
significa que allí la otra edición no lee nada: omite.

Quitando los bloques se recupera el texto corriente, y eso no es una
suposición: los 7 968 versículos de `with-variants`, limpios de llaves,
coinciden carácter por carácter con los de `no-variants`, que es de donde sale
lo que la aplicación ya muestra. Por eso cada variante se puede colgar de su
posición exacta sin alinear nada a ojo.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

# Una marca que no aparece en el texto griego, para no perder la posición del
# bloque cuando se normalizan los espacios.
_MARCA = ""
_BLOQUE = re.compile(r"\{([^}]*)\}")
_MARCADA = re.compile(_MARCA + r"(\d+)" + _MARCA)

# «{NA ~}» sin flecha: la otra edición pone las mismas palabras en otro orden.
_TRANSPOSICION = "~"


@dataclass(frozen=True)
class Variante:
    """Una discrepancia entre el texto bizantino y otra edición."""

    posicion: int        # desplazamiento en caracteres dentro del versículo limpio
    fin: int             # final del tramo al que afecta, para poder subrayarlo
    sigla: str           # NA, NA28, Byz, ECM...
    bizantino: str       # lo que lee el texto que mostramos
    otra: str            # lo que lee la otra edición; vacío si omite
    transpone: bool      # sólo cambia el orden de las palabras


def _limpiar(texto: str) -> str:
    """La misma normalización que build_db aplica al guardar el versículo."""
    texto = texto.replace("¶", "").replace(" ", " ")
    return re.sub(r"\s+", " ", texto).strip()


def _partir(cuerpo: str) -> tuple[str, str, str, bool] | None:
    """De «NA Βοὸζ ἐκ > Βόες ἐκ» saca la sigla y las dos lecturas."""
    cuerpo = cuerpo.strip()
    if not cuerpo:
        return None
    sigla, _, resto = cuerpo.partition(" ")
    resto = resto.strip()
    if resto == _TRANSPOSICION:
        return sigla, "", "", True
    izquierda, flecha, derecha = resto.partition(">")
    if not flecha:
        return None
    izquierda, derecha = izquierda.strip(), derecha.strip()
    # El guion marca la omisión: allí la otra edición no lee nada.
    if derecha == "-":
        derecha = ""
    if izquierda == "-":
        izquierda = ""
    return sigla, izquierda, derecha, False


def extraer(texto: str) -> tuple[str, list[Variante]]:
    """Devuelve el versículo limpio y las variantes con su posición dentro de él."""
    cuerpos: list[str] = []

    def guardar(m: re.Match[str]) -> str:
        cuerpos.append(m.group(1))
        return _MARCA + str(len(cuerpos) - 1) + _MARCA

    marcado = _limpiar(_BLOQUE.sub(guardar, texto))

    # Se recorre de izquierda a derecha restando lo que ya se ha quitado, que es
    # la única forma de que la posición siga valiendo sobre el texto final.
    limpio_partes: list[str] = []
    variantes: list[Variante] = []
    ultimo = 0
    largo = 0
    for m in _MARCADA.finditer(marcado):
        trozo = marcado[ultimo:m.start()]
        limpio_partes.append(trozo)
        largo += len(trozo)
        partido = _partir(cuerpos[int(m.group(1))])
        if partido is not None:
            sigla, bizantino, otra, transpone = partido
            variantes.append(
                Variante(largo, largo, sigla, bizantino, otra, transpone))
        ultimo = m.end()
    limpio_partes.append(marcado[ultimo:])

    # Al quitar las marcas quedan espacios dobles donde el bloque iba suelto.
    limpio = "".join(limpio_partes)
    apretado = re.sub(r"\s+", " ", limpio).strip()
    return apretado, _recolocar(apretado, variantes)


# La puntuación del texto corrido no está en el lema del aparato: el bloque dice
# «ἡμῶν Ἰησοῦ χριστοῦ συναχθέντων» y el versículo lleva una coma en medio. Por
# eso la lectura no se busca tal cual, sino sobre una copia sin más que letras y
# espacios, con un índice que devuelve cada letra a su sitio en el original.
_SOLO_LETRAS = re.compile(r"[^\w\s]", re.UNICODE)


def _desnudar(texto: str) -> tuple[str, list[int]]:
    """El texto sin puntuación, y de qué posición del original sale cada carácter."""
    piezas: list[str] = []
    indices: list[int] = []
    espacio = True
    for i, c in enumerate(texto):
        if c.isspace():
            if not espacio:
                piezas.append(" ")
                indices.append(i)
                espacio = True
            continue
        if _SOLO_LETRAS.fullmatch(c):
            continue
        piezas.append(c)
        indices.append(i)
        espacio = False
    return "".join(piezas), indices


def _recolocar(texto: str, variantes: list[Variante]) -> list[Variante]:
    """Sitúa cada variante sobre la lectura bizantina que le corresponde."""
    desnudo, indices = _desnudar(texto)
    salida: list[Variante] = []
    desde = 0
    for v in variantes:
        if not v.bizantino:
            # Omisión o transposición: no hay lectura que subrayar, la marca se
            # queda donde la puso la edición.
            tope = min(v.posicion, len(texto))
            salida.append(Variante(tope, tope, v.sigla, v.bizantino, v.otra, v.transpone))
            continue
        aguja, _ = _desnudar(v.bizantino)
        i = desnudo.find(aguja, desde)
        if i < 0:                       # puede repetirse antes del punto de partida
            i = desnudo.find(aguja)
        if i < 0:
            tope = min(v.posicion, len(texto))
            salida.append(Variante(tope, tope, v.sigla, v.bizantino, v.otra, v.transpone))
            continue
        ini = indices[i]
        fin = indices[i + len(aguja) - 1] + 1
        salida.append(Variante(ini, fin, v.sigla, v.bizantino, v.otra, v.transpone))
        desde = i + len(aguja)
    return salida


def leer(path: Path) -> dict[tuple[int, int], tuple[str, list[Variante]]]:
    """Lee un CSV de `with-variants` y devuelve {(capítulo, versículo): (texto, variantes)}."""
    salida: dict[tuple[int, int], tuple[str, list[Variante]]] = {}
    with open(path, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            clave = (int(fila["chapter"]), int(fila["verse"]))
            salida[clave] = extraer(fila["text"])
    return salida


# --- comprobación -----------------------------------------------------------
# Se ejecuta sola: `python3 tools/variantes.py /ruta/a/byz`. Comprueba las dos
# cosas de las que depende todo lo demás —que el texto limpio sea el que la
# aplicación ya publica, y que cada lectura bizantina caiga donde dice su
# posición— porque si alguna de las dos deja de ser verdad, lo que se subraya
# en pantalla deja de ser lo que el aparato dice.

NT = (
    "MAT MAR LUK JOH ACT ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH 1TI 2TI TIT PHM "
    "HEB JAM 1PE 2PE 1JO 2JO 3JO JUD REV"
).split()


def _sin_puntuacion(texto: str) -> str:
    return _desnudar(texto)[0]


def comprobar(raiz: Path) -> int:
    base = raiz / "csv-unicode" / "ccat"
    vers = distintos = total = ancladas = sueltas = perdidas = 0
    fallos: list[str] = []
    for libro in NT:
        con_var = base / "with-variants" / f"{libro}.csv"
        sin_var = base / "no-variants" / f"{libro}.csv"
        if not con_var.exists() or not sin_var.exists():
            print(f"  AVISO: falta {libro}")
            continue
        with open(sin_var, encoding="utf-8") as f:
            publicado = {
                (int(r["chapter"]), int(r["verse"])): _limpiar(r["text"])
                for r in csv.DictReader(f)
            }
        for clave, (texto, variantes) in leer(con_var).items():
            vers += 1
            if publicado.get(clave) != texto:
                distintos += 1
                fallos.append(f"{libro} {clave}: el texto limpio no es el publicado")
            for v in variantes:
                total += 1
                if not v.bizantino:
                    sueltas += 1
                elif _sin_puntuacion(texto[v.posicion:v.fin]) == _sin_puntuacion(v.bizantino):
                    ancladas += 1
                else:
                    perdidas += 1
                    fallos.append(f"{libro} {clave}: no se halló «{v.bizantino[:40]}»")
    print(f"versículos {vers}   texto distinto al publicado: {distintos}")
    print(f"variantes {total}   ancladas {ancladas}   "
          f"omiten o transponen {sueltas}   sin anclar {perdidas}")
    for f in fallos[:10]:
        print("   ", f)
    # Las discontinuas («ἐν... ἐν... ἐν») y la nota de capítulo de Ro 14 no se
    # pueden anclar a un tramo: son cuatro y están contadas, no escondidas.
    return 1 if distintos or perdidas > 4 else 0


if __name__ == "__main__":
    import sys

    raise SystemExit(comprobar(Path(sys.argv[1])))
