class Celdas:
    
    fila = 0
    columna = 0
    valor = ""
    
    @staticmethod
    def ingresar_numero():
        while True:
            numero = input("Ingrese un numero\n")
            if numero.isnumeric():
                return int(numero)
            else:
                print("Ingresaste un valor incorrecto")
    def pedir_valores(self):
        print("Ingrese la fila")
        self.fila = self.ingresar_numero()
        print("Ingrese la columna")
        self.columna = self.ingresar_numero()
        self.valor = input(f"Ingrese valor a colocar en la fila {self.fila} columna {self.columna}\n")
        print("Valor ingresado correctamente")
        
    def agregar_matriz(self, matriz):
        matriz.agregar_celdas([self.fila, self.columna, self.valor])
            
    def obtener_valor(self):
        return self.valor
class Matriz:
    matriz = []
    def agregar_celdas(self, valor):
        if valor[2] != "salir":
            self.matriz.append(valor)
    
    def ordenar_matriz(self):
        self.matriz.sort()        
            
    def mostrar_celdas(self):
        self.ordenar_matriz()
        print("Celdas:")
        for elemento in self.matriz:
            print(f"Fila {elemento[0]} Columna: {elemento[1]} Valor: {elemento[2]}")

matriz_usuario = Matriz()

while True:
    celda = Celdas()
    celda.pedir_valores()
    if celda.obtener_valor().lower() == "salir":
        break
    celda.agregar_matriz(matriz_usuario)

matriz_usuario.mostrar_celdas()