"""Solicitar el ingreso de un numero decimal y asignarle el nombre valordecimal, convertirlo a short, int, long y float"""

valorDecimal=input("Ingrese un numero con decimales\n")

#convertir a float
valorDecimal=float(valorDecimal)
print(f"La variable {valorDecimal} ahora es de tipo: {type(valorDecimal)}" )

#convertir a int
valorDecimal=int(valorDecimal)
print(f"La variable {valorDecimal} ahora es de tipo {type(valorDecimal)}")

#convertir a bool
valorDecimal=bool(valorDecimal)
print(f"La variable {valorDecimal} ahora es de tipo {type(valorDecimal)}")
