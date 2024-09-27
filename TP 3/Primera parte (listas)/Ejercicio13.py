""" Explique  y  ejemplifique  la  librería  NumPy  para  trabajar  con  matrices  y 
arrays"""

import numpy as np
matriz_numpy = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])
lista_numpy = np.array([1,2,3,4,5])
"""Numpy es un libreria que es de mucha utlilidad para trabajar con matrices multidimensioinales y hacer operaciones matematicas
con grandes cantidadades de datos
ventajas:
- los arrays son mas rapidos y ocupan menos espacio
- permite realizar operaciones matematicas avanzadas sobre arrays
- manejo de datos estructurados, para realizar arrays de diferentes tipos de datos
- broadcasting, facilita operaciones entre arrays de distintos tamaños y formas"""

#Ejemplo: creacion de matriz con valors aleatorios con numpy:
matriz_aleatoria = np.random.randint(0,100, size=(3,3))

print(matriz_aleatoria)