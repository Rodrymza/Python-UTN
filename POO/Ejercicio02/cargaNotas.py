from alumno import Alumno
from nota import Nota

class CargaNotas:
    def __init__(self):
        self.lista_alumnos = []
    
    def agregar_alumno(self):
        while True:
            alumno_actual = Alumno(self.pedir_nombre(),self.pedir_entero("Ingrese legajo del alumno"))
            while True:
                materia = self.pedir_nombre("Ingrese nombre de la materia:\n")
                nota = self.pedir_nota(materia)
                alumno_actual.agregar_nota(Nota(materia, nota))
                if not self.pedir_boolean("Desea agregar otra nota?"):
                    break
            self.lista_alumnos.append(alumno_actual)
            if not self.pedir_boolean("Desea agregar mas alumnos?"):
                break

    def pedir_nota(self, materia):
            while True:
                nota = float(self.pedir_numero(f"Ingrese nota de {materia}\n"))
                if nota>0 and nota <=10:
                    return nota
                else:
                    print("Ingresaste una nota incorrecta")
        
    def pedir_nombre(self):
        while True:
            nombre = input("Ingrese nombre del alumno")
            if nombre:
                return nombre
            else:
                print("Debe ingresar un nombre")           
    
    def pedir_entero(self, mensaje):
        while True:
            ingreso = input(mensaje + "\n.")
            try:
                numero = int(ingreso)
                return numero
            except:
                print("No ingresaste un numero valido")
    
    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            print(f"{alumno.getNombre()} Promedio: {alumno.calcular_promedio()}")
            for materia in alumno.lista_notas:
                print(f"{materia.catedra}: {materia.notaexamen}")
                
    def pedir_boolean(self, mensaje):
        while True:
            ingreso = input(mensaje + "\n")
            match ingreso:
                case "s" : return True
                case "n": return False
                case _: print("Respuesta incorrecta")
                

cargar_notas = CargaNotas()
cargar_notas.agregar_alumno()