"""
Enunciado:
Redacción de una página con títulos, listas y referencias cruzadas
internas en reStructuredText (parte en Python).

Una vez hayas completado "overview.rst", implementa en este módulo las
funciones:

1. "titulo_principal": devuelve el texto del título de nivel 1 (la línea
   de texto situada justo encima de la línea de signos "=").
2. "elementos_de_lista": devuelve la lista de elementos (sin el guion
   inicial "- ") de la primera lista con guiones de la página.
3. "referencias_cruzadas": devuelve la lista de rutas referenciadas
   mediante el rol ":doc:`texto <ruta>`" o ":doc:`ruta`".
"""

import os
import re
from typing import List

EJ_DIR = os.path.dirname(__file__)
OVERVIEW_PATH = os.path.join(EJ_DIR, "overview.rst")


def _leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def titulo_principal(ruta: str = OVERVIEW_PATH) -> str:
    """Devuelve el título de nivel 1 de la página.

    Un título de nivel 1 en RST es una línea de texto seguida de una
    línea compuesta únicamente por el carácter "=" (de longitud igual o
    mayor que el texto del título).

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Texto del título, sin espacios sobrantes.
    """
    # TODO: busca una línea de texto seguida de una línea de "=" y
    # devuelve el texto de la primera línea.

    with open(ruta, encoding="utf-8") as f:
        contenido = f.read()
        titulo_match = re.search(r"^(.+)$\n=+$", contenido, re.MULTILINE)
        if titulo_match:
            return titulo_match.group(1).strip()
    return ""   


def elementos_de_lista(ruta: str = OVERVIEW_PATH) -> List[str]:
    """Devuelve los elementos de la primera lista con guiones de la página.

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Lista con el texto de cada elemento, sin el guion inicial "- ".
    """
    # TODO: localiza las líneas de lista ("- elemento") y devuelve su
    # contenido, sin el guion inicial.
    with open(ruta, encoding="utf-8") as f:
        contenido = f.read()
        lista_match = re.search(r"^- (.+)$", contenido, re.MULTILINE)
        if lista_match:
            elementos = re.findall(r"^- (.+)$", contenido, re.MULTILINE)
            return [elemento.strip() for elemento in elementos]
    return []


def referencias_cruzadas(ruta: str = OVERVIEW_PATH) -> List[str]:
    """Devuelve las rutas referenciadas con el rol ":doc:".

    Args:
        ruta: Ruta al archivo RST que se quiere analizar.

    Returns:
        Lista de rutas (por ejemplo, ["instalacion", "api"]) referenciadas
        mediante ":doc:`texto <ruta>`" o ":doc:`ruta`".
    """
    # TODO: busca todas las coincidencias del rol ":doc:" (con o sin
    # texto visible) y devuelve la lista de rutas.
    with open(ruta, encoding="utf-8") as f:
        contenido = f.read()
        referencias = re.findall(r":doc:`(?:[^<]+)<([^`]+)>`|:doc:`([^`]+)`", contenido)
        return [ruta for ruta in referencias if ruta]  # Filtra las tuplas vacías   
    


if __name__ == "__main__":
    print("Título:", titulo_principal())
    print("Lista:", elementos_de_lista())
    print("Referencias cruzadas:", referencias_cruzadas())
