class Actividad:
    def __init__(self, tipo_actividad: str, tipo: str, costo_actividad: float) -> None:
        self.tipo_actividad = tipo_actividad
        self.tipo = tipo
        self.costo_actividad = costo_actividad

    def mostrar_actividad(self):
        print(f"{self.tipo_actividad.ljust(15)}       {self.tipo.ljust(8)}     ${self.costo_actividad}")

    