"""Sumas de cada una de las filas de una matriz"""

import Ejercicio01

matriz = Ejercicio01.crear_matriz(4,4)

for filas in matriz:
    print(f"La suma de la fila {filas} es {sum(filas)}")
