"""Escribe  un  programa  que  identifique  y  muestre  los  elementos  que  se  repiten  en  una 
lista."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
lista_repetidos = []
for numero in lista_numeros:
    if lista_numeros.count(numero)>1:
        lista_repetidos.append(numero)
        
auxiliar = set(lista_repetidos)

for numero in auxiliar:
    print(f"El numero {numero} se repite")