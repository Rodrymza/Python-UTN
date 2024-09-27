"""Una  tupla  es  una  colección  ordenada  e  inmutable  de  elementos.  Esto  significa  que, 
una vez que se crea una tupla, no se puede modificar. Se definen usando paréntesis ()"""

#puede usarse el metodo tuple al igual que el metodo list para crear nuevas tuplas
nombre = "Rodrigo"
tuple_name = tuple(nombre)  #La función tuple() toma un iterable (como una lista) y lo convierte en una tupla
print(tuple_name)

#pueden realizarse las mismas operaciones que con listas: desempaquetar, concatenar y verificar existencia:

tupla_ejemplo = (1, 2, 3, 4)

a, b , c, d= tupla_ejemplo

print(a)
print(b)

tupla_2 = (5, 6, 7)

nuevatupla = tupla_ejemplo + tupla_2
print(nuevatupla)

print(8 in nuevatupla)