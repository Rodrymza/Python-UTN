import random
numero = random.randint(0,101)
intento = -1
tries = 0

print("Adivina un número aleatorio de el 1 al 100.")

while intento != numero:
    print("Ingrese un número:")
    intento = int(input())
    tries += 1
    if intento<numero:
        print("El número es mayor, te quedaste corto.")
    else: 
        print("El número es menor, te pasaste.")
        
print("Excelente, el número era ", intento, ". Necesitaste ", tries, " intentos.")

