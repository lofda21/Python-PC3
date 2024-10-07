import operaciones

def ejecutar_operaciones():
    print(operaciones.suma(10, 5))
    print(operaciones.resta(10, 5)) 
    print(operaciones.producto(10, 5)) 
    print(operaciones.division(10, 5))   
    print(operaciones.suma(10, 'a'))
    print(operaciones.division(10, 0))

if __name__ == "__main__":
    ejecutar_operaciones()
