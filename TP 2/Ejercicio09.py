"""Recorre  la  cadena  del  ejercicio  6  y  transforma  cada  carácter  a  su  código  ASCII. 
Muéstralos en línea recta, separados por un espacio entre cada carácter."""

from Ejercicio06 import cadena
for letra in cadena:
    print(f"El valor ASCII de {letra} es: {ord(letra)}")