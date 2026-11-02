.. Enunciado:
   Integración de la referencia automática de la API dentro de las
   páginas de documentación.

   La extensión "sphinx.ext.autodoc" permite insertar en cualquier
   página RST la documentación generada automáticamente a partir de los
   docstrings de un módulo de Python, usando directivas como:

       .. automodule:: nombre_del_modulo
          :members:

   En el ejercicio "ej1g1" has construido un paquete "ej1g1" con dos
   módulos: "ej1g1.contacto" (clase "Contacto") y "ej1g1.agenda" (clase
   "Agenda").

   Tu tarea es completar esta página de referencia de la API para que
   incluya un título y dos directivas ".. automodule::": una para el
   módulo "ej1g1.contacto" y otra para el módulo "ej1g1.agenda", ambas
   con la opción ":members:" para documentar también sus métodos.

   Consulta también "__init__.py" en esta misma carpeta para completar
   la parte en Python de este ejercicio.

Referencia de la API
=====================

TODO: añade aquí la directiva ``.. automodule:: ej1g1.contacto`` (con
``:members:``) para generar automáticamente la documentación del módulo
"ej1g1.contacto".

..automodule:: ej1g1.contacto
   :members:

   

TODO: añade aquí la directiva ``.. automodule:: ej1g1.agenda`` (con
``:members:``) para generar automáticamente la documentación del módulo
"ej1g1.agenda".

..automodule:: ej1g1.agenda
   :members:
