# Enunciado:
# Instalación del plugin y configuración de las rutas del código fuente en
# el archivo de configuración.
#
# La extensión "sphinx.ext.autodoc" permite generar documentación de
# referencia de la API automáticamente a partir de los docstrings del
# código fuente, como los que has escrito para el paquete "ej1g1" en el
# ejercicio anterior. La extensión "sphinx.ext.napoleon" añade, además,
# soporte para docstrings en formato Google o NumPy (complementario al
# formato reST nativo).
#
# Tu tarea es:
# 1. Añadir la dependencia "sphinx" al archivo de requisitos
#    "requirements.txt" (ya está añadida de forma implícita en el
#    "requirements.txt" raíz del repositorio, pero este archivo local
#    también debe declararla).
# 2. Completar en este archivo la lista "extensions" para activar
#    "sphinx.ext.autodoc" y "sphinx.ext.napoleon".
# 3. Añadir el código necesario para que Sphinx pueda encontrar el
#    paquete "ej1g1" al generar la documentación, insertando en
#    "sys.path" la ruta de la carpeta "1g/" (un nivel por encima de este
#    archivo "conf.py").

import os
import sys

project = "Mi Proyecto Documentado"
author = "Estudiante"

# TODO: inserta en "sys.path" la ruta donde se encuentra el paquete
# "ej1g1", es decir, la carpeta "1g/" (un nivel por encima de este
# archivo "conf.py").
sys.path.insert(0, os.path.abspath('../1g'))


# TODO: completa la lista "extensions" con "sphinx.ext.autodoc" y
# "sphinx.ext.napoleon".
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

html_theme = "sphinx_rtd_theme"
