"""
Módulo que define la clase :class:`Contacto`, un contacto de una agenda telefónica.
"""


class Contacto:
    """
    Representa un contacto de una agenda telefónica.

    :ivar nombre: El nombre del contacto.
    :ivar telefono: El número de teléfono del contacto.
    :ivar favorito: Indica si el contacto está marcado como favorito.
    """

    def __init__(self, nombre, telefono):
        """
        Inicializa un contacto.

        :param nombre: El nombre del contacto.
        :type nombre: str
        :param telefono: El número de teléfono del contacto.
        :type telefono: str
        """
        self.nombre = nombre
        self.telefono = telefono
        self.favorito = False

    def marcar_como_favorito(self):
        """
        Marca el contacto como favorito.

        :return: No devuelve ningún valor.
        :rtype: None
        """
        self.favorito = True

    def __repr__(self):
        """
        Devuelve una representación en texto del contacto.

        :return: El nombre y el teléfono del contacto.
        :rtype: str
        """
        return f"{self.nombre} ({self.telefono})"

    def __eq__(self, other):
        """
        Compara contactos por número de teléfono.

        :param other: El objeto que se compara con este contacto.
        :type other: object
        :return: ``True`` si ambos contactos tienen el mismo teléfono.
        :rtype: bool
        """
        if not isinstance(other, Contacto):
            return NotImplemented
        return self.telefono == other.telefono
