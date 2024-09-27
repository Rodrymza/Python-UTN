"""Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
suma de todos los elementos en la lista."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

suma = 0
print(f"La lista de numeros es: {lista_numeros}")

for numero in lista_numeros:
    suma += numero
    
print(f"La suma de los numeros de la lista es {suma}")