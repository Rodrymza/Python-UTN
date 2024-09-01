"""¿Que ocurre si se asigna a una variable un valor fuera de rango?
Si se asigna a un variable un valor que no le corresponde dara un error de tipo ValueError"""

numero="dostres"
"""Si intentamos convertirlo con el casteo dara error numero=int(numero)
Sin embargo, podemos controlar este tipo de errores con el bloque try-exept donde podemos preveer que ocurrira 
en caso de que no se pueda completar la operacion"""

print(f"La variable numero contiene el valor: {numero} de tipo {type(numero)}")
try:
    numero=int(numero)
except:
    print("No se pudo realizar la conversion a int")
    print(f"El valor en la variable es: {numero} y es de tipo {type(numero)}")