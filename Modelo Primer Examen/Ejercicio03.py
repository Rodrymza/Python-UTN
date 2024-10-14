correcto = False
while not correcto:
    numero = input("Ingresa un numero\n")
    try:
        numero = int(numero)
        correcto = True
    except:
        print("No ingresaste un valor numerico")
        