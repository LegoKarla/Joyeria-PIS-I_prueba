# vista.py
from Modelo.G_inventario.Producto import Aretes, Collares, Anillos, Piercings, Pulseras, Dijes

class UI_Inventario:
    def __init__(self, controlador):
        self.controlador = controlador

    def menu_principal(self):
        while True:
            print("\n=== Menú Principal ===")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Buscar producto")
            print("4. Actualizar stock")
            print("5. Mostrar inventario")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.actualizar_stock()
            elif opcion == "5":
                self.mostrar_inventario()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def agregar_producto(self):
        while True:
            print("\nTipos de productos disponibles:")
            print("1. Aretes")
            print("2. Collares")
            print("3. Anillos")
            print("4. Piercings")
            print("5. Pulseras")
            print("6. Dijes")

            tipo_producto = input("Seleccione el tipo de producto: ")

            if tipo_producto not in ["1", "2", "3", "4", "5", "6"]:
                print("Tipo de producto no válido. Inténtelo de nuevo.")
                continue

            # Solicita al usuario ingresar los detalles del producto
            nombre = input("Ingrese el nombre del producto: ")
            modelo = input("Ingrese el modelo del producto: ")
            marca = input("Ingrese la marca del producto: ")
            stock = input("Ingrese la cantidad del producto: ")
            material = input("Ingrese el material del producto: ")
            color = input("Ingrese el color del producto: ")
            piedra = input("Ingrese el tipo de piedra del producto: ")
            precio = input("Ingrese el precio del producto: ")

            # Valida que stock y precio sean números enteros positivos
            if not stock.isdigit() or not precio.isdigit() or int(stock) < 0 or int(precio) < 0:
                print("La cantidad y el precio deben ser números enteros positivos. Inténtelo de nuevo.")
                continue

            stock = int(stock)
            precio = int(precio)

            # Crea una instancia del producto según el tipo seleccionado
            if tipo_producto == "1":
                producto = Aretes(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "2":
                producto = Collares(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "3":
                producto = Anillos(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "4":
                producto = Piercings(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "5":
                producto = Pulseras(nombre, modelo, marca, stock, material, color, piedra, precio)
            elif tipo_producto == "6":
                producto = Dijes(nombre, modelo, marca, stock, material, color, piedra, precio)

            # Agrega el producto al inventario a través del controlador y muestra un mensaje de confirmación
            self.controlador.agregar_producto(producto)
            print("Producto agregado correctamente.")
            break

    def eliminar_producto(self):
        # Solicita al usuario el nombre del producto a eliminar y lo elimina del inventario a través del controlador
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        self.controlador.eliminar_producto(nombre_producto)

    def buscar_producto(self):
        nombre_producto = input("Ingrese el nombre del producto a buscar: ")
        resultado = self.controlador.buscar_producto(nombre_producto)
        print(resultado)

    def actualizar_stock(self):
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        stock = int(input("Ingrese la cantidad adicional: "))
        self.controlador.actualizar_stock(nombre_producto, stock)

    def mostrar_inventario(self):
        inventario = self.controlador.obtener_inventario()
        print("\n=== Inventario ===")
        for nombre_producto, stock in inventario.items():
            print(f"{nombre_producto}: {stock}")


