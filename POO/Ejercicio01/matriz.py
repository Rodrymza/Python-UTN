class Matriz:
    def __init__(self):
        self.matriz = []
        
    def celda_ocupada(self, fila, columna):
        for celda in self.matriz:
            if celda[0] == fila and celda[1] == columna:
                return True
        return False
    
    def agregar_celda(self, valor):
        if valor[2] != "fin":
            self.matriz.append(valor)
    
    def ordenar_matriz(self):
        self.matriz.sort()        
            
    def mostrar_celdas(self):
        self.ordenar_matriz()
        print("Celdas:")
        for elemento in self.matriz:
            print(f"Fila: {elemento[0]} Columna: {elemento[1]} Valor: {elemento[2]}")