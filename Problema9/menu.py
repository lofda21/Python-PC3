from figuras import Circulo, Rectangulo, Cuadrado

def validar_numero(num):
    try:
        valor = float(num)
        if valor <= 0:
            raise ValueError("El número debe ser positivo.")
        return valor
    except ValueError as e:
        print(e)
        return None

def menu():
    while True:
        print("\nMenú de Cálculo de Áreas")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            radio = input("Ingrese el radio del círculo: ")
            radio = validar_numero(radio)
            if radio is not None:
                circulo = Circulo(radio)
                print(f"El área del círculo es: {circulo.calcular_area():.2f}")

        elif opcion == '2':
            largo = input("Ingrese el largo del rectángulo: ")
            ancho = input("Ingrese el ancho del rectángulo: ")
            largo = validar_numero(largo)
            ancho = validar_numero(ancho)
            if largo is not None and ancho is not None:
                rectangulo = Rectangulo(largo, ancho)
                print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")

        elif opcion == '3':
            lado = input("Ingrese el lado del cuadrado: ")
            lado = validar_numero(lado)
            if lado is not None:
                cuadrado = Cuadrado(lado)
                print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    menu()
