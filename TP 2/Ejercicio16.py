"""Codifique un método que reciba como parámetro una cadena y determine si la 
misma contiene o no números"""

def contiene_numeros(string):
    numeros=list("0123456789")
    for letra in string:
        for numero in numeros:
            if letra==numero:
                return True
    return False

print(contiene_numeros("hola como va"))
print(contiene_numeros("hoy me compre 3 cafe con leches"))