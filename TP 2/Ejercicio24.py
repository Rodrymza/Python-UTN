"""Crea un programa que lea una cadena de texto carácter por carácter usando
recursión."""

def mostrar_caracter(cadena):
    if len(cadena)==1:
        print(cadena)
    else:
        print(cadena[0])
        mostrar_caracter(cadena[1:])   
    
cadena="Rodrigo"
mostrar_caracter(cadena)