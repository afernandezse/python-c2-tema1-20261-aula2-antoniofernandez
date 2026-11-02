"""
Enunciado:
Inserción de bloques de código y admonitions en reStructuredText (parte
en Python).

Una vez hayas completado "instalacion.rst", implementa en este módulo las
funciones:

1. "bloques_de_codigo": devuelve una lista de tuplas (lenguaje, contenido)
   con todos los bloques ".. code-block:: <lenguaje>" de la página, en el
   orden en que aparecen.
2. "comando_de_instalacion": devuelve, del bloque "bash", la primera línea
   que contenga "pip install".
3. "admonitions": devuelve un diccionario {tipo: contenido} con el
   contenido (sin indentar) de cada admonition ".. tipo::" de la página.
"""

import os
import re
import textwrap
from typing import Dict, List, Optional, Tuple

EJ_DIR = os.path.dirname(__file__)
INSTALACION_PATH = os.path.join(EJ_DIR, "instalacion.rst")


def _leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def bloques_de_codigo(ruta: str = INSTALACION_PATH) -> List[Tuple[str, str]]:
    """Devuelve los bloques ".. code-block:: <lenguaje>" de la página.

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Lista de tuplas (lenguaje, contenido) con el contenido
        (desindentado) de cada bloque de código, en el orden en que
        aparecen.
    """
    # TODO: busca todas las directivas ".. code-block:: <lenguaje>" y
    # devuelve una lista de tuplas (lenguaje, contenido desindentado).
    
    content = _leer(ruta)
    pattern = r'(?m)^\.\. code-block::\s*(\w+)[ \t]*\n((?:\n|[ \t]+.*\n)+)'
    matches = re.findall(pattern, content)
    bloques = []
    for lenguaje, bloque in matches:
        # Desindentamos el contenido del bloque
        desindentado = textwrap.dedent(bloque).strip()
        bloques.append((lenguaje, desindentado))
    return bloques


def comando_de_instalacion(ruta: str = INSTALACION_PATH) -> Optional[str]:
    """Devuelve el comando "pip install" del bloque de código "bash".

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        La línea del bloque "bash" que contiene "pip install", sin
        espacios sobrantes, o "None" si no se encuentra.
    """
    # TODO: localiza el bloque de código "bash" y devuelve la línea que
    # contiene "pip install".
    for lenguaje, bloque in bloques_de_codigo(ruta):
        if lenguaje == "bash":
            for linea in bloque.splitlines():
                if "pip install" in linea:
                    return linea.strip()
    return None


def admonitions(ruta: str = INSTALACION_PATH) -> Dict[str, str]:
    """Devuelve el contenido de cada admonition de la página.

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Diccionario que asocia el tipo de admonition ("note", "warning",
        etc.) con su contenido, sin la indentación.
    """
    # TODO: busca todas las directivas ".. tipo::" (note, warning, etc.)
    # y devuelve un diccionario tipo -> contenido desindentado.
    content = _leer(ruta)
    pattern = r'(?m)^\.\. (\w+)::[ \t]*\n((?:\n|[ \t]+.*\n)+)'
    matches = re.findall(pattern, content)
    admonitions_dict = {}
    for tipo, bloque in matches:
        desindentado = textwrap.dedent(bloque).strip()
        admonitions_dict[tipo] = desindentado
    return admonitions_dict


if __name__ == "__main__":
    print("Bloques:", bloques_de_codigo())
    print("Comando de instalación:", comando_de_instalacion())
    print("Admonitions:", admonitions())
