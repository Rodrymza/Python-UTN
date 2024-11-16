from ciudad import Ciudad
class DiaViaje:
    def __init__(self, numero_dia) -> None:
        self.numero_dia = numero_dia
        self.lista_de_ciudades = []

    def mostrar_dia(self):
        ciudad: Ciudad
        print(f"Dia {self.numero_dia}")
        for ciudad in self.lista_de_ciudades:
            ciudad.mostrar_cuidad()
        print("".center(20,"-"))


    def calcular_costo_dia(self):
        ciudad: Ciudad
        costo = 0
        for ciudad in self.lista_de_ciudades:
            costo += ciudad.calcular_costo_total()
        return costo
    
    def agregar_ciudad(self, ciudad: Ciudad):
        self.lista_de_ciudades.append(ciudad)
        print(f"Ciudad {ciudad.nombreCiudad} agregada al dia {self.numero_dia}")