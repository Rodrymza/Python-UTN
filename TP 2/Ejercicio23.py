"""Crea un programa donde se pida el ingreso de una cadena y por medio de 
recursión mostrar la cadena de forma inversa."""

def mostrar_inverso(cadena):
    if len(cadena)<=1:
        return cadena
    else:
        return cadena[-1] + mostrar_inverso(cadena[0:-1])
        
cadena="Rodrigo"
print(mostrar_inverso(cadena))