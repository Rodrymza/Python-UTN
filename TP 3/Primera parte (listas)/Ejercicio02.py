"""Escribe  un programa que  pida al usuario una lista de números y encuentre  el mayor y 
el menor de ellos."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

maximo = lista_numeros[0]
minimo = lista_numeros[0]
for numero in lista_numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print(f"El numero mayor de la lista es {maximo} y el menor es {minimo}")