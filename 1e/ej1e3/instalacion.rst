.. Enunciado:
   Inserción de bloques de código con resaltado de sintaxis y de cajas de
   alerta (admonitions) en reStructuredText.

   Completa esta página de instalación añadiendo:

   1. Un bloque de código con resaltado de sintaxis para "bash" que
      muestre el comando para instalar las dependencias del proyecto con
      pip, usando la directiva:

          .. code-block:: bash

             comando

   2. Un bloque de código con resaltado de sintaxis para "python" que
      muestre un pequeño script de ejemplo.
   3. Una admonition de tipo "note" con información útil para el lector,
      usando la directiva ".. note::".
   4. Una admonition de tipo "warning" advirtiendo de algo importante,
      usando la directiva ".. warning::".

   Recuerda que, en RST, el contenido de una directiva se indenta (por
   convención, 3 espacios) respecto a la línea de la directiva.

   Consulta también "__init__.py" en esta misma carpeta para completar
   la parte en Python de este ejercicio.

Instalación
===========


.. code-block:: bash

   pip install -r requirements.txt



.. code-block:: python

   def saludo(nombre):
      print(f"Hola, {nombre}!")

   if __name__ == "__main__":
      saludo("Mundo")


.. note::

   Recuerda que debes tener Python 3.6 o superior instalado en tu sistema
   para ejecutar este proyecto correctamente.


.. warning::

   Asegúrate de ejecutar los comandos en un entorno virtual para evitar
   conflictos con otras dependencias de Python que puedas tener
   instaladas globalmente.
