"""Crear programa que cree una matriz identidad inversa"""
filas, columnas = 4, 4

matriz = []

for fila in range(filas):
    lista_aux=[]
    for elemento in range(columnas):
        if fila+elemento==3 or fila==elemento:
            lista_aux.append(1)
        else:
            lista_aux.append(0)
    matriz.append(lista_aux)

for _ in matriz:
    print(_)