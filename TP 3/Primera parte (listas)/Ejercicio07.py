"""Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
promedio de los elementos."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
suma = 0
for numero in lista_numeros:
    suma += numero
    
promedio = float(round(suma/len(lista_numeros)))

print("El promedio de los valores de la lista es", promedio)