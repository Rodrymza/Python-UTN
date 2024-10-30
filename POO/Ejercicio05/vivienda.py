#Atributos: calle (cadena), numero (entero), manzana (cadena), nroCasa (entero), 
#superficieTerreno (decimal), lista de objetos Habitacion []
from habitacion import Habitacion
class Vivienda:
    def __init__(self):
        self.calle = input("Ingrese nombre de la calle\n").title()
        self.numero = ingresarNumero("Ingrese numero\n", 1)
        self.manzana = input("Ingrese manzana\n")
        self.nroCasa = ingresarNumero("Ingrese numero de casa\n", 1)
        self.superficieTerreno = ingresarNumero("Ingrese superficie total del terreno\n")
        self.listaHabitacion = []
        self.agregarHabitacion()
        
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
            if pedir_boolean("Desea agregar mas habitaciones?"):
                break
    
def ingresarNumero(mensaje, valor = 0):
    """valor predeterminado valida decimal, coloca 1 para validar entero"""
    while True:
        ingreso = input(mensaje)
        try:
            precio = float(ingreso) if valor == 0 else int(ingreso)
            return precio
        except:
            print("El valor ingresado no es valido\n")
def pedir_boolean(mensaje, valores = ["s", "n"]):   #valores invertidos 0 1 para funcionalidad de pregunta
    while True:
        ingreso = input(mensaje).lower()
        if ingreso in valores:
            return valores.index(ingreso)
        else:
            print("Respuesta incorrecta")   

