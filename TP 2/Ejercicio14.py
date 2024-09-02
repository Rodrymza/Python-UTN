"""Valores por ferefencia y por valor"""

"""Las variables que son definidas en el bloque del programa principal pueden ser utilizadas en las diferentes funciones 
y utilizarlas normalmente"""

def sumar(num):
    return variable_global+num
variable_global=23

print("Valor original de la variable global:", variable_global)
print("Valor devuelto por la funcion:", sumar(3))
print("Variable global:", variable_global)

"""Sin embargo, estas variables no pueden ser cambiadas dentro del bloque de la funcion ya que dara un error UnboundLocalError"""

def sumar(num):
    variable_global=variable_global+num
    return variable_global

try:
    print(f"Modificar variable global:", sumar(2))
except:
    print("Error al intentar modificar la variable global")

"""Si podrian cambiarse a traves de una funcion, pero no directamente en el bloque de la funcion"""

def sumar(num):
    return variable_global+num

variable_global=sumar(3)
print("Se cambio el valor de la variable global a:", variable_global)
