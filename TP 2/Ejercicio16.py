"""Codifique un método que reciba como parámetro una cadena y determine si la 
misma contiene o no números"""

def contiene_numeros(string):
    numeros="0123456789"
    condicion = False
    for letra in string:
        if letra in numeros:
                condicion = True
                break
    if condicion:
        print(f"La cadena '{string}' contiene numeros")
    else:
        print(f"La cadena '{string}' no contiene numeros")

contiene_numeros("hola como va")
contiene_numeros("hoy me compre 3 cafe con leches")