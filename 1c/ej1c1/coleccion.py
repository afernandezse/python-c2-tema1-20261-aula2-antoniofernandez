"""
TODO: completa el docstring de este módulo.
Debe indicar brevemente que este módulo define la clase "ColeccionLibros",
que gestiona una colección de objetos "Libro".
"""

from .excepciones import LibroNoEncontradoError


class ColeccionLibros:
    """
    TODO: completa este docstring en formato Google.
    Debe describir la clase y documentar sus atributos en una sección
    "Attributes:" (nombre y la lista interna de libros).
    """

    def __init__(self, nombre):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el parámetro "nombre" en una sección "Args:".
        """
        # TODO: guarda "nombre" como atributo.
        # TODO: inicializa una lista vacía donde se guardarán los libros
        self._nombre = nombre
        self._libros = []
        # (por ejemplo, en un atributo "_libros").
        pass

    def añadir_libro(self, libro):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el parámetro "libro" (un objeto "Libro") en una
        sección "Args:".
        """
        # TODO: añade "libro" a la lista interna de libros.
        self._libros.append(libro)
        pass

    def buscar_por_isbn(self, isbn):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el parámetro "isbn" en una sección "Args:", el
        valor devuelto (el objeto "Libro" encontrado) en una sección
        "Returns:", y documentar en una sección "Raises:" que lanza
        "LibroNoEncontradoError" si no se encuentra ningún libro con ese
        ISBN.
        """
        # TODO: recorre la lista interna de libros y devuelve el que
        # tenga el ISBN indicado.
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        # TODO: si no se encuentra ningún libro con ese ISBN, lanza
        # "LibroNoEncontradoError".
        raise LibroNoEncontradoError(f"No se encontró ningún libro con ISBN {isbn}.")
        pass

    def buscar_por_autor(self, autor):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el parámetro "autor" en una sección "Args:" y el
        valor devuelto (una lista de objetos "Libro") en una sección
        "Returns:".
        """
        # TODO: devuelve una lista con todos los libros cuyo autor
        # coincida exactamente con "autor".
        return [libro for libro in self._libros if libro.autor == autor]


    def prestar_libro(self, isbn):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el parámetro "isbn" en una sección "Args:" y el
        valor devuelto en una sección "Returns:" (True si se ha podido
        prestar, False si ya estaba prestado), documentando también en
        una sección "Raises:" que lanza "LibroNoEncontradoError" si no
        existe ningún libro con ese ISBN.
        """
        # TODO: busca el libro por ISBN (reutiliza "buscar_por_isbn") y
        # llama a su método "prestar()", devolviendo el resultado.
        libro = self.buscar_por_isbn(isbn)
        return libro.prestar()

    def listar_disponibles(self):
        """
        TODO: completa este docstring en formato Google.
        Debe documentar el valor devuelto (una lista de objetos "Libro"
        no prestados) en una sección "Returns:".
        """
        # TODO: devuelve una lista con todos los libros cuyo atributo
        # "prestado" sea False.
        return [libro for libro in self._libros if not libro.prestado]

    def __len__(self):
        """
        TODO: completa este docstring en formato Google.
        Debe describir que devuelve el número total de libros de la
        colección, documentándolo en una sección "Returns:".
        """
        # TODO: devuelve el número de libros de la colección.
        return len(self._libros)
