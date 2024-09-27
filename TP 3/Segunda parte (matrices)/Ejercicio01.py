"""Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
debe  generar  una  matriz  de  ese  tamaño,  donde  los  valores  son  números  enteros 
consecutivos empezando desde 1."""

def crear_matriz(filas: int,columnas: int):
    "Crear matriz con n filas y columnas"
    matriz=[[j + i*columnas for j in range(1,columnas+1)] for i in range(filas)]
    return matriz

#funcion usada para mostrar mastriz por pantalla
def imprimir_matriz(matriz_param: list):
    "Imprimir matriz en pantalla"
    for _ in matriz_param:
        print(_)
