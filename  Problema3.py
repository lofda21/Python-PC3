import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

if __name__ == '__main__':
    # Crear dos objetos de tipo Circulo
    circulo1 = Circulo(5)
    circulo2 = Circulo(7)

    # Calcular y mostrar el área de ambos círculos
    print(f"Área del círculo 1: {circulo1.calcular_area():.2f}")
    print(f"Área del círculo 2: {circulo2.calcular_area():.2f}")
