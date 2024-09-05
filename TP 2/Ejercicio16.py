"""Codifique un método que reciba como parámetro una cadena y determine si la 
misma contiene o no números"""

def contiene_numeros(string):
    numeros=list("0123456789")
    for letra in string:
        if letra in numeros:
                return True
    return False

print(contiene_numeros("hola como va"))
print(contiene_numeros("hoy me compre 3 cafe con leches"))