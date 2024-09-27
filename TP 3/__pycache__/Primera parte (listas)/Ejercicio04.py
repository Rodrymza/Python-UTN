"""Escribe  un  programa  que  pida  al  usuario  una  lista  de  números  y  cuente  cuántos  de 
ellos son pares y cuántos son impares."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
pares = 0
impares = 0
for numero in lista_numeros:
    if numero%2 == 0:
        pares += 1
    else:
        impares += 1