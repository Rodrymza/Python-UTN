
from diaViaje import DiaViaje
class PaqueteViaje:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.total_costo_viaje = 0
        self.lista_de_dias = []

    def calcular_costo_viaje(self):
        dia: DiaViaje
        for dia in self.lista_de_dias:
            self.total_costo_viaje += dia.calcular_costo_dia()
    
    def maximo_por_paquete(self, maximo: float):
        return self.calcular_costo_viaje() <= maximo
    
    def mostrar_paquete(self):
        self.calcular_costo_viaje()
        print(f"Paquete de viaje: {self.nombre}")
        print(("".center(30,"-")))
        dia: DiaViaje
        for dia in self.lista_de_dias:
            dia.mostrar_dia()
        print(f"Costo total del paquete ${self.total_costo_viaje}")  

    def agregar_dia(self, dia: DiaViaje):
        self.lista_de_dias.append(dia)
        print(f"Se agrego el dia {dia.numero_dia} correctamente")  

