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
        lista_suma = []
        for elemento in filas:
            suma += elemento
        lista_suma.append(suma)
        matriz_suma.append(lista_suma)
    
    return matriz_suma        
            

print("Ingrese el numero de filas ")
filas = pedir_valores(filas_min)
print("Ingrese el numero de columnas")
columnas = pedir_valores(columnas_min)

ingreso = ""
print("¿Desea colocar los valores automaticamente o de forma manual?")
print("1 Manual")
print("2 Automatico")
while ingreso!="1" and ingreso!="2":
    ingreso = str(input())
    match ingreso:
        case "1" | "2": matriz_numeros = crear_matriz(filas, columnas, ingreso) 
        
        case _: print("Opcion incorrecta (1-2)")
        
mostrar_matriz(matriz_numeros)

filas_sumadas = sumar_filas(matriz_numeros)

mostrar_matriz(filas_sumadas)
lista_auxiliar = []
for fila in filas_sumadas:
    for elemento in fila:
        lista_auxiliar.append(elemento)
    lista_auxiliar.sort(reverse = True)

matriz_nueva = []

for elemento in lista_auxiliar:
    matriz_nueva
    
print("nueva matriz")
mostrar_matriz(matriz_nueva)