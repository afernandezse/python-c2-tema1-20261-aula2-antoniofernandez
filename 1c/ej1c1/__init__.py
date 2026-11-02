"""
Enunciado:
Escritura de funciones en Python documentadas mediante docstrings
estructurados en formato Google.

En este ejercicio vas a construir una pequeña librería en forma de paquete
de Python ("ej1c1/", el propio directorio donde se encuentra este
archivo), con sus propias clases, y la documentarás completamente usando
docstrings en formato Google. Esta documentación es la que luego se usará,
en los ejercicios "ej1c2" y "ej1c3", para generar automáticamente la
referencia de la API con "mkdocstrings".

El paquete contiene los siguientes módulos, que deberás completar:

- "excepciones.py": una excepción personalizada "LibroNoEncontradoError".
- "libro.py": la clase "Libro", que representa un libro físico.
- "coleccion.py": la clase "ColeccionLibros", que gestiona una colección de
  objetos "Libro".

Tu tarea en este archivo ("__init__.py"), que actúa a la vez como punto de
entrada del paquete y como fichero que expone su API pública, es:

1. Importar "Libro", "ColeccionLibros" y "LibroNoEncontradoError" desde sus
   respectivos módulos (import relativo, p. ej. "from .libro import
   Libro").
2. Completar la lista "__all__" con esos tres nombres.
3. Completar la función "cargar_libros_iniciales" para que devuelva una
   "ColeccionLibros" con 3 libros de ejemplo ya añadidos, documentándola
   con un docstring en formato Google (con una sección "Returns:").
"""

from .coleccion import ColeccionLibros
from .excepciones import LibroNoEncontradoError
from .libro import Libro

__all__ = [
    "Libro",
    "ColeccionLibros",
    "LibroNoEncontradoError",
    "cargar_libros_iniciales",
]


def cargar_libros_iniciales():
    """Crea una colección de libros de ejemplo.

    Returns:
        ColeccionLibros: Una colección con tres libros iniciales.
    """
    coleccion = ColeccionLibros("Mi biblioteca")
    coleccion.añadir_libro(Libro("Dune", "Frank Herbert", 1965, "9780441172719"))
    coleccion.añadir_libro(
        Libro("Fundación", "Isaac Asimov", 1951, "9780553293357")
    )
    coleccion.añadir_libro(
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "9780307474728")
    )
    return coleccion


if __name__ == "__main__":
    coleccion = cargar_libros_iniciales()
    print(f"Colección: {coleccion.nombre} ({len(coleccion)} libros)")
    for libro in coleccion.listar_disponibles():
        print(f" - {libro}")
