class Alumno:
    def __init__(self, nombre, apellido, legajo):   #constructor de clase
        self.nombre = nombre
        self.apellido = apellido    #atributos comunes
        self.legajo = legajo    #atributo unico de la clase
        
    def mostrar_datos(self):    #metodo
        print(f"Nombre {self.nombre} {self.apellido} Legajo: {self.legajo}")
        
alumno1 = Alumno("Juan", "Alonso", 25000)

alumno1.mostrar_datos()

"""Encapsulamiento: todo lo que haga referencia a la clase se trate dentro de la misma clase (metodos y atributos)
y no debe exponerse. Esto se logra ocultando los atributos
Herencia: se crean nuevas clases a partir de clases ya existentes
Polimorfismo: diferentes clases pueden ser tratadas como si fueran del mismo tipo a traves de metodos con el mismo nombre (debe haber herencia primero)
Abstraccion: tratar de modelar todos los objetos a traves de la clase, agrupar todos los atributos unicos en los objetos"""