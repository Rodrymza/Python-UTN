def pedir_boolean(mensaje, valores = ["s", "n"]):   #valores invertidos 0 1 para funcionalidad de pregunta
    while True:
        ingreso = input(mensaje).lower()
        if ingreso in valores:
            return valores.index(ingreso)
        else:
            print("Respuesta incorrecta")   

def ingresarNumero(mensaje, valor = 0):
    """valor predeterminado valida decimal, coloca 1 para validar entero"""
    while True:
        ingreso = input(mensaje)
        try:
            precio = float(ingreso) if valor == 0 else int(ingreso)
            return precio
        except:
            print("El valor ingresado no es valido\n")