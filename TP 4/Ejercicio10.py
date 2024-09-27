"""Ejercicio 10: Diccionario anidado 
Dado el siguiente diccionario de alumnos: """ 

alumnos = {"alumno1": {"nombre": "Carlos", "edad": 20, "nota": 8.5},
           "alumno2": {"nombre": "Lucía", "edad": 22, "nota": 9.0},
           "alumno3": {"nombre": "Ana", "edad": 21, "nota": 7.5}, } 

"""a) Imprime el nombre del alumno2. 
b) Imprime la nota del alumno3"""

print(f"El nombre del Alumno 2 es: {alumnos["alumno2"]["nombre"]}")
print(f"La nota del Alumno 3 es: {alumnos["alumno3"]["nota"]}")