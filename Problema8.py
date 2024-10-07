# operaciones.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."


# calculos.py

import operaciones

if __name__ == '__main__':
    print("Suma: ", operaciones.suma(5, 3))  # Ejemplo de suma
    print("Resta: ", operaciones.resta(10, 2))  # Ejemplo de resta
    print("Producto: ", operaciones.producto(4, 3))  # Ejemplo de producto
    print("División: ", operaciones.division(10, 0))  # Ejemplo de división con error
    print("División: ", operaciones.division(10, 2))  # Ejemplo de división exitosa
