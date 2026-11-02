"""
Módulo que define la clase Agenda, que representa una agenda de contactos.

"""

from .excepciones import ContactoNoEncontradoError


class Agenda:
    """
    Clase que representa una agenda de contactos.

    :ivar nombre: El nombre de la agenda.
    :ivar contactos: La lista de contactos en la agenda.
    """

    def __init__(self, nombre):
        """
        Inicializa una agenda vacía.

        :param nombre: El nombre de la agenda.
        :type nombre: str
        """
        self.nombre = nombre
        self.contactos = []

    def añadir_contacto(self, contacto):
        """
        Añade un contacto a la agenda.

        :param contacto: El contacto a añadir.
        :type contacto: Contacto
        """
        self.contactos.append(contacto)

    def buscar_por_telefono(self, telefono):
        """
        Busca un contacto por su número de teléfono.

        :param telefono: El número de teléfono del contacto a buscar.
        :type telefono: str
        :return: El contacto con el número de teléfono especificado.
        :rtype: Contacto
        :raises ContactoNoEncontradoError: Si no se encuentra ningún contacto con ese teléfono.
        """
        for contacto in self.contactos:
            if contacto.telefono == telefono:
                return contacto
        raise ContactoNoEncontradoError("Contacto no encontrado")

    def buscar_favoritos(self):
        """
        Busca los contactos marcados como favoritos.

        :return: La lista de contactos marcados como favoritos.
        :rtype: list
        """
        favoritos = [contacto for contacto in self.contactos if contacto.favorito]
        return favoritos

    def __len__(self):
        """
        Devuelve el número de contactos de la agenda.

        :return: El número de contactos de la agenda.
        :rtype: int
        """
        return len(self.contactos)
