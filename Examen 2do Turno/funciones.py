def pedirentero(mensaje):
    while True:
        entero = input(mensaje + "\n")
        try:
            entero = int(entero)
            return entero
        except:
            print("El valor ingresado no es correcto")

def pedirdecimal(mensaje):
    while True:
        entero = input(mensaje + "\n")
        try:
            entero = float(entero)
            return entero
        except:
            print("El valor ingresado no es correcto")

def pedir_boolean(mensaje):
    while True:
        respuesta = input(mensaje + "(s/n)\n").lower()
        match respuesta:
            case "s": return True
            case "n": return False
            case _ : 
                print("Respuesta incorrecta")
    