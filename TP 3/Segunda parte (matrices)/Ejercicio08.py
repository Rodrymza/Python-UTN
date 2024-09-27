"""Crear un programa que llene una matriz con los elementos en la diagonal principal sean 1 y el resto 0"""
num=5
filas, columnas = num, num

matriz = []

for fila in range(filas):
    lista_aux=[]
    for elemento in range(columnas):
        lista_aux.append(1) if  fila==elemento else lista_aux.append(0)
    matriz.append(lista_aux)

for _ in matriz:
    print(_)