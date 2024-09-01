#las clases permiten crear objetos que combinan datos y funcionalidades
#puede ser tomado como una "plantilla" 

#Sintaxis

class Persona:
    def __init__(self, nombre, edad):   #Constructor del objeto
        self.nombre= nombre
        self.edad= edad
        
        #el objeto es cada instancia de la clase
        
def saludar(self):
    print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad}")
        
persona1 = Persona("Rodrigo",32)
persona2 = Persona("Rocio",29)

saludar(persona2)