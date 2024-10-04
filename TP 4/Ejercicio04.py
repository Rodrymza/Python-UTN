"""Ejercicio 4: Verificar existencia de un elemento
a) Verifica si el color "morado" está presente en la tupla.
b) Verifica si el color "azul" está presente en la tupla.
c) Imprime el resultado de ambas verificaciones. """

colores = ("rojo", "verde", "azul", "amarillo")

def ver_existencia(color,tupla):
    if color in tupla:
        print(f"El color {color} esta en la tupla")
    else:
        print(f"El color {color} no esta en la tupla")

ver_existencia("morado",colores)
ver_existencia("azul",colores)