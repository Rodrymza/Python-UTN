#Programa que cuente las palabras de una cadena de texto y las guarde en un diccionario

texto = "manzana manzana pera manzana pera banana banana manzana pera huevos huevos palta palta naranja naranja"

frutas = list(texto.split())
cantidad_frutas = {}
print(frutas)

for fruta in frutas: 
    if cantidad_frutas.get(fruta):
        cantidad_frutas[fruta] += 1
    else :
        cantidad_frutas[fruta] = 1
        
print(cantidad_frutas)
