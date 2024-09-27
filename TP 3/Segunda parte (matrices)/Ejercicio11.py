"""Rotar una matriz 90 grados en sentido de las agujas del reloj"""

#misma funcion que para trasponer matriz, solo que los elementos individuales de las listas auxiliares
#se van agregando en orden inverso
import Ejercicio01
def girar_matriz(matriz):
    matriz_traspuesta=[]
    for columna in range(len(matriz[0])):
        lista_aux=[]
        for fila in range(len(matriz)):
            lista_aux.insert(0, matriz[fila][columna])
        matriz_traspuesta.append(lista_aux)
    return matriz_traspuesta

matriz = Ejercicio01.crear_matriz(4,4)

print("Matriz original")
Ejercicio01.imprimir_matriz(matriz)

print("")
print("Matriz girada")
matriz=girar_matriz(matriz)

Ejercicio01.imprimir_matriz(matriz)