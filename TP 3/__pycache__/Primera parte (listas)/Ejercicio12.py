"""Escribe  un  programa  que  sume  dos  listas  de  números  elemento  por  elemento.  Las 
listas deben tener la misma longitud."""

lista_numeros_1 = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
lista_numeros_2 = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

if len(lista_numeros_2) == len(lista_numeros_1):    
    for i in range(len(lista_numeros_1)):
        print(f"La suma de {lista_numeros_1[i]} + {lista_numeros_2[i]} es igual a {lista_numeros_1[i] + lista_numeros_2[i]}")
    else:
        print("Las listas deben contener el mismo numero de elementos")