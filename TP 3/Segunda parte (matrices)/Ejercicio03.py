"""Sumas de cada una de las filas de una matriz"""

from  Ejercicio01 import crear_matriz

matriz = crear_matriz(4,4)

for filas in matriz:
    print(f"La suma de la fila {filas} es {sum(filas)}")
