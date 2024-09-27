"""Multiplicar cada elemento de la matriz por un numero dado por el usuario"""

import Ejercicio01
matriz = Ejercicio01.crear_matriz(4, 4)

print("Matriz sin modificar:")
Ejercicio01.imprimir_matriz(matriz)
#print(matriz)
escalar = int(input("Ingrese un numero para multiplicar cada elemento de la matriz\n"))
nueva_matriz = []
for filas in range(len(matriz)):
    for elemento in range(len(matriz[0])):
        matriz[filas][elemento]*=escalar

print("Matriz modificada:")
Ejercicio01.imprimir_matriz(matriz)
