"""
Enunciado:
Escritura de un mini-proyecto en Python ("agenda") documentado con
docstrings estructurados en formato reST (el formato nativo de Sphinx,
con campos ":param:", ":type:", ":return:", ":rtype:" y ":raises:").

Este paquete define una pequeña agenda de contactos, repartida en tres
módulos:

- "agenda.contacto": la clase "Contacto".
- "agenda.agenda": la clase "Agenda", una colección de contactos.
- "agenda.excepciones": la excepción "ContactoNoEncontradoError".

Tu tarea es completar el código y los docstrings (en formato reST) de
estos tres módulos, y la función "cargar_agenda_inicial" de este archivo,
que crea una "Agenda" con algunos contactos de ejemplo.
"""

from .agenda import Agenda
from .contacto import Contacto
from .excepciones import ContactoNoEncontradoError

__all__ = ["Agenda", "Contacto", "ContactoNoEncontradoError", "cargar_agenda_inicial"]


def cargar_agenda_inicial():
    """
    Crea una agenda de ejemplo con varios contactos.

    :return: Una agenda de ejemplo con al menos tres contactos.
    :rtype: Agenda
    """
    agenda = Agenda("Agenda de ejemplo")
    agenda.añadir_contacto(Contacto("Ana", "600111222"))
    agenda.añadir_contacto(Contacto("Bruno", "600333444"))
    agenda.añadir_contacto(Contacto("Carla", "600555666"))
    return agenda


if __name__ == "__main__":
    agenda = cargar_agenda_inicial()
    print(f"Agenda '{agenda.nombre}' con {len(agenda)} contactos.")
