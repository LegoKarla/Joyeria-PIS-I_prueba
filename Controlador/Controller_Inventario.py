from Modelo.G_inventario.GestorInventario import GestorInventario
from Vista.UI_Inventario import UI_Inventario

class Controller_Inventario:
    def __init__(self):
        self.GestorInventario = GestorInventario()
        self.UI_Inventario = UI_Inventario(self)

    def iniciar_aplicacion(self):
        self.UI_Inventario.menu_principal()

    def agregar_producto(self, producto):
        self.GestorInventario.agregar_producto(producto)

    def eliminar_producto(self, nombre_producto):
        self.GestorInventario.eliminar_producto(nombre_producto)

    def buscar_producto(self, nombre_producto):
        return self.GestorInventario.buscar_producto(nombre_producto)

    def actualizar_stock(self, nombre_producto, stock):
        self.GestorInventario.actualizar_stock(nombre_producto, stock)

    def obtener_inventario(self):
        return self.GestorInventario.obtener_inventario()
