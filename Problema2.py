def get_grades():
    while True:
        try:21,56,1
        
            grades_input = input("Ingrese las calificaciones separadas por comas: ")
            grades_list = [int(grade.strip()) for grade in grades_input.split(',')]
            return grades_list
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

if __name__ == '__main__':
    grades = get_grades()
    print(f"Las calificaciones son: {grades}")
