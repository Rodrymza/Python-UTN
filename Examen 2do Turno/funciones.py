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

def solicitar_cliente(diccionario):
    while True:
        cuil = input("Ingrese numero de cliente\n")
        if diccionario.get(cuil):
            return diccionario[cuil]
        elif cuil[0:2] in ("20", "27", "30", "33"):
            return "Consumidor Final"
        else:
            print("El cuil ingresado es incorrecto")

def solicitar_codigo_producto(lista_productos):
    while True:
        codigo = input("Ingrese el codigo del producto\n")
        if codigo == "0000":
            return codigo
        else:
            try:
                codigo = int(codigo)
                if codigo in lista_productos:
                    return codigo
                else:
                    print("El codigo no corresponde a un producto de la lista")
            except:
                print("El valor ingresado es incorrecto")

def pedir_boolean(mensaje):
    valores = ["s", "n"]
    while True:
        respuesta = input(mensaje + " (s/n)\n").lower()
        if respuesta in valores:
            return valores.index(respuesta)
        else:
            print("Respuesta incorrecta")
    