"""Valores por ferefencia y por valor"""

"""En Python los parametros pueden pasarse por valor o por referencia pero esto depende del tipo de dato
Los tipos de dato mutables (listas, diccionarios, sets) se pasan por referencia, es decir que si cambian su valor dentro de la funcion
tambien lo haran el el bloque principal"""


def sumar_valor(lista_parametro):
    for i in range(len(lista_parametro)):
        lista[i]+=1

lista=[1, 2, 3, 4]
print(lista)
sumar_valor(lista)
print("Valores cambiados")
print(lista)

"""Los datos inmutables (numeros, cadenas de texto, tuplas), se pasan por valor, es decir
que no cambian su valor en el bloque principal aunque cambien dentro de la funcion"""

def multiplicarpor2(num):
    num*=2

numero=2
print(numero)
print("Llamado a la funcion")
multiplicarpor2(numero)
print(numero)

"""Para que especificar que se va a trabajar con la variable global hay que declararlo con la palabra clave -global- dentro
de la funcion, cabe aclarar que entonces no habra que pasarla mediante parametros"""

def modificar_global():
    global numero
    numero*=2

modificar_global()

print("Variable modificada", numero)