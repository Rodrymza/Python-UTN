"""Convertir cadena a mayusculas o minusculas. Dar al usuario la opcion de que desea hacer"""

cadena=input("Ingrese una cadena de texto\n")
opc=""

while opc!="1" and opc!="2":
    print("Ingrese la opcion deseada")
    print("1 Mayusculas a Minusculas")
    opc = input("2 Minisculas a Mayusculas\n")
    
    match opc:
        case "1" : print(f"Cadena convertida a Minusculas: {cadena.lower()}")
        case "2": print(f"Cadena convertida a Mayusculas: {cadena.upper()}")
        case _: print("Opcion Invalida!")
