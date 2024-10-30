#Atributos: calle (cadena), numero (entero), manzana (cadena), nroCasa (entero), 
#superficieTerreno (decimal), lista de objetos Habitacion []
from habitacion import Habitacion
import funciones

class Vivienda:
    def __init__(self):
        self.calle = input("Ingrese nombre de la calle\n").title()
        self.numero = funciones.ingresarNumero("Ingrese numero\n", 1)
        self.manzana = input("Ingrese manzana\n")
        self.nroCasa = funciones.ingresarNumero("Ingrese numero de casa\n", 1)
        self.superficieTerreno = funciones.ingresarNumero("Ingrese superficie total del terreno\n")
        self.listaHabitacion = []
        
    def getMetrosCuadradosCubiertos(self):
        sup_cubierta = 0.0
        for habitacion in self.listaHabitacion:
            sup_cubierta += habitacion.metrosCuadrados
        if sup_cubierta > self.superficieTerreno:
            print("Error, la superficie cubierta no pude ser mayor a la del terreno")
        else:
            return sup_cubierta
    
    def agregarHabitacion(self):
        while True:
            habitacion_actual = Habitacion()
            self.listaHabitacion.append(habitacion_actual)
            if funciones.pedir_boolean("Desea agregar mas habitaciones? (s/n)"):
                break

    


