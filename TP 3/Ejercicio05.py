"""Escribir un programa que encuentre el elemento mayor en una lista bidimensional"""

import random
import Ejercicio01
filas, columnas = 4, 4
matriz  = []

for fila in range(filas):
    nuevafila = []
    for columna in range(columnas):
        nuevafila.append(random.randint(0,100))
    matriz.append(nuevafila)
    
Ejercicio01.imprimir_matriz(matriz) 
   
num_mayor = matriz[0][0] #primer elemento como el menor, despues comienza a comparar
for fila in matriz:
    for elemento in fila:
        if elemento > num_mayor:
            num_mayor = elemento 

print("El numero mas grande en la matriz es", num_mayor)