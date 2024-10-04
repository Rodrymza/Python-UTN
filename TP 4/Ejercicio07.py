"""Ejercicio 7: Modificar un diccionario 
Dado el siguiente diccionario: 
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
    } 
a) Cambia el valor de la clave edad a 31.
b) Agrega una nueva clave profesión con el valor "Ingeniero".
c) Imprime el diccionario modificado."""

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} 

persona["edad"] = 31

persona["profesion"] = "Ingeniero"

for clave, valor in persona.items():
    print(f"{clave.upper()}: {valor}")