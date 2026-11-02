"""
Enunciado:
Personalización de la paleta de colores y la interfaz (parte en Python).

Una vez hayas completado "mkdocs.yml" con la paleta de colores y las
funcionalidades del tema, implementa en este módulo las funciones:

1. "paleta_de_colores": devuelve un diccionario con los colores "primary"
   y "accent" configurados en "theme.palette".
2. "funcionalidades_activadas": devuelve la lista de funcionalidades
   configuradas en "theme.features".
"""

import os
from typing import Dict, List

from mkdocs import config
import yaml

EJ_DIR = os.path.dirname(__file__)
MKDOCS_CONFIG_PATH = os.path.join(EJ_DIR, "mkdocs.yml")


def paleta_de_colores(ruta_config: str = MKDOCS_CONFIG_PATH) -> Dict[str, str]:
    """Devuelve los colores "primary" y "accent" de la paleta configurada.

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Diccionario con, como mínimo, las claves "primary" y "accent".
    """
    # TODO: carga el archivo YAML y devuelve "theme.palette".
    with open(ruta_config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("theme", {}).get("palette", {})


def funcionalidades_activadas(ruta_config: str = MKDOCS_CONFIG_PATH) -> List[str]:
    """Devuelve las funcionalidades configuradas en "theme.features".

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Lista de funcionalidades activadas (por ejemplo,
        "navigation.tabs").
    """
    # TODO: carga el archivo YAML y devuelve "theme.features".
    with open(ruta_config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("theme", {}).get("features", [])



if __name__ == "__main__":
    print("Paleta:", paleta_de_colores())
    print("Funcionalidades:", funcionalidades_activadas())
