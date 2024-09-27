"""Reemplaza todas las 'a' de una cadena por la letra 'e' """

cadena=input("Ingresa un texto cualquiera: ")
nuevacadena = ""

#print(cadena.replace("a","e")) --->funcion para reemplazar

for letra in cadena:
    if letra== "a":
        nuevacadena += "e"
    else:
        nuevacadena += letra
        
print(nuevacadena)