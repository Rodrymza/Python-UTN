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
        return float(round(suma/len(self.lista_notas),2))
            
    def agregar_nota(self, nota):
        self.lista_notas.append(nota)
    
    def mostrar_notas(self):
        print(f"Alumno: {self.nombre_completo}")
        for elemento in self.lista_notas:
            print(f"{elemento.catedra}: {elemento.notaexamen}")
        print(f"Promedio: {self.calcular_promedio()}")