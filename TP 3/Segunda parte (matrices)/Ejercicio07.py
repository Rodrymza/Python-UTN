"""Programa que extraiga los elementos de la diagonal principal de una matriz"""
import Ejercicio01
matriz = Ejercicio01.crear_matriz(4, 4)
diagonales = []
print("Matriz completa:")
Ejercicio01.imprimir_matriz(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i==j:
            diagonales.append(matriz[i][j])

print("Los elementos de la diagonal principal de la matriz son :", diagonales)