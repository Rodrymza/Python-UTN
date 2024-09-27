"""Programa que calcula la traspuesta de una matriz"""
import Ejercicio01
matriz = Ejercicio01.crear_matriz(3,3)

Ejercicio01.imprimir_matriz(matriz)

for columna in range(len(matriz[0])):
    suma=0
    for fila in range(len(matriz)):
        "Impresion de matriz por pantalla"
        suma+=matriz[fila][columna]
    print(f"La suma de la columna {columna} es {suma}")
