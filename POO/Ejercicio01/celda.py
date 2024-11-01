import funciones
class Celda:
    def __init__(self):
        self.fila = 0
        self.columna = 0
        self.valor = ""
    
    def pedir_valores(self):
        self.fila = funciones.ingresarNumero("Ingrese la fila\n", 1)
        self.columna = funciones.ingresarNumero("Ingrese la columna\n", 1)
        
    def agregar_celda_matriz(self, matriz):
        if not matriz.celda_ocupada(self.fila, self.columna):
            self.valor = input(f"Ingrese valor a colocar en la fila {self.fila} columna {self.columna}\n")
            print(f"Valor {self.valor} ingresado correctamente ({self.fila}, {self.columna})")
            matriz.agregar_celda([self.fila, self.columna, self.valor])
        else:
            print("Esta celda ya se encuentra ocupada")
