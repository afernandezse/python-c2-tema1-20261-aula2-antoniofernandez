# Enunciado:
# Personalización de la interfaz del tema Read the Docs mediante
# "html_theme_options".
#
# El tema "sphinx_rtd_theme" permite personalizar su aspecto mediante el
# diccionario "html_theme_options", indicando, entre otras, las claves:
#   - "logo_only" (booleano): si solo se muestra el logo, sin el nombre
#     del proyecto.
#   - "navigation_depth" (entero): la profundidad máxima del menú lateral
#     de navegación.
#
# Tu tarea es completar la configuración del tema añadiendo una clave
# "html_theme_options" con, como mínimo:
#   1. "logo_only" con el valor "True".
#   2. "navigation_depth" con el valor "4".

project = "Mi Proyecto Documentado"
author = "Estudiante"

extensions = []
html_theme = "sphinx_rtd_theme"

# TODO: añade aquí la clave "html_theme_options" con "logo_only" y
# "navigation_depth".
html_theme_options = {
    "logo_only": True,
    "navigation_depth": 4
}
