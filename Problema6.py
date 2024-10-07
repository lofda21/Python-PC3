class Producto:
    def __init__(self, nombre, año, precio):
        self.nombre = nombre
        self.año = año
        self.precio = precio
    def __str__(self):
        return f"Producto: {self.nombre}, Año: {self.año}, Precio: {self.precio}"

class Catalogo:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]
    def filtrar_por_precio_max(self, precio_max):
        return [producto for producto in self.productos if producto.precio <= precio_max]

if __name__ == '__main__':
    prod1 = Producto("Aceite", 2024, 25.50)
    prod2 = Producto("Filtro de Aire", 2023, 45.00)
    prod3 = Producto("Pastillas", 2023, 15.00)

    catalogo = Catalogo()
    catalogo.agregar_producto(prod1)
    catalogo.agregar_producto(prod2)
    catalogo.agregar_producto(prod3)

    print("Todos los productos en el catálogo:")
    catalogo.mostrar_productos()

    print("\nProductos del año 2023:")
    productos_2023 = catalogo.filtrar_por_año(2023)
    for producto in productos_2023:
        print(producto)

    print("\nProductos con precio menor o igual a 30:")
    productos_baratos = catalogo.filtrar_por_precio_max(30)
    for producto in productos_baratos:
        print(producto)
