from Modelo.G_inventario.Inventario import Inventario

class GestorInventario:
    def __init__(self):
        self.Inventario = Inventario()

    def agregar_producto(self, producto):
        self.Inventario.agregar_producto(producto)

    def eliminar_producto(self, nombre_producto):
        self.Inventario.eliminar_producto(nombre_producto)

    def buscar_producto(self, nombre_producto):
        return self.Inventario.buscar_producto(nombre_producto)

    def actualizar_stock(self, nombre_producto, stock):
        self.Inventario.actualizar_stock(nombre_producto, stock)

    def obtener_inventario(self):
        return self.Inventario.obtener_inventario()
