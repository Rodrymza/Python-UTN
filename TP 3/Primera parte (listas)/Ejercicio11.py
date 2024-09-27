"""Escribe  un programa que  permita al usuario  ingresar una lista y un número, y cuente 
cuántas veces aparece ese número en la lista."""

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

elemento_contar = int(input("Ingrese el numero a contar en la lista"))
contador = 0
for numero in lista_numeros:
    if numero == elemento_contar:
        contador += 1
        
print(f"El numero {elemento_contar} aparece {contador} veces en la lista")