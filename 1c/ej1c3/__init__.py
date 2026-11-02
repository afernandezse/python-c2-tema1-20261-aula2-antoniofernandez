"""
Enunciado:
Integración de la referencia automática de la API (parte en Python).

Una vez hayas completado "api.md" con las directivas de mkdocstrings,
implementa en este módulo la función:

1. "modulos_referenciados": devuelve la lista de nombres de módulo
   referenciados mediante directivas "::: nombre_del_modulo" en la página,
   en el orden en que aparecen.
"""

import os
import re
from typing import List

EJ_DIR = os.path.dirname(__file__)
API_PATH = os.path.join(EJ_DIR, "api.md")


def modulos_referenciados(ruta: str = API_PATH) -> List[str]:
    """Devuelve los módulos referenciados mediante directivas de mkdocstrings.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Lista de nombres de módulo (por ejemplo, ["ej1c1.libro",
        "ej1c1.coleccion"]), en el orden en que aparecen en la página.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return re.findall(r"(?m)^\s*:::\s*(\S+)\s*$", contenido)


if __name__ == "__main__":
    print("Módulos referenciados:", modulos_referenciados())
