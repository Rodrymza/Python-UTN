"""Ejercicio 9: Contar palabras en un texto 
Dado el siguiente texto: 
texto = "manzana naranja manzana pera pera pera naranja manzana" 
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
texto utilizando un diccionario. 
b) Imprime el diccionario resultante. """

texto = "manzana naranja manzana pera pera pera naranja manzana"
texto += " " 

lista_frutas = []
fruta = ""
for letra in texto:
    
    if letra != " ":
        fruta += letra
    else:
        lista_frutas.append(fruta)
        fruta = ""
        
frutas = {}
for palabra in lista_frutas:
    if palabra in frutas:
        frutas[palabra] += 1
    else:
        frutas[palabra] = 1

print(frutas)