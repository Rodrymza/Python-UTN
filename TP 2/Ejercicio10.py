"""Convertir cadena a mayusculas o minusculas. Dar al usuario la opcion de que desea hacer"""

cadena=input("Ingrese una cadena de texto\n")
opc=0

while opc!=1 and opc!=2:
    print("Ingrese la opcion deseada")
    print("1 Mayusculas a Minusculas")
    print("2 Minisculas a Mayusculas")
    opc=int(input())
    
    if opc==1:
        print(f"Cadena convertida a Minusculas: {cadena.lower()}")
    elif opc==2:
        print(f"Cadena convertida a Mayusculas: {cadena.upper()}")
    else:
        print("Opcion Invalida!")
