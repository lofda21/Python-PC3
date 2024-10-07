def get_fuel_percentage():
    while True:
        try:
            # Solicitar fracción al usuario
            fraction = input("Ingrese la fracción X/Y: ")
            # Dividir la fracción en X e Y
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)

            # Verificar que Y no sea cero y que X no sea mayor que Y
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError("X no puede ser mayor que Y.")
            
            # Calcular el porcentaje
            percentage = (x / y) * 100

            # Retornar resultado basado en el porcentaje
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{round(percentage)}%"
        
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar números enteros y que X sea menor o igual a Y.")
        except ZeroDivisionError:
            print("Error: Y no puede ser cero.")

if __name__ == '__main__':
    print(get_fuel_percentage())
