from random import randint as aleatorio

def generar_matriz():   #generacion de matriz
    matriz = []
    minimo, maximo = 50, 1000
    filas = int(input("Ingresa la cantidad de filas\n"))
    columnas = int(input("Ingresa la cantidad de columnas\n"))
    
    for _ in range(filas):
        auxiliar_filas = []
        for _ in range(columnas):
                auxiliar_filas.append(aleatorio(minimo, maximo))
        matriz.append(auxiliar_filas)
    return matriz

def mostrar_matriz(matriz): #mostrar matriz por pantalla
    for filas in matriz:
        for elemento in filas:
            print(elemento, end= "\t")
        print("")
        
def lista_cuadrados(matriz):
    matriz_cuadrados = []
    for filas in matriz:
        lista_auxiliar = []
        for elemento in filas:
            lista_auxiliar.append(elemento**2)
        matriz_cuadrados.append(lista_auxiliar)
    return matriz_cuadrados
        
def matriz_sumas(matriz):
    matriz_sumada = []
    n = 1
    for filas in matriz:
        lista_auxiliar = []
        suma = 0 
        for elemento in filas:
            suma += elemento
        lista_auxiliar.append(suma)
        lista_auxiliar.append(n)
        matriz_sumada.append(lista_auxiliar)
        n += 1
        
    return matriz_sumada
        
def ordenar(matriz):    #ordenamiento
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[j] > matriz[i]:
                matriz[j], matriz[i] = matriz[i], matriz[j]
matriz = [[aleatorio(0,10) for i in range(3)] for j in range(3)]
mostrar_matriz(matriz)

print("Matriz cuadrados")

matriz_cuadrados = lista_cuadrados(matriz)

mostrar_matriz(matriz_cuadrados)

print("Matriz sumada")
matriz_sumada = matriz_sumas(matriz)
mostrar_matriz(matriz_sumada)

matriz_ordenada = matriz_sumada

ordenar(matriz_ordenada)

print("Matriz ordenada")
mostrar_matriz(matriz_ordenada)