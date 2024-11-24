class Ambiente:
    def __init__(self, tipo_ambiente: str, metros_cuadrados: int, costo_ambiente:int):
        self.tipo_ambiente = tipo_ambiente
        self.metros_cuadrados = metros_cuadrados
        self.costo_ambiente = costo_ambiente
        
    def mostrar_ambiente(self):
        print(f"{self.tipo_ambiente:<20}{self.metros_cuadrados:<2} metros cuadrados")    