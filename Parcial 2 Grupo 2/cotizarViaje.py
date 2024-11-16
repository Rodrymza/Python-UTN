
from actividad import Actividad
from ciudad import Ciudad
from diaViaje import DiaViaje
from paqueteViaje import PaqueteViaje
def main():
    maximo_costo = 10000000
    paquete_viaje = PaqueteViaje(input("Ingrese nombre del paquete: "))
    dias_paquete = cargar_dias()
    for i in range(dias_paquete):
        print(f"Dia {i+1}")
        nuevo_dia = DiaViaje(i+1)
        while True:
            nueva_ciudad: Ciudad = crear_ciudad(paquete_viaje, maximo_costo)
            nuevo_dia.agregar_ciudad(nueva_ciudad)
            respuesta = input("Desea agregar mas ciudades?\n")
            if respuesta == "n":    
                paquete_viaje.agregar_dia(nuevo_dia)
                break
            
    paquete_viaje.mostrar_paquete()


def seleccionar_actividad():
    costo_viaje = {
    "100": ["DESAYUNO", 3000, 4000],
"200": ["ALMUERZO", 8000, 9000],
"300": ["MEDIATARDE", 4000, 5000],
"400": ["CENA", 7000, 8000],
"500": ["HOTEL 3 ESTRELLAS", 25000, 27000],
"600": ["HOTEL 4 ESTRELLAS", 30000, 32000],
"700": ["HOTEL 5 ESTRELLAS", 35000, 38000],
"800": ["VISITA MUSEO", 3500, 4500],
"900": ["CITY TOUR", 5500, 7500]}
    
    for codigo, (nombre, estandar, exclusive) in costo_viaje.items():
        print(f"{codigo} - {nombre} Estandar ${estandar} / Exclusive ${exclusive}")
    while True:
        opcion = input("Ingrese codigo de activiad seleccionada: ")
        if costo_viaje.get(opcion):
            print(f"Actividad seleccionada: {costo_viaje[opcion][0]}")
            while True:
                tipo = input("Ingrese \n1 Estandar \n2 Exclusive\n")
                if tipo == "1":
                    return Actividad(costo_viaje[opcion][0],"Tipo S", costo_viaje[opcion][1])
                elif tipo == "2":
                    return Actividad(costo_viaje[opcion][0], "Tipo E", costo_viaje[opcion][2])
                else:
                    print("Opcion invalida")
        else:
            print("Codigo invalido")

def crear_ciudad(paquete: PaqueteViaje, monto_maximo: int):
    while True:
        nombre = input("Ingrese el nombre de la ciudad: ")
        pais = input("Ingrese el nombre del pais: ")
        nueva_ciudad = Ciudad(nombre, pais)
        nueva_actividad = seleccionar_actividad()
        if paquete.calcular_costo_viaje() + nueva_ciudad.calcular_costo_total() + nueva_actividad.costo_actividad <= monto_maximo:
            paquete.agregar_ciudad(nueva_ciudad)
            print(f"Actividad {nueva_actividad.tipo_actividad} agregada correctamente")
        else:
            print(f"El monto maximo de ${monto_maximo} ha sido superado")
        respuesta = input("Desea agregar mas actividades?\n")
        if respuesta == "n":
            if nueva_ciudad.minimo_actividades():
                return nueva_ciudad
            else:
                print("Debes agregar al menos 3 actividades")
                input()

def cargar_dias(minimo = 1, maximo = 30):
    while True:
        dias = int(input("Ingrese la cantidad de dias: "))
        if minimo <= dias <= maximo:
            return dias
        else:
            print("La cantidad de dias debe estar entre {} y {}".format(minimo, maximo))

main()