filas, columnas = 4, 4

matriz_consecutiva = [[j + i*columnas for j in range(columnas)] for i in range(filas)]

def trasponer_matriz(matriz): #trasponer los elementos de una matriz y devolver una matriz nueva
    matriz_traspuesta=[]
    for columna in range(len(matriz[0])):
        lista_aux=[]
        for fila in range(len(matriz)):
            lista_aux.append(matriz[fila][columna])
        matriz_traspuesta.append(lista_aux)
    return matriz_traspuesta

def es_matriz_simetrica(matriz): #verificar si las matrices son iguales devolver mensaje si es simetrica o no
    matriz_traspuesta=trasponer_matriz(matriz)
    if matriz==matriz_traspuesta:
        print(f"La matriz es simetrica")
    else:
        print(f"La matriz no es simetrica")

#llenando matriz con 1 diagonales
matriz_diagonales = []
for fila in range(filas):
    lista_aux=[]
    for elemento in range(columnas):
        if fila+elemento == len(matriz_consecutiva)-1 or fila == elemento:
            lista_aux.append(1)
        else:
            lista_aux.append(0)
    matriz_diagonales.append(lista_aux)

print("Matriz de diagonales:")
for _ in matriz_diagonales:
    print(_)

print("Matriz consecutiva:")
for _ in matriz_consecutiva:
    print(_)

print("Verificamos primero la matriz consecutiva:")
es_matriz_simetrica(matriz_consecutiva)

print("Verificamos primero la matriz diagonales:")
es_matriz_simetrica(matriz_diagonales)