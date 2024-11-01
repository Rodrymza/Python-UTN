from matriz import Matriz
from celda import Celda
from funciones import pedir_boolean
class GestorMatriz:
    def __init__(self):
        self.matriz_usuario = Matriz()

    def agregar_celdas(self):

        while True:
            celda = Celda()
            celda.pedir_valores()
            celda.agregar_celda_matriz(self.matriz_usuario)
            if pedir_boolean("Desea agregar mas celdas (s/n)?"):
                break
        print("Total de celdas ingresadas:")
        self.matriz_usuario.mostrar_celdas()
    
        
gestor = GestorMatriz()
gestor.agregar_celdas()