"""Ejercicio 6: Crear y acceder a un diccionario 
Crea un diccionario que contenga información sobre una persona, incluyendo las 
claves: nombre, edad, y ciudad. Luego:
a) Imprime el valor asociado a la clave nombre.
b) Imprime el valor asociado a la clave edad. """

persona = {"nombre" : "Rodrigo",
           "apellido" : "Ramirez",
           "edad" : 33}

print(f"El nombre de la persona es: {persona['apellido']}, {persona["nombre"]}")
print(f"La edad de la persona es: {persona["edad"]}")