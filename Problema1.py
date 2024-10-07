def get_fuel_percentage():
    while True:
        try:
            fraction = input("Ingrese la fracción X/Y: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError("X no puede ser mayor que Y.")
            percentage = (x / y) * 100
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
