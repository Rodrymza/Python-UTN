"""Escribe  un  programa  que  permita  al usuario  ingresar una  lista  de  números  y  eliminar 
un elemento en un índice especificado. """

lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]

indice_borrar = int(input("Ingrese el indice del elemento a borrar"))

print(lista_numeros)
if indice_borrar<len(lista_numeros):
    lista_numeros.remove(lista_numeros[indice_borrar])
    print("Lista con elemento borrado:", lista_numeros)
else:
    print("Indice fuera de rango")