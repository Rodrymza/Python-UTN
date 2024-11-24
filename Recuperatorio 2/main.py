from carrera import Carrera
from atleta import Atleta
def main():
    
    carrera = seleccionar_maraton()
    while True:
        agregar_atleta_carrera(carrera)
        respuesta = input("Agregar mas atletas?")
        if respuesta == "n":
            break
    carrera.asignar_valores()
    carrera.mostrar_carrera()
    carrera.mostrar_atletas()



def seleccionar_maraton():
    maratones = {"AAA" : ["Maraton de Boston", "EEUU", 55],
                     "BBB" : ["Maraton de Roma", "Italia", 52],
                     "CCC" : ["Maraton de Paris", "Francia", 51],
                     "AAA" : ["Maraton de Buenos Aires", "Argentina", 53]}

    for clave, (nombre, pais, km) in maratones.items():
        print(f"{clave} - Maraton: {pais}, {km} km")

    while True:
        seleccion = input("Seleccione una maraton de la lista: ").upper()
        if maratones.get(seleccion):
            print(f"Carrera seleccionada: {nombre}, {pais}")
            return Carrera(pais, nombre, km)
        else:
            print("Codigo invalido")
            
def agregar_atleta_carrera(carrera: Carrera):
    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = pedir_decimal("Ingrese el tiempo del atleta: ")
    nuevo_atleta = Atleta(nombre, tiempo)
    carrera.agregar_atleta(nuevo_atleta)
    
def pedir_decimal(mensaje):
    while True:
        decimal = input(mensaje)
        try:
            return float(decimal)
        except:
            print("El valor ingresado no es correcto")
            
if __name__ == "__main__":
    main()