# Ejercicio ej1a1: menú de navegación + `mkdocs serve`

Este ejercicio combina dos tareas:

1. **Configuración (`mkdocs.yml`)**: completar la clave `nav` del archivo de
   configuración de MkDocs con las cuatro páginas indicadas en el
   enunciado, en el orden correcto.
2. **Python (`__init__.py`)**: implementar dos funciones que trabajan con
   esa configuración y con el comando de vista previa de MkDocs:
   - `titulos_del_menu`: lee `mkdocs.yml` y devuelve los títulos del menú,
     en orden.
   - `comando_mkdocs_serve`: construye la lista de argumentos equivalente a
     ejecutar `mkdocs serve --dev-addr 127.0.0.1:<puerto>` en la terminal.

## Por qué una carpeta

Como en otros ejercicios de este bloque, el ejercicio necesita más de un
archivo (la configuración YAML y el código Python que la utiliza), así que
se agrupan en esta carpeta `ej1a1/`. El código Python se escribe en
`__init__.py` porque es el archivo que se importa al hacer
`import ej1a1` y el que se ejecuta con `python -m ej1a1`.

## Cómo probar tu solución

Desde la carpeta `1a/`:

```bash
python -m pytest ej1a1_test.py -v
```

Para arrancar el servidor de MkDocs, con `mkdocs` instalado, ejecuta desde
la raíz del repositorio:

```bash
mkdocs serve --config-file 1a/ej1a1/mkdocs.yml --dev-addr 127.0.0.1:8000
```

Si tu terminal ya está en `1a/ej1a1/`, ejecuta directamente:

```bash
mkdocs serve --dev-addr 127.0.0.1:8000
```
