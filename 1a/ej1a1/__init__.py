"""
Enunciado:
Configuración del menú de navegación global (nav) y primer contacto con el
servidor de desarrollo de MkDocs.

Además de completar "mkdocs.yml" (la lista "nav"), tu tarea en este módulo
es escribir el código Python que:

1. Lee el archivo "mkdocs.yml" de esta misma carpeta y devuelve, en orden,
   los títulos de las páginas configuradas en "nav"
   (función "titulos_del_menu").
2. Construye la línea de comandos necesaria para arrancar el servidor de
   desarrollo de MkDocs en un puerto dado, es decir, el equivalente a
   ejecutar en la terminal:

       mkdocs serve --dev-addr 127.0.0.1:<puerto>

   (función "comando_mkdocs_serve").

No es necesario ejecutar el servidor de verdad: basta con construir
correctamente la lista de argumentos del comando, tal y como la aceptaría
"subprocess.run".
"""

import os
from typing import List

import yaml

EJ_DIR = os.path.dirname(__file__)
MKDOCS_CONFIG_PATH = os.path.join(EJ_DIR, "mkdocs.yml")


def titulos_del_menu(ruta_config: str = MKDOCS_CONFIG_PATH) -> List[str]:
    """Devuelve los títulos del menú de navegación, en orden.

    Lee el archivo de configuración de MkDocs indicado y extrae los
    títulos (las claves) de cada elemento de la lista "nav", respetando
    el orden en que aparecen en el archivo.

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Lista de títulos del menú, en el mismo orden que en "nav".
    """
    # TODO: abre y carga el archivo YAML indicado por "ruta_config" y
    # devuelve la lista de títulos de "nav", en orden.


    with open(ruta_config, "r") as f:
        config = yaml.safe_load(f)
    return [item['title'] for item in config['nav']]




def comando_mkdocs_serve(puerto: int = 8000) -> List[str]:
    """Construye el comando para arrancar "mkdocs serve" en un puerto dado.

    El resultado debe ser una lista de cadenas lista para pasarse a
    "subprocess.run", equivalente a ejecutar en la terminal:

        mkdocs serve --dev-addr 127.0.0.1:<puerto>

    Args:
        puerto: Puerto en el que debe escuchar el servidor de desarrollo.

    Returns:
        Lista de argumentos del comando, por ejemplo
        ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8000"].
    """
    # TODO: construye y devuelve la lista de argumentos del comando.
    return ["mkdocs", "serve", "--dev-addr", f"127.0.0.1:{puerto}"]
    raise NotImplementedError



if __name__ == "__main__":
    print("Títulos del menú:", titulos_del_menu())
    print("Comando para servir la documentación:", " ".join(comando_mkdocs_serve()))
