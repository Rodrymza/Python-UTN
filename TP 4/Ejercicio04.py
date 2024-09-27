"""Ejercicio 4: Verificar existencia de un elemento
a) Verifica si el color "morado" está presente en la tupla.
b) Verifica si el color "azul" está presente en la tupla.
c) Imprime el resultado de ambas verificaciones. """

colores = ("rojo", "verde", "azul", "amarillo")

morado_in_colores = "morado" in colores
azul_in_colores = "azul" in colores

if morado_in_colores:
    print("El color morado esta en la tupla")
else:
    print("El color morado no esta en la tupla")
    
if azul_in_colores:
    print("El color azul esta en la tupla")
else:
    print("El color azul no esta en la tupla")