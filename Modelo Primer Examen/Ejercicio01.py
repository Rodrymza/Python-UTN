import random

def generar_matriz():   #generacion de matriz
    matriz = []
    minimo, maximo = 0, 100
    filas = int(input("Ingresa la cantidad de filas\n"))
    columnas = int(input("Ingresa la cantidad de columnas\n"))
    opcion = input("Seleccione tipo de carga: \n 1 Manual \n 2 Automatico\n")
    for i in range(filas):
        auxiliar_filas = []
        for j in range(columnas):
            if opcion == "2":
                auxiliar_filas.append(random.randint(minimo, maximo))
            else:
                auxiliar_filas.append(input("Ingresa un valor: "))
        matriz.append(auxiliar_filas)
    return matriz

def mostrar_matriz(matriz): #mostrar matriz por pantalla
    for filas in matriz:
        for elemento in filas:
            print(elemento, end= "\t")
        print("")
    
def promedio(lista): #Calcular promedio de una lista
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma/len(lista)

def sacar_promedios(matriz):    #sacar promedio por fila y crear nueva matriz
    promedios = []
    n=1
    for filas in matriz:
        lista_auxiliar = []
        lista_auxiliar.append(promedio(filas))
        lista_auxiliar.append(n)
        promedios.append(lista_auxiliar)
        n += 1
    return promedios

def ordenar(matriz):    #ordenamiento
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[j] < matriz[i]:
                matriz[j], matriz[i] = matriz[i], matriz[j]
    
#matriz = generar_matriz()
matriz = [[random.randint(0,50) for i in range(4)] for j in range(4)]
print("Matriz original")
mostrar_matriz(matriz)

promedios = sacar_promedios(matriz)
print("Matriz promedios")
mostrar_matriz(promedios)

promedios_ordenados = promedios
ordenar(promedios_ordenados)

print("Promedios ordenados")
mostrar_matriz(promedios_ordenados)