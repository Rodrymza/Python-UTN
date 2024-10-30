import funciones
class Habitacion:
    def __init__(self):
        self.nombre = input("Ingrese nombre habitacion\n")
        self.metrosCuadrados = funciones.ingresarNumero("Ingrese metros cuadrados de la habitacion\n")
     
    