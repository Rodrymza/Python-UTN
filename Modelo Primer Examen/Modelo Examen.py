lista_decimales = []
filas_min = 3
columnas_min = 2
import random

def pedir_valores(valor_min):
    valor = 0
    while valor < valor_min:
        valor = int(input("Ingresa el valor: "))
        if valor < valor_min:
            print("El numero debe ser mayor o igual a 3")
    return valor

def crear_matriz(filas,columnas, opcion):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            if opcion == "2":
                fila.append(round(random.uniform(1.00,999.99),2))
            else:
                numero = 0
                while numero < 1 or numero > 999:
                    numero = float(input("Ingresa un valor decimal(1-999): "))
                    if numero > 999 or numero < 1:
                        print("Valor incorrecto")
        matriz.append(fila)
    return matriz
            
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def sumar_filas(matriz):
    matriz_suma = []
    for filas in matriz:
        suma = 0
        for elemento in filas:
            suma += elemento
        matriz_suma.append([round(suma,2)])
    return matriz_suma        

def agregar_columna(matriz):
    i=1
    for filas in matriz:
            filas.append(i)
            i += 1    
    ordenar(matriz)
    return matriz

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar

#pedir valores de columnas y filas
#print("Ingrese el numero de filas ")
#filas = pedir_valores(filas_min)
#print("Ingrese el numero de columnas")
#columnas = pedir_valores(columnas_min)
filas, columnas = 5, 5
print("¿Desea colocar los valores automaticamente o de forma manual?")
print("1 Manual")
print("2 Automatico")

ingreso = "2"
while ingreso not in ("1","2"):    
    print("Opcion incorrecta (1-2)")
    ingreso = input()

matriz_numeros = crear_matriz(filas, columnas,ingreso)
print("Matriz original:")    
mostrar_matriz(matriz_numeros)

filas_sumadas = sumar_filas(matriz_numeros)
print("Filas sumadas")
mostrar_matriz(filas_sumadas)

print("Columna agregada de posicion inicial:")
matriz_indice = agregar_columna(filas_sumadas)
mostrar_matriz(matriz_indice)