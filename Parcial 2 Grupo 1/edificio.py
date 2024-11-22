from piso import Piso
class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre.title()
        self.total_metros_cubiertos = 0
        self.total_costo_construccion = 0
        self.lista_pisos = []
        
    def mostrar_edificio(self):
        print("Edificio".center(40, "-"))
        print(f"Nombre: {self.nombre}")
        print("Pisos".center(40,"-"))
        piso: Piso
        for piso in self.lista_pisos:
            piso.mostrar_piso()
        self.asignar_totales()
        print("Total metros cuadrados edificio: ", self.total_metros_cubiertos, "m2")
        print("Total costo de construcción: $", self.total_costo_construccion)
        print("Costo promedio por metro cuadrado: $", self.promedio_por_metro())
        
    def calcular_total_metros(self):
        piso: Piso
        total = 0
        for piso in self.lista_pisos:
            total += piso.total_metros_piso()
        return total
    
    def calcular_total_costo(self):
        piso: Piso
        total = 0
        for piso in self.lista_pisos:
            total += piso.total_costo_piso()
        return total
    
    def asignar_totales(self):
        self.total_metros_cubiertos = self.calcular_total_metros()
        self.total_costo_construccion = self.calcular_total_costo()
        
    def promedio_por_metro(self):
        return round(float(self.total_costo_construccion / self.total_metros_cubiertos),2)
    
    def agregar_piso(self, piso: Piso):
        self.lista_pisos.append(piso)
        print(f"Se agrego el Piso {piso.nroPiso} al edificio")
        