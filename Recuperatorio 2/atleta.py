class Atleta:
    def __init__(self, nombre: str, tiempoRealizado: int):
        self.nombre = nombre.title()
        self.tiempoRealizado = tiempoRealizado
    
    def __str__(self):
        return f"{self.nombre} con un tiempo de {self.tiempoRealizado}"