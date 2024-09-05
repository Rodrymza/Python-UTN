"""Suma los dígitos de un número ingresado por el usuario de forma recursiva. """

def sumar_digitos(num):
    if num<10:
        return num
    else:
        return num%10 + sumar_digitos(num//10) 
        

print(sumar_digitos(123))