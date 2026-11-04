"""Mira la credencial de Play antes de usarla.

Sin esto, una clave cortada al pegarla o la clave equivocada se descubren
cuando la API contesta un 400 sin explicar nada, cuatro minutos después de
empezar a compilar. Aquí se dice qué le falta y se acaba.

El JSON llega por la entrada estándar, nunca por la línea de órdenes: lo que
se pasa como argumento sale en el registro de procesos de la máquina. No se
imprime ningún trozo de la credencial, solo el motivo del fallo.
"""
import json
import sys

OBLIGATORIOS = ("client_email", "private_key", "token_uri")


def comprobar(texto):
    """Devuelve el motivo por el que la credencial no sirve, o None si sirve."""
    if not texto.strip():
        return "está vacía"
    try:
        cuenta = json.loads(texto)
    except ValueError as error:
        return f"no es JSON válido ({error})"
    if not isinstance(cuenta, dict):
        return "no es un objeto JSON"
    if cuenta.get("type") != "service_account":
        return (
            "no es la clave de una cuenta de servicio: le falta "
            '«"type": "service_account"». ¿Pegaste el identificador de cliente '
            "de OAuth en vez del archivo de la cuenta de servicio?"
        )
    faltan = [campo for campo in OBLIGATORIOS if not cuenta.get(campo)]
    if faltan:
        return "le faltan estos campos: " + ", ".join(faltan)
    if "BEGIN PRIVATE KEY" not in cuenta["private_key"]:
        return "el campo private_key no contiene una clave; llegó cortado"
    return None


def main():
    motivo = comprobar(sys.stdin.read())
    if motivo:
        print(f"La credencial de Play no sirve: {motivo}", file=sys.stderr)
        return 1
    print("La credencial de Play tiene todas sus piezas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
