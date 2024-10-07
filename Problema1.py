def Pfraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser 0.")
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = round((x / y) * 100)
            
            if porcentaje <= 1:
                return "E"
            elif porcentaje >= 99:
                return "F"
            else:
                return f"{porcentaje}%"
        
        except ValueError:
            print("Error: Ingrese una fracción válida con números enteros.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0.")

if __name__ == "__main__":
    result = Pfraccion()
    print(result)
