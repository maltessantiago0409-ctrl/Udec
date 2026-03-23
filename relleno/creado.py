class Estudiante:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_resultado(self):
        print("Estudiante:", self.nombre)
        print("Nota:", self.nota)

        if self.nota >= 3:
            print("Resultado: Aprobo")
        else:
            print("Resultado: Reprobo")


estudiantes = [
    Estudiante("Ana", 4.5),
    Estudiante("Luis", 2.8),
    Estudiante("Carlos", 3.7),
    Estudiante("Maria", 1.9)
]

for estudiante in estudiantes:
    estudiante.mostrar_resultado()
    print("--------------------")