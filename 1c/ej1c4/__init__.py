"""
Enunciado:
Documentación automatizada con tipado estático (typing), mkdocstrings y
docstrings en formato Google.

Cuando una función o método ya tiene anotaciones de tipo (type hints), el
plugin "mkdocstrings" es capaz de mostrar automáticamente esos tipos en la
documentación generada, por lo que **no hace falta repetirlos** dentro del
docstring. Por ejemplo, en formato Google, en lugar de escribir:

    Args:
        nombre (str): el nombre del producto.

cuando ya existe la anotación "nombre: str" en la firma de la función,
basta con escribir:

    Args:
        nombre: el nombre del producto.

En este ejercicio vas a completar un pequeño paquete ("ej1c4/", el propio
directorio donde se encuentra este archivo) que modela el inventario de
una tienda, usando el módulo "typing" para anotar los tipos y docstrings
en formato Google que no dupliquen esa información.

Tu tarea es completar, en este archivo ("__init__.py"):

1. La clase "Producto", con sus atributos anotados ("nombre: str",
   "precio: float", "stock: int") y sus métodos:
   - "__init__": inicializa el producto con stock 0 por defecto.
   - "vender(cantidad: int) -> bool": descuenta stock si hay suficiente y
     devuelve True; si no hay stock suficiente, no modifica nada y
     devuelve False.
2. La función "buscar_producto(productos: List[Producto], nombre: str) ->
   Optional[Producto]", que devuelve el primer producto cuyo nombre
   coincida, o "None" si no se encuentra ninguno.
3. La función "valor_total_inventario(productos: List[Producto]) ->
   float", que devuelve la suma de "precio * stock" de todos los
   productos.

Todas las funciones y métodos deben tener:
- Anotaciones de tipo completas (parámetros y valor de retorno), usando
  "List" y "Optional" del módulo "typing".
- Un docstring en formato Google (con las secciones "Args:"/"Attributes:"
  y "Returns:" según corresponda) que **no repita los tipos** ya indicados
  mediante las anotaciones.

Consulta también "ej1c4.yml", donde deberás configurar las opciones de
"mkdocstrings" para que se muestren estas anotaciones de tipo en la
documentación generada.
"""

# TODO: importa "List" y "Optional" desde "typing".
from typing import List, Optional


class Producto:
    """
    Esta clase representa un producto en el inventario de la tienda.
    Attributes:
        nombre: el nombre del producto.
        precio: el precio unitario del producto.
        stock: la cantidad disponible en inventario.

    """

    def __init__(self, nombre: str, precio: float, stock: int = 0):
        """
        Inicializa un producto con un nombre, precio y cantidad en stock.

        Args:
            nombre: el nombre del producto.
            precio: el precio unitario del producto.
            stock: la cantidad disponible en inventario.
        """
        # TODO: guarda "nombre", "precio" y "stock" como atributos.
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        pass

    def vender(self, cantidad: int) -> bool:
        """
        Este método intenta vender una cantidad de este producto, descontando
        del stock si hay suficiente.

        Args:
            cantidad: Cantidad de unidades que se intenta vender.

        Returns:
            True si hay stock suficiente y se realiza la venta; False en caso contrario.
        """
        # TODO: si no hay stock suficiente ("cantidad" > "stock"), no
        # modifiques nada y devuelve False.
        if cantidad > self.stock:
            return False
        else:
            self.stock -= cantidad
            return True


def buscar_producto(productos: List[Producto], nombre: str) -> Optional[Producto]:
    """
    Este método busca un producto por nombre en la lista de productos.
    Args:
        productos: lista de productos a buscar.
        nombre: nombre del producto a buscar.
    Returns:
        El primer producto cuyo nombre coincida con "nombre", o "None" si no
        se encuentra ninguno.
    """
    # TODO: devuelve el primer producto de "productos" cuyo nombre
    # coincida con "nombre", o "None" si no se encuentra ninguno.
    for producto in productos:
        if producto.nombre == nombre:
            return producto
    return None
    pass


def valor_total_inventario(productos: List[Producto]) -> float:
    """
    Este método calcula el valor total del inventario, sumando el precio
    multiplicado por el stock de cada producto.
    Args:
        productos: lista de productos a evaluar.
    Returns:
        La suma de "precio * stock" de todos los productos, o 0.0 si la lista está vacía.
    """
    # TODO: devuelve la suma de "precio * stock" de todos los productos de
    # "productos" (0.0 si la lista está vacía).
    total = 0.0
    for producto in productos:
        total += producto.precio * producto.stock
    return total
