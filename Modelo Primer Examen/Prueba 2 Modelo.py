def verificacion_numerica(ingreso):
    bandera = True
    while bandera:
        try:
            ingreso = int(ingreso)
            bandera = False
        except:
            ingreso = input("No ingresaste un valor numerico, ingresa nuevamente\n")
    return ingreso

def ingreso_dato( minimo,nombre):
    numero = 0
    while numero < minimo:
        numero = input(f"Ingrese el numero de {nombre}\n")
        numero = verificacion_numerica(numero)
        if numero < minimo:
            print(f"Ingresa un numero mayor a {minimo}\n")
    return numero

def crear_matriz(filas, columnas):
    opcion = input("Seleccione generacion: \n1 Automatica \n2 Manual\n")
    while opcion not in ("1", "2"):
        opcion = input("Opcion invalida, seleccione correctamente (1-2)")
    if opcion == "1":
        import random
        matriz = [[random.randint(0,1000) for i in range(filas)] for j in range(columnas)]
    else:
        matriz = [[int(input("Ingrese un numero\n")) for i in range(filas)]for j in range(columnas)]
    return matriz
def mostrar_matriz(matriz):
    for filas in matriz:
        print(*filas,sep = "\t")
        
def sumar_filas(matriz):
    filas_sumadas = []
    for filas in matriz:
        suma = 0
        for elemento in filas:
            suma += elemento
        fila_auxiliar = []
        fila_auxiliar.append(suma)
        filas_sumadas.append(fila_auxiliar)
    return filas_sumadas

def agregar_columna(matriz):
    n=1
    for filas in matriz:
       filas.append(n)
       n += 1 
       
def ordenar(matriz):
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i] < matriz[j]:
                matriz[i], matriz[j] = matriz[j], matriz[i]
                
def sumar_columna(matriz, columna):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]
    return suma
filas = ingreso_dato(2, "filas")
columnas = ingreso_dato(3, "columnas")

matriz = crear_matriz(filas, columnas)
print("Matriz original")
mostrar_matriz(matriz)

print("Filas sumadas")
filas_sumadas =sumar_filas(matriz)

mostrar_matriz(filas_sumadas)
print("Columna numerica agregada")
agregar_columna(filas_sumadas)
mostrar_matriz(filas_sumadas)

print("Matriz ordenada")
ordenar(filas_sumadas)
mostrar_matriz(filas_sumadas)

print("Sumatoria de primera columna: ", sumar_columna(filas_sumadas,0))