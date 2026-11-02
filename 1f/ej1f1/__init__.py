"""
Enunciado:
Instalación del paquete de diseño avanzado y cambio del tema por defecto
(parte en Python).

Una vez hayas completado "conf.py" y "requirements.txt", implementa en
este módulo las funciones:

1. "tema_configurado": devuelve el nombre del tema configurado en
   "conf.py" (la variable "html_theme").
2. "dependencias": devuelve la lista de paquetes (sin comentarios ni
   líneas en blanco) declarados en "requirements.txt".
"""

import os
from typing import List

EJ_DIR = os.path.dirname(__file__)
CONF_PATH = os.path.join(EJ_DIR, "conf.py")
REQUIREMENTS_PATH = os.path.join(EJ_DIR, "requirements.txt")


def tema_configurado(ruta_config: str = CONF_PATH) -> str:
    """Devuelve el nombre del tema configurado en "conf.py".

    Args:
        ruta_config: Ruta al archivo "conf.py" que se quiere leer.

    Returns:
        Valor de la variable "html_theme" (por ejemplo,
        "sphinx_rtd_theme").
    """
    # TODO: ejecuta el contenido de "conf.py" (por ejemplo con "exec"
    # sobre un diccionario propio) y devuelve el valor de "html_theme".
    contexto = {}
    with open(ruta_config, "r", encoding="utf-8") as f:
        exec(f.read(), contexto)
    return contexto.get("html_theme", "")


def dependencias(ruta_requirements: str = REQUIREMENTS_PATH) -> List[str]:
    """Devuelve la lista de dependencias declaradas en "requirements.txt".

    Args:
        ruta_requirements: Ruta al archivo de requisitos que se quiere leer.

    Returns:
        Lista de nombres de paquetes, sin comentarios ni líneas en blanco.
    """
    # TODO: lee el archivo de requisitos y devuelve la lista de paquetes,
    # ignorando las líneas vacías y las que empiezan por "#".
    dependencias = []
    with open(ruta_requirements, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                dependencias.append(linea)
    return dependencias


if __name__ == "__main__":
    print("Tema:", tema_configurado())
    print("Dependencias:", dependencias())
