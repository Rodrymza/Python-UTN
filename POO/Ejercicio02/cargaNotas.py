from alumno import Alumno
from nota import Nota

class CargaNotas:
    def __init__(self):
        self.lista_alumnos = []
    
    def agregar_alumno(self):
        while True:
            alumno_actual = Alumno(self.pedir_string("Ingrese nombre del alumno"),self.pedir_entero("Ingrese legajo del alumno"))
            while True:
                materia = self.pedir_string("Ingrese nombre de la materia:")
                nota = self.pedir_nota(materia)
                alumno_actual.agregar_nota(Nota(materia, nota))
                if not self.pedir_boolean("Desea agregar otra nota?"):
                    break
            self.lista_alumnos.append(alumno_actual)
            alumno_actual.mostrar_notas()
            if not self.pedir_boolean("Desea agregar mas alumnos?"):
                break


    def pedir_nota(self, materia):
            while True:
                nota = float(self.pedir_entero(f"Ingrese nota de {materia}"))
                if nota>0 and nota <=10:
                    return nota
                else:
                    print("Ingresaste una nota incorrecta")
        
    def pedir_string(self, mensaje):
        while True:
            nombre = input(mensaje + "\n").title()
            if nombre:
                return nombre
            else:
                print("Debe ingresar un nombre")           
    
    def pedir_entero(self, mensaje):
        while True:
            ingreso = input(mensaje + "\n")
            try:
                numero = int(ingreso)
                return numero
            except:
                print("No ingresaste un numero valido")
    
    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            alumno.mostrar_notas()
                
    def pedir_boolean(self, mensaje):
        while True:
            ingreso = input(mensaje + "\n")
            match ingreso:
                case "s" : return True
                case "n": return False
                case _: print("Respuesta incorrecta")
                
def main():
    cargar_notas = CargaNotas()
    cargar_notas.agregar_alumno()
    
if __name__ == "__main__":
    main()
    