"""Codifique un programa que solicite un número entero mayor a cero y que 
mediante recursión sume todos los números números naturales desde el número 
ingresado hasta 1. """

def sumar_recursivo(numero):
    if numero==1:
        return 1
    else:
        return numero + sumar_recursivo(numero-1)
   
print(sumar_recursivo(5)) 
    