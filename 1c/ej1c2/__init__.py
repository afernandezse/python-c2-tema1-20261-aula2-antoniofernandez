"""
Enunciado:
Instalación del plugin y configuración de las rutas del código fuente
(parte en Python).

Una vez hayas completado "mkdocs.yml" y "requirements.txt", implementa en
este módulo las funciones:

1. "plugins_configurados": devuelve la lista de nombres de los plugins
   activados en "mkdocs.yml" (por ejemplo, ["search", "mkdocstrings"]).
2. "rutas_de_mkdocstrings": devuelve la lista de rutas configuradas en
   "handlers.python.paths" del plugin "mkdocstrings".
"""

import os
from typing import List

import yaml

EJ_DIR = os.path.dirname(__file__)
MKDOCS_CONFIG_PATH = os.path.join(EJ_DIR, "mkdocs.yml")


def _find_plugin(plugins, name):
    for plugin in plugins:
        if plugin == name:
            return {}
        if isinstance(plugin, dict) and name in plugin:
            return plugin[name] or {}
    return None


def plugins_configurados(ruta_config: str = MKDOCS_CONFIG_PATH) -> List[str]:
    """Devuelve los nombres de los plugins activados en "mkdocs.yml".

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Lista de nombres de plugins, en el orden en que aparecen.
    """
    # TODO: carga el archivo YAML y devuelve los nombres de los elementos
    # de la lista "plugins" (cada elemento puede ser una cadena o un
    # diccionario de una sola clave).
    with open(ruta_config, "r") as f:
        config = yaml.safe_load(f)
    return [plugin if isinstance(plugin, str) else list(plugin.keys())[0] for plugin in config.get("plugins", [])]


def rutas_de_mkdocstrings(ruta_config: str = MKDOCS_CONFIG_PATH) -> List[str]:
    """Devuelve las rutas configuradas en "handlers.python.paths".

    Args:
        ruta_config: Ruta al archivo "mkdocs.yml" que se quiere leer.

    Returns:
        Lista de rutas de código fuente configuradas para el plugin
        "mkdocstrings".
    """
    # TODO: carga el archivo YAML, localiza el plugin "mkdocstrings" y
    # devuelve "handlers.python.paths".
    with open(ruta_config, "r") as f:
        config = yaml.safe_load(f)
    mkdocstrings_plugin = _find_plugin(config.get("plugins", []), "mkdocstrings")
    return mkdocstrings_plugin.get("handlers", {}).get("python", {}).get("paths", [])


if __name__ == "__main__":
    print("Plugins:", plugins_configurados())
    print("Rutas de mkdocstrings:", rutas_de_mkdocstrings())
