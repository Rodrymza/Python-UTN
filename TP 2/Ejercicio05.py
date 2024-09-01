"""Solicitar el ingreso de una cadena y eliminar los espacios, mostrar cadena resultante"""

cadena=input("Ingrese un texto cualquiera \n")
nuevacadena=""
for i in cadena:
    if i!=" ":
        nuevacadena+=i
print(f"La cadena sin espacios es : {nuevacadena}")
    