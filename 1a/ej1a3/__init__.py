"""
Enunciado:
Inserción de bloques de código con resaltado de sintaxis para comandos y
scripts (parte en Python).

Una vez hayas completado "instalacion.md" con los bloques de código
"```bash" y "```python", implementa en este módulo las funciones que los
extraen mediante expresiones regulares:

1. "bloques_de_codigo": devuelve una lista de tuplas (lenguaje, contenido)
   con todos los bloques de código con resaltado de sintaxis de la página,
   en el orden en que aparecen.
2. "comando_de_instalacion": devuelve, del bloque "```bash", la primera
   línea que contenga "pip install".
"""

import os
import re
from typing import List, Optional, Tuple

EJ_DIR = os.path.dirname(__file__)
INSTALACION_PATH = os.path.join(EJ_DIR, "instalacion.md")


def _leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def bloques_de_codigo(ruta: str = INSTALACION_PATH) -> List[Tuple[str, str]]:
    """Devuelve los bloques de código con resaltado de sintaxis de la página.

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        Lista de tuplas (lenguaje, contenido) con el contenido de cada
        bloque de código delimitado por tres acentos graves, en el orden
        en que aparecen en el archivo.
    """
    # TODO: busca todos los bloques ```<lenguaje>\n...``` y devuelve una
    # lista de tuplas (lenguaje, contenido).
    contenido = _leer(ruta)
    bloques = re.findall(r"```(\w+)\n(.*?)```", contenido, re.DOTALL)
    return [(lenguaje, bloque.strip()) for lenguaje, bloque in bloques]

def comando_de_instalacion(ruta: str = INSTALACION_PATH) -> Optional[str]:
    """Devuelve el comando "pip install" del bloque de código "bash".

    Args:
        ruta: Ruta al archivo Markdown que se quiere analizar.

    Returns:
        La línea del bloque "bash" que contiene "pip install", sin
        espacios sobrantes, o "None" si no se encuentra.
    """
    # TODO: localiza el bloque de código "bash" y devuelve la línea que
    # contiene "pip install".
    bloques = bloques_de_codigo(ruta)
    for lenguaje, bloque in bloques:
        if lenguaje == "bash":
            for linea in bloque.splitlines():
                if "pip install" in linea:
                    return linea.strip()
    return None


if __name__ == "__main__":
    print("Bloques:", bloques_de_codigo())
    print("Comando de instalación:", comando_de_instalacion())
