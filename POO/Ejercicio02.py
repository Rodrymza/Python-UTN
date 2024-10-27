class Nota:
    def __init__(self, catedra, notaexamen):
        self.catedra = catedra
        self.notaexamen = float(notaexamen)
        
class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombre_completo = nombreCompleto
        self.legajo = legajo
        self.lista_notas = []
        
    def getNombre(self):
        return self.nombre_completo
    
    def calcular_promedio(self):
        suma = 0
        for nota in self.lista_notas:
            suma += nota.notaexamen
        return round(suma/len(self.lista_notas),2)
            
    def agregar_nota(self, nota):
        self.lista_notas.append(nota)
        
class CargarNotas:
    def __init__(self):
        self.lista_alumnos = []
    
    def main(self):
        while True:
            nombre = self.pedir_nombre("Ingrese nombre del alumno:\n")
            if nombre is None:
                break
            legajo = int(self.pedir_numero("Ingrese legajo del alumno\n", 1, 200))
            alumno_actual = Alumno(nombre, legajo)

            notas_ingresadas = 0
            while True:
                materia = self.pedir_nombre("Ingrese nombre de la materia:\n")
                if materia is None:
                    if notas_ingresadas == 0:
                        print("Debe ingresar al menos una nota")
                        continue
                    else:
                        break
                
                nota = float(self.pedir_numero(f"Ingrese nota de {materia}\n", 1, 10))
                notas_ingresadas += 1
                alumno_actual.agregar_nota(Nota(materia, nota))
                
            self.lista_alumnos.append(alumno_actual)
        
    def pedir_nombre(self, mensaje, ):
        nombre = input(mensaje).title()
        if nombre == "Salir":
            print("")
            return None
        return nombre
    
    def pedir_numero(self, mensaje, minimo =float("-inf"), maximo = float("inf")):
        while True:
            ingreso = input(mensaje)
            try:
                numero = float(ingreso)
                if numero >= minimo and numero <= maximo:
                    return numero
                else:
                    print(f"Valor fuera de rango ({minimo}-{maximo})")
            except:
                print("No ingresaste un numero valido")
    
    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            print(f"{alumno.getNombre()} Promedio: {alumno.calcular_promedio()}")
            for materia in alumno.lista_notas:
                print(f"{materia.catedra}: {materia.notaexamen}")

notas_escuela = CargarNotas()
notas_escuela.main()
notas_escuela.mostrar_alumnos()