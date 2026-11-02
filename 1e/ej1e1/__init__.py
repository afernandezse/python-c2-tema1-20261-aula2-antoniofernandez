"""
Enunciado:
Configuración del proyecto Sphinx y del índice de navegación (parte en
Python).

Una vez hayas completado "conf.py" y "index.rst", implementa en este
módulo las funciones:

1. "info_proyecto": devuelve un diccionario con las claves "project" y
   "author" tal y como están definidas en "conf.py".
2. "paginas_del_indice": devuelve la lista de páginas declaradas dentro
   del bloque ".. toctree::" de "index.rst", en el orden en que aparecen.
"""

import os
import re
from typing import Dict, List

EJ_DIR = os.path.dirname(__file__)
CONF_PATH = os.path.join(EJ_DIR, "conf.py")
INDEX_PATH = os.path.join(EJ_DIR, "index.rst")


def info_proyecto(ruta: str = CONF_PATH) -> Dict[str, str]:
    """Devuelve el nombre del proyecto y el autor configurados en "conf.py".

    Sphinx ejecuta "conf.py" como un script de Python para leer su
    configuración; esta función hace lo mismo mediante "exec" sobre un
    espacio de nombres propio.

    Args:
        ruta: Ruta al archivo "conf.py" que se quiere leer.

    Returns:
        Diccionario con las claves "project" y "author".
    """
    # TODO: lee el contenido de "ruta", ejecútalo con "exec" sobre un
    # diccionario de espacio de nombres propio, y devuelve un diccionario
    # con las claves "project" y "author" tomadas de ese espacio de
    # nombres.

    namespace = {}
    with open(ruta, "r") as f:
        exec(f.read(), namespace)
    return {"project": namespace.get("project"), "author": namespace.get("author")}


def paginas_del_indice(ruta: str = INDEX_PATH) -> List[str]:
    """Devuelve las páginas declaradas en el bloque ".. toctree::".

    Args:
        ruta: Ruta al archivo "index.rst" que se quiere analizar.

    Returns:
        Lista de nombres de página (sin extensión), en el orden en que
        aparecen dentro del "toctree".
    """
    # TODO: localiza el bloque ".. toctree::" y devuelve las líneas
    # indentadas que no son opciones (no empiezan por ":"), ignorando las
    # líneas en blanco.
    
    with open(ruta, "r") as f:
        content = f.read()

    # Encuentra el bloque ".. toctree::"
    toctree_match = re.search(r"\.\. toctree::\n((?:\s+.*\n)+)", content)
    if not toctree_match:
        return []

    # Extrae las líneas indentadas que no son opciones
    toctree_content = toctree_match.group(1)
    lines = toctree_content.split('\n')
    pages = [line.strip() for line in lines if line.strip() and not line.strip().startswith(':')]

    return pages


if __name__ == "__main__":
    print("Información del proyecto:", info_proyecto())
    print("Páginas del índice:", paginas_del_indice())
