class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    def display(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}, Edad: {self.edad}, Nota: {self.nota}")
    def setAge(self, edad):
        self.edad = edad
    def setNota(self, nota):
        self.nota = nota

if __name__ == '__main__':
    estudiante = Alumno("Grover", "2003")
    estudiante.setAge(22)
    estudiante.setNota(18)
    estudiante.display()
