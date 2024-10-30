from vivienda import Vivienda
from vivienda import pedir_boolean
class Barrio:
    def __init__(self):
        self.nombre = input("Ingrese nombre del barrio\n").title()
        self.empresaConstructora = input("Ingrese nombre de la empresa constructora\n").title()
        self.listaViviendas = []
        
    def getSuperficieTotalTerreno(self, manzana = 0):   #uso el la misma funcion para sumar terrenos por manzana getSuperficieTotalTerrenoXManzana(manzana)
        superficie_total = 0.0
        for vivienda in self.listaViviendas:
            if manzana != 0:
                if vivienda.manzana == manzana:
                    superficie_total += vivienda.superficieTerreno
                else:
                    superficie_total += vivienda.superficieTerreno
        return superficie_total
    
    def getSuperficieTotalCubierta(self):
        sup_cubierta = 0.0
        for vivienda in self.listaViviendas:
            sup_cubierta += vivienda.getMetrosCuadradosCubiertos()
            
    def agregarVivienda(self):
        while True:
            vivienda_actual = Vivienda()
            vivienda_actual.agregarHabitacion()
            self.listaViviendas.append(vivienda_actual)
            if pedir_boolean("Desea agregar otra vivienda?"):
                break