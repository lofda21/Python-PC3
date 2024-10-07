import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio
   
    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser números positivos.")
        self.largo = largo
        self.ancho = ancho
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
