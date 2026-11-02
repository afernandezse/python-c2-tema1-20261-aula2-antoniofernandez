"""
Enunciado:
Incorporación de cajas de alerta o admonitions (parte en Python).

Una vez hayas completado "notas.md" con las admonitions "!!! note" y
"!!! warning", implementa en este módulo la función:

1. "admonitions": devuelve un diccionario {tipo: contenido} con el
   contenido (sin indentar) de cada admonition de la página, usando como
   clave el tipo ("note", "warning", etc.).
"""

import os
import re
from typing import Dict

EJ_DIR = os.path.dirname(__file__)
NOTAS_PATH = os.path.join(EJ_DIR, "notas.md")


def admonitions(ruta: str = NOTAS_PATH) -> Dict[str, str]:
    """Devuelve el contenido de cada admonition de la página."""

    content = {}

    with open(ruta, "r", encoding="utf-8") as f:
        text = f.read()

    admonition_pattern = r"^!!![ \t]+(\w+)[ \t]*\n((?:[ ]{4}.*(?:\n|$))+)"

    matches = re.findall(admonition_pattern, text, re.MULTILINE)

    for tipo, bloque in matches:
        contenido = "\n".join(
            linea[4:] for linea in bloque.splitlines()
        ).strip()

        content[tipo] = contenido

    return content


if __name__ == "__main__":
    print("Admonitions:", admonitions())
