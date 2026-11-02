"""
Enunciado:
Instalación del plugin y configuración de las rutas del código fuente
(parte en Python).

Una vez hayas completado "conf.py" y "requirements.txt", implementa en
este módulo las funciones:

1. "extensiones_activadas": devuelve la lista de extensiones activadas en
   "conf.py" (la variable "extensions").
2. "rutas_en_sys_path": devuelve la lista de rutas que "conf.py" añade a
   "sys.path", como cadenas de texto relativas a la carpeta de "conf.py"
   (por ejemplo, [".."]).
"""

import os
import re
from typing import List

EJ_DIR = os.path.dirname(__file__)
CONF_PATH = os.path.join(EJ_DIR, "conf.py")


def _leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def extensiones_activadas(ruta_config: str = CONF_PATH) -> List[str]:
    """Devuelve las extensiones activadas en "conf.py".

    Args:
        ruta_config: Ruta al archivo "conf.py" que se quiere leer.

    Returns:
        Lista de nombres de extensión (por ejemplo,
        ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]).
    """
    # TODO: ejecuta el contenido de "conf.py" (por ejemplo con "exec"
    # sobre un diccionario propio) y devuelve el valor de "extensions".
    dict_conf = {}
    exec(_leer(ruta_config), dict_conf)
    return dict_conf.get("extensions", [])


def rutas_en_sys_path(ruta_config: str = CONF_PATH) -> List[str]:
    """Devuelve las rutas que "conf.py" añade a "sys.path".

    Args:
        ruta_config: Ruta al archivo "conf.py" que se quiere analizar.

    Returns:
        Lista de las rutas (como aparecen literalmente en las llamadas a
        "sys.path.insert" o "sys.path.append") usadas en el archivo.
    """
    # TODO: busca todas las llamadas "sys.path.insert(...)" o
    # "sys.path.append(...)" en el texto de "conf.py" y devuelve la lista
    # de rutas (el argumento que contiene la ruta, como cadena de texto).
    rutas = []
    contenido = _leer(ruta_config)
    # Expresión regular para encontrar sys.path.insert(...) o sys.path.append(...)
    patron = r'sys\.path\.(?:insert|append)\(\s*\d*\s*,\s*os\.path\.abspath\(\s*[\'"]([^\'"]+)[\'"]\s*\)\s*\)'
    rutas = re.findall(patron, contenido)
    return rutas


if __name__ == "__main__":
    print("Extensiones:", extensiones_activadas())
    print("Rutas en sys.path:", rutas_en_sys_path())
