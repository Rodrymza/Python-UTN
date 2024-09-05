"""Crea un programa que lea una cadena de texto carácter por carácter usando
recursión."""

def mostrar_caracter(cadena):
    if len(cadena)<=1:
        return cadena
    else:
        return cadena[0] + "\n" + mostrar_caracter(cadena[1:])   
    
    pass

cadena="Rodrigo"
print(mostrar_caracter(cadena))