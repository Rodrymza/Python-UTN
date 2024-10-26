class Alumno:
    def __init__(self, nombre, apellido, legajo):   #constructor de clase
        self.nombre = nombre
        self.apellido = apellido    #atributos comunes
        self.legajo = legajo    #atributo unico de la clase
        
    def mostrar_datos(self):    #metodo
        print(f"Nombre {self.nombre} {self.apellido} Legajo: {self.legajo}")
        
alumno1 = Alumno("Juan", "Alonso", 25000)

alumno1.mostrar_datos()