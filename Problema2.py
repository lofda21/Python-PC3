def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
            calificaciones_str = entrada.split(',')
            calificaciones = [int(calificacion.strip()) for calificacion in calificaciones_str]
            return calificaciones
        
        except ValueError:
            print("Error: Asegúrese de que todas las calificaciones sean números enteros separados por comas.")

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    print("Las calificaciones ingresadas son:", calificaciones)
