"""
Define la clase Libro, que representa un libro físico de una biblioteca.
"""


class Libro:
    """
    Define la clase Libro, que representa un libro físico de una biblioteca.
    Sus atributos incluyen título, autor, año de publicación, ISBN y un indicador de si está prestado o no.
    Sus métodos permiten prestar y devolver el libro, así como obtener representaciones y comparaciones basadas en el ISBN.
    Attributes:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        anio (int): El año de publicación del libro.
        isbn (str): El ISBN del libro, que sirve como identificador único.
        prestado (bool): Indica si el libro está actualmente prestado (True) o disponible (False).
    Methods:
        __init__(self, titulo, autor, anio, isbn): Inicializa una instancia de Libro.
        prestar(self): Marca el libro como prestado.
        devolver(self): Marca el libro como devuelto.
        __repr__(self): Devuelve una representación en texto del libro.
        __eq__(self, other): Compara dos libros por su ISBN.
    """

    def __init__(self, titulo, autor, anio, isbn):
        """
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            anio (int): El año de publicación del libro.
            isbn (str): El ISBN del libro, que sirve como identificador único.
        """
        # TODO: guarda "titulo", "autor", "anio" e "isbn" como atributos.
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.isbn = isbn
        # TODO: inicializa un atributo "prestado" a False (el libro
        # empieza disponible).
        self.prestado = False

    def prestar(self):
        """
        Este método cambia el estado del libro a prestado si no lo estaba previamente.
        Returns:
            bool: True si el libro se ha prestado con éxito, False si ya estaba prestado.
        """
        # TODO: si el libro ya está prestado, devuelve False sin hacer
        # nada más.
        if self.prestado:
            return False
        # TODO: si el libro no está prestado, márcalo como prestado
        # (atributo "prestado" a True) y devuelve True.
        self.prestado = True
        return True

    def devolver(self):
        """
        Este método cambia el estado del libro a disponible, marcándolo como no prestado.   
        """
        # TODO: marca el libro como disponible (atributo "prestado" a
        # False).
        self.prestado = False

    def __repr__(self):
        """
        Este método devuelve una representación en texto del libro, incluyendo su título, autor y año de publicación.
        Returns:
            str: Una cadena de texto que representa el libro en el formato "'<titulo>' de <autor> (<anio>)".
        """
        # TODO: devuelve un string con, por ejemplo, el formato:
        # "'<titulo>' de <autor> (<anio>)"
        return f"'{self.titulo}' de {self.autor} ({self.anio})"

    def __eq__(self, other):
        """
        Este método compara dos libros basándose en su ISBN, considerándolos iguales si ambos tienen el mismo ISBN.
        Args:
            other (Libro): Otro objeto de tipo Libro para comparar.
        Returns:
            bool: True si ambos libros tienen el mismo ISBN, False en caso contrario.
        """
        # TODO: si "other" no es una instancia de "Libro", devuelve
        # "NotImplemented".
        if not isinstance(other, Libro):
            return NotImplemented
        # TODO: en caso contrario, devuelve True si ambos ISBN coinciden.
        return self.isbn == other.isbn
