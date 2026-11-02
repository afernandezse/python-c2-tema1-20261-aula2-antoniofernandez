"""
Enunciado:
Integración de la referencia automática de la API (parte en Python).

Una vez hayas completado "api.rst" con las directivas de autodoc,
implementa en este módulo la función:

1. "modulos_referenciados": devuelve la lista de nombres de módulo
   referenciados mediante directivas ".. automodule:: nombre_del_modulo"
   en la página, en el orden en que aparecen.
"""

import os
import re
from typing import List

EJ_DIR = os.path.dirname(__file__)
API_PATH = os.path.join(EJ_DIR, "api.rst")


def modulos_referenciados(ruta: str = API_PATH) -> List[str]:
    """Devuelve los módulos referenciados mediante directivas "automodule".

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Lista de nombres de módulo (por ejemplo, ["ej1g1.contacto",
        "ej1g1.agenda"]), en el orden en que aparecen en la página.
    """
    # TODO: busca todas las directivas ".. automodule:: nombre_del_modulo"
    # y devuelve la lista de nombres de módulo, en orden.
    list_modulos = []
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
        list_modulos = re.findall(r"\.\. automodule:: (\S+)", contenido)
    return list_modulos


if __name__ == "__main__":
    print("Módulos referenciados:", modulos_referenciados())
