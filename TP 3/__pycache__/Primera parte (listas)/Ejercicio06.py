"""Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
elementos duplicados. 
Pista: 
- Utiliza la función set()."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

lista_nueva = list(set(lista_numeros))

print(lista_nueva)