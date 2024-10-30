import vivienda
class Habitacion:
    def __init__(self):
        self.nombre = input("Ingrese nombre habitacion\n")
        self.metrosCuadrados = vivienda.ingresarNumero("Ingrese metros cuadrados de la habitacion\n")
     
    