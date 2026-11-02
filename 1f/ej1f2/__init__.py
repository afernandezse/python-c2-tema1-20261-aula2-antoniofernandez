"""
Enunciado:
Personalización de la interfaz del tema Read the Docs (parte en Python).

Una vez hayas completado "conf.py" con la clave "html_theme_options",
implementa en este módulo la función:

1. "opciones_del_tema": devuelve el diccionario "html_theme_options"
   configurado en "conf.py".
"""

import os
from typing import Dict

EJ_DIR = os.path.dirname(__file__)
CONF_PATH = os.path.join(EJ_DIR, "conf.py")


def opciones_del_tema(ruta_config: str = CONF_PATH) -> Dict[str, object]:
    """Devuelve las opciones de personalización del tema.

    Args:
        ruta_config: Ruta al archivo "conf.py" que se quiere leer.

    Returns:
        Diccionario con, como mínimo, las claves "logo_only" y
        "navigation_depth".
    """
    # TODO: ejecuta el contenido de "conf.py" y devuelve el valor de
    # "html_theme_options".
    conf = {}
    with open(ruta_config, "r") as f:
        exec(f.read(), conf)
    return conf.get("html_theme_options", {})


if __name__ == "__main__":
    print("Opciones del tema:", opciones_del_tema())
