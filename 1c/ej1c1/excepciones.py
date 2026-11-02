"""Define la excepción LibroNoEncontradoError, usada por el paquete ej1c1."""


class LibroNoEncontradoError(Exception):
    """Excepción lanzada cuando no se encuentra un libro por su ISBN dentro de una ColeccionLibros.

    Esta excepción se utiliza para indicar que la búsqueda de un libro
    específico mediante su identificador ISBN no ha devuelto ningún resultado
    dentro de la colección.
    """

    pass