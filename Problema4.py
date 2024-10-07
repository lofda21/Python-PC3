class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    # Crear objeto de tipo Rectangulo
    rectangulo = Rectangulo(4, 8)
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")

    # Crear objeto de tipo Cuadrado
    cuadrado = Cuadrado(5)
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
