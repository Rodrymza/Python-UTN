"""Solicitar el ingreso de una cadena y determinar el tamaño y la cantidad de vocales de la misma"""

cadena=input("Ingrese un texto cualquiera: ")
vocales="aeiou"
cantidad=0

for letra in cadena:
    cantidad +=1 if letra in vocales else 0   
           
print(f"El tamaño de la cadena es {len(cadena)}")
print(f"La cantidad de vocales es {cantidad}")