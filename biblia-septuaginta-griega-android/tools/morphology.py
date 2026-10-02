"""Traduce a español los códigos morfológicos de Robinson del Nuevo Testamento.

Los códigos vienen en el etiquetado de byztxt con esta forma:

    V-2AAI-3S   verbo, segundo aoristo activo indicativo, 3ª persona singular
    N-DSF       sustantivo, dativo singular femenino
    S-1SASF     posesivo de 1ª persona singular, acusativo singular femenino
    ADV-C       adverbio comparativo
    V-RAI-3S-ATT  perfecto activo indicativo 3ª sing., forma ática

`decode` devuelve la descripción en español o None si no reconoce el código;
`build_table` recorre un corpus y avisa de todo lo que no supo traducir, para
que nunca se muestre al usuario una etiqueta inventada.
"""

from __future__ import annotations

POS = {
    "N": "sustantivo",
    "A": "adjetivo",
    "T": "artículo",
    "V": "verbo",
    "P": "pronombre personal",
    "R": "pronombre relativo",
    "C": "pronombre recíproco",
    "D": "pronombre demostrativo",
    "K": "pronombre correlativo",
    "I": "pronombre interrogativo",
    "X": "pronombre indefinido",
    "Q": "pronombre correlativo o interrogativo",
    "F": "pronombre reflexivo",
    "S": "pronombre posesivo",
    "ADV": "adverbio",
    "CONJ": "conjunción",
    "COND": "partícula condicional",
    "PRT": "partícula",
    "PREP": "preposición",
    "INJ": "interjección",
    "ARAM": "voz aramea",
    "HEB": "voz hebrea",
}

CASE = {"N": "nominativo", "G": "genitivo", "D": "dativo", "A": "acusativo", "V": "vocativo"}
NUMBER = {"S": "singular", "P": "plural"}
GENDER = {"M": "masculino", "F": "femenino", "N": "neutro"}

TENSE = {
    "P": "presente",
    "I": "imperfecto",
    "F": "futuro",
    "A": "aoristo",
    "R": "perfecto",
    "L": "pluscuamperfecto",
}
VOICE = {
    "A": "activa",
    "M": "media",
    "P": "pasiva",
    "E": "media o pasiva",
    "D": "media deponente",
    "O": "pasiva deponente",
    "N": "media o pasiva deponente",
}
MOOD = {
    "I": "indicativo",
    "S": "subjuntivo",
    "O": "optativo",
    "M": "imperativo",
    "N": "infinitivo",
    "P": "participio",
}
PERSON = {"1": "1ª persona", "2": "2ª persona", "3": "3ª persona"}

# Sufijos que pueden cerrar cualquier código.
SUFFIX = {
    "ATT": "forma ática",
    "C": "comparativo",
    "S": "superlativo",
    "N": "negativo",
    "I": "interrogativo",
    "K": "correlativo",
    "ABB": "abreviado",
}

# Códigos indeclinables, que no llevan caso ni género.
INDECLINABLE = {
    "PRI": "nombre propio indeclinable",
    "NUI": "numeral indeclinable",
    "LI": "letra indeclinable",
    "OI": "indeclinable de otro tipo",
}


def _nominal(spec: str) -> str | None:
    """`NSM` -> «nominativo singular masculino»; `1NS` -> «1ª persona nominativo singular»."""
    if spec in INDECLINABLE:
        return INDECLINABLE[spec]

    if len(spec) == 3 and spec[0] in PERSON:
        # pronombre con persona: persona + caso + número
        person, case, number = spec
        if case in CASE and number in NUMBER:
            return f"{PERSON[person]} {CASE[case]} {NUMBER[number]}"
        return None

    if len(spec) == 4 and spec[0] in PERSON:
        # reflexivo: persona + caso + número + género
        person, case, number, gender = spec
        if case in CASE and number in NUMBER and gender in GENDER:
            return f"{PERSON[person]} {CASE[case]} {NUMBER[number]} {GENDER[gender]}"
        return None

    if len(spec) == 3:
        case, number, gender = spec
        if case in CASE and number in NUMBER and gender in GENDER:
            return f"{CASE[case]} {NUMBER[number]} {GENDER[gender]}"
        return None

    if len(spec) == 5 and spec[0] in PERSON and spec[1] in NUMBER:
        # posesivo: persona y número del poseedor + caso, número y género de lo poseído
        owner = f"{PERSON[spec[0]]} {NUMBER[spec[1]]}"
        thing = _nominal(spec[2:])
        return f"{owner}, {thing}" if thing else None

    return None


def _verb(tvm: str, rest: list[str]) -> str | None:
    second = False
    if tvm.startswith("2"):
        second, tvm = True, tvm[1:]
    if len(tvm) != 3:
        return None
    tense, voice, mood = tvm
    if tense not in TENSE or voice not in VOICE or mood not in MOOD:
        return None

    tense_name = f"segundo {TENSE[tense]}" if second else TENSE[tense]
    parts = [tense_name, f"voz {VOICE[voice]}", MOOD[mood]]

    if rest:
        spec = rest[0]
        if len(spec) == 2 and spec[0] in PERSON and spec[1] in NUMBER:
            parts.append(f"{PERSON[spec[0]]} {NUMBER[spec[1]]}")
        else:
            nominal = _nominal(spec)
            if nominal is None:
                return None
            parts.append(nominal)

    return ", ".join(parts)


def decode(code: str) -> str | None:
    """Devuelve la glosa española del código, o None si no se reconoce."""
    if not code:
        return None

    parts = code.split("-")
    pos = parts[0]
    if pos not in POS:
        return None

    rest = parts[1:]
    suffix = None
    if rest and rest[-1] in SUFFIX and not (pos == "V" and len(rest) == 1):
        suffix = SUFFIX[rest[-1]]
        rest = rest[:-1]

    if pos == "V":
        if not rest:
            return None
        body = _verb(rest[0], rest[1:])
    elif not rest:
        body = POS[pos]
    else:
        nominal = _nominal(rest[0])
        if nominal is None:
            return None
        body = f"{POS[pos]}, {nominal}"

    if body is None:
        return None
    if pos == "V":
        body = f"{POS[pos]}, {body}"
    return f"{body}, {suffix}" if suffix else body


def build_table(codes: set[str]) -> tuple[dict[str, str], list[str]]:
    """Devuelve (código -> glosa) y la lista de códigos no reconocidos."""
    table, unknown = {}, []
    for code in sorted(codes):
        glossed = decode(code)
        if glossed:
            table[code] = glossed
        else:
            unknown.append(code)
    return table, unknown
