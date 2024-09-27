"""Escribe un programa que permita al usuario ingresar una lista y la invierta."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
lista_invertida = []
for numero in lista_numeros:
    lista_invertida.insert(0,numero)
    
print(f"Lista original: {lista_numeros}")
print(f"Lista invertida {lista_invertida}")