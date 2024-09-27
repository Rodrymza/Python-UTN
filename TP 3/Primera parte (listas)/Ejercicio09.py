"""Escribe  un programa que  permita al usuario  ingresar una lista de  números y  filtre  los 
números primos."""

def es_primo(numero):
    divisores=0
    dividendo=1
    while dividendo<=numero and divisores<3:
        if numero%dividendo==0:
            divisores+=1
        dividendo+=1
    
    if divisores<=2 and numero>1:
        return True
    else:
        return False
    
lista_numeros = [int(input("Ingrese un numero \n")) for i in range(int(input("Ingrese el total de numeros \n")))]
lista_primos = []
for numero in lista_numeros:
    if es_primo(numero):
        lista_primos.append(numero)
        
print(f"Lista numeros primos {lista_primos}")
print(f"Lista original {lista_numeros}")