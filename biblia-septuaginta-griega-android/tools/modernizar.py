"""Ortografía de hoy para la Reina-Valera de 1909.

La 1909 está en dominio público, pero se escribió con las reglas de su tiempo:
«á» con tilde para la preposición, «fué», «dió», «vió», y «criar» en el sentido
de «crear». Quien la lee hoy lo toma por erratas —un tester señaló
Eclesiastés 12:1, «acuérdate de tu Criador»—, así que se pone al día.

Solo se toca la ortografía, nunca las palabras ni el orden: la revisión de 1960,
que es la que la gente tiene en el oído, es propiedad de las Sociedades Bíblicas
Unidas, y copiar sus cambios de redacción no está permitido. Lo que se hace
aquí es lo mismo que haría cualquier editor al reimprimir la 1909 con la
ortografía de la Real Academia, y el resultado sigue siendo la 1909.

«Criar» es el único caso que no es mecánico: en la 1909 vale tanto «crear»
(«en el principio crió Dios») como «criar» de hoy («crió su hijo hasta que lo
destetó»). Se cambia solo en los versículos donde es «crear», revisados uno a
uno, y en los demás se deja.
"""

from __future__ import annotations

import re

# Palabras con la tilde que la ortografía de 1909 ponía y la actual no.
TILDES = {
    "á": "a", "é": "e", "ó": "o", "ú": "u",
    "Á": "A", "É": "E", "Ó": "O", "Ú": "U",
    "fué": "fue", "Fué": "Fue", "fuí": "fui", "Fuí": "Fui",
    "dió": "dio", "Dió": "Dio", "vió": "vio", "Vió": "Vio",
    "ví": "vi", "Ví": "Vi", "dí": "di", "Dí": "Di",
    "pié": "pie", "piés": "pies", "hé": "he",
}

# Palabras que la Academia ya no admite en la forma de 1909.
FORMAS = {
    "priesa": "prisa", "Priesa": "Prisa",
    # «Criador» es siempre el Creador en la 1909: no hay otro sentido.
    "Criador": "Creador", "criador": "Creador",
}

# «Criar» por «crear»: (código USFX, capítulo, versículo) -> palabras que
# cambian en ese versículo. Todo lo que no está aquí es «criar» de hoy.
CREAR = {
    ("GEN", 1, 1): ["crió"],
    ("GEN", 1, 21): ["crió"],
    ("GEN", 1, 27): ["crió"],
    ("GEN", 2, 4): ["criados"],
    ("GEN", 5, 1): ["crió"],
    ("GEN", 5, 2): ["crió", "criados"],
    ("DEU", 4, 32): ["crió"],
    ("DEU", 32, 18): ["crió"],
    ("JOB", 26, 13): ["crió"],
    ("PSA", 89, 12): ["criaste"],
    ("PSA", 102, 18): ["criará"],
    ("PSA", 148, 5): ["criadas"],
    ("ISA", 4, 5): ["criará"],
    ("ISA", 40, 26): ["crió"],
    ("ISA", 40, 28): ["crió"],
    ("ISA", 41, 20): ["crió"],
    ("ISA", 43, 21): ["crié"],
    ("ISA", 45, 8): ["crié"],
    ("ISA", 45, 12): ["crié"],
    ("ISA", 45, 18): ["crió"],
    ("ISA", 48, 7): ["criadas"],
    ("ISA", 54, 16): ["crié"],
    ("JER", 31, 22): ["criará"],
    ("MAL", 2, 10): ["criado"],
    ("MRK", 13, 19): ["crió"],
    ("1CO", 11, 9): ["criado"],
    ("EPH", 2, 10): ["criados"],
    ("EPH", 3, 9): ["crió"],
    ("EPH", 4, 24): ["criado"],
    ("COL", 1, 16): ["criadas", "criado"],
    ("COL", 3, 10): ["crió"],
    ("1TI", 4, 3): ["crió"],
    ("1TI", 4, 4): ["crió"],
    ("HEB", 3, 4): ["crió"],
    ("REV", 4, 11): ["criaste", "criadas"],
    ("REV", 10, 6): ["criado"],
}

_CRIAR_A_CREAR = {
    "crió": "creó", "crié": "creé", "criaste": "creaste", "criará": "creará",
    "criado": "creado", "criados": "creados", "criadas": "creadas",
}

_PALABRA = re.compile(r"\w+")


def modernizar(texto: str, libro: str = "", capitulo: int = 0, versiculo: int = 0) -> str:
    """El texto de la 1909 con la ortografía de hoy. `libro` es el código USFX."""
    crear = set(CREAR.get((libro, capitulo, versiculo), ()))

    def cambiar(m: re.Match[str]) -> str:
        palabra = m.group()
        if palabra in crear:
            return _CRIAR_A_CREAR[palabra]
        return TILDES.get(palabra) or FORMAS.get(palabra) or palabra

    return _PALABRA.sub(cambiar, texto)
