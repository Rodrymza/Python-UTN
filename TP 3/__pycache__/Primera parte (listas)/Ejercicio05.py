"""Escribe  un programa  que  multiplique  cada  elemento  de  una  lista  de  números  por  un 
valor ingresado por el usuario."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

multiplicador = int(input("Ingrese un valor para multiplicar los elementos de la lista"))

lista_nueva = []

for numero in lista_numeros:
    lista_nueva.append(numero * multiplicador)
    
print(f"Lista original: {lista_numeros}")
print(f"Lista modificada: {lista_nueva}")