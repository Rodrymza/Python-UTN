"""Codificar un algoritmo que solicite el ingreso de un numero de 3 cifras y
por medio del uso de operaciones matematicas modulo 10 efectue la suma de los numeros"""

numero=int(input("Ingrese un numero de 3 cifras \n"))
suma=0
while numero>0:
    resto=numero%10
    numero//=10
    suma+=resto
    
print(f"La suma de las 3 cifras da: {suma}")