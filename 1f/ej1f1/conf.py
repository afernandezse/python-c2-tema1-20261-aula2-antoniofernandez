# Enunciado:
# Instalación del paquete de diseño avanzado y cambio del tema por defecto.
#
# Sphinx usa por defecto un tema básico llamado "alabaster". El tema
# "Read the Docs" (paquete "sphinx-rtd-theme") ofrece un diseño mucho más
# avanzado y es uno de los más usados en proyectos Python.
#
# Tu tarea es:
# 1. Añadir la dependencia "sphinx-rtd-theme" al archivo de requisitos
#    "requirements.txt".
# 2. Cambiar en este archivo de configuración el tema por defecto
#    ("alabaster") por el tema "sphinx_rtd_theme".

project = "Mi Proyecto Documentado"
author = "Estudiante"

extensions = []

# TODO: cambia el valor de "html_theme" a "sphinx_rtd_theme".
html_theme = "sphinx_rtd_theme"  # Valor por defecto, cambiar a "sphinx_rtd_theme"