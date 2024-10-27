class Celdas:
    def __init__(self):
        self.fila = 0
        self.columna = 0
        self.valor = ""
        
    def ingresar_numero(self, mensaje = "Ingrese un numero"):
        while True:
            numero = input(f"{mensaje} \n")
            if numero.isnumeric():
                return int(numero)
            else:
                print("Ingresaste un valor incorrecto")
    
    def pedir_valores(self):
        self.fila = self.ingresar_numero("Ingrese la fila")
        self.columna = self.ingresar_numero("Ingrese la columna")
        
    def agregar_matriz(self, matriz):
        if not matriz.celda_ocupada(self.fila, self.columna):
            self.valor = input(f"Ingrese valor a colocar en la fila {self.fila} columna {self.columna}\n")
            print("Valor ingresado correctamente")

            matriz.agregar_celda([self.fila, self.columna, self.valor])
        else:
            print("Esta celda ya se encuentra ocupada")
            
    def obtener_valor(self):
        return self.valor
    

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
            print(f"Fila {elemento[0]} Columna: {elemento[1]} Valor: {elemento[2]}")
            
   
def main():
    matriz_usuario = Matriz()

    while True:
        celda = Celdas()
        celda.pedir_valores()
        if celda.obtener_valor().lower() == "fin":
            break
        celda.agregar_matriz(matriz_usuario)

    matriz_usuario.mostrar_celdas()
    
if __name__ == "__main__":
    main()