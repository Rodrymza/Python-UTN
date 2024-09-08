def trasponer_matriz(matriz):
    matriz_traspuesta=[]
    for columna in range(len(matriz[0])):
        lista_aux=[]
        for fila in range(len(matriz)):
            lista_aux.append(matriz[fila][columna])
        matriz_traspuesta.append(lista_aux)
    return matriz_traspuesta
filas, columnas = 4, 5

matriz_consecutiva = [[j + i*columnas for j in range(columnas)] for i in range(filas)]

for _ in matriz_consecutiva:
    print(_)

nueva_matriz=trasponer_matriz(matriz_consecutiva)


print("")
for _ in nueva_matriz:
    print(_)