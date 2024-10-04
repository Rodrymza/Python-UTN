"""Ejercicio 9: Contar palabras en un texto 
Dado el siguiente texto: 
texto = "manzana naranja manzana pera pera pera naranja manzana" 
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
texto utilizando un diccionario. 
b) Imprime el diccionario resultante. """

texto = "manzana naranja manzana pera pera pera naranja manzana"
lista_frutas = texto.split(" ")
print(lista_frutas)   
frutas = {}
for palabra in lista_frutas:
    if palabra in frutas:
        frutas[palabra] += 1
    else:
        frutas[palabra] = 1

print(frutas)