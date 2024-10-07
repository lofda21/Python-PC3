def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrese de ingresar números."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrese de ingresar números."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrese de ingresar números."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrese de ingresar números."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."
