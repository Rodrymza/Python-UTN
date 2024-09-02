class Persona:
    def __init__(info,nombre, edad):
        info.nombre = nombre
        info.edad = edad
        
    def saludar(info):
        print(f"Hola! {info.nombre}, tienes {info.edad} años")
    def sumaredad(info):
        print(f"Dentro de 10 años tendras {info.edad+10} años")
        
persona1=Persona(input("Ingresa tu nombre:"),int(input("Ingresa tu edad")))

persona1.saludar()
persona1.sumaredad()