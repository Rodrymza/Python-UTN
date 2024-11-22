from edificio import Edificio
from ambiente import Ambiente
from departamento import Departamento
from piso import Piso

def main():
    edificio: Edificio = crear_edificio()
    cantidad_pisos = pedir_cantidad_pisos()
    for piso in range(cantidad_pisos):
        print("Creando piso", piso)
        nuevo_piso = Piso(piso)
        while True:
            print("Agregando departamento")
            nuevo_departamento = crear_departamento(nuevo_piso, edificio)
            nuevo_piso.agregar_departamento(nuevo_departamento)
            respuesta = input("Desea agregar mas departamentos?: ")
            if respuesta.lower() == "n":
                edificio.agregar_piso(nuevo_piso)
                break
    edificio.mostrar_edificio()

def crear_edificio():
    nombre = input("Ingrese el nombre del edificio: ")
    edificio = Edificio(nombre)
    return edificio

def pedir_cantidad_pisos(minimo = 1, maximo = 7):
    while True:
        try:
            cantidad_pisos = int(input(f"Ingrese la cantidad de pisos del edificio: "))
            if minimo <= cantidad_pisos <= maximo:
                return cantidad_pisos
            else:
                print("La cantidad de pisos debe estar entre", minimo, "y", maximo)
        except:
            print("La cantidad de pisos debe ser un número entero")
           
           
def crear_departamento(piso: Piso, edificio: Edificio, maximo_metros = 800):
    letra = input("Ingrese letra del departamento: ").upper()
    departamento = Departamento(letra)
    
    while True:
        nuevo_ambiente = seleccionar_ambiente()
        if edificio.calcular_total_metros() + piso.total_metros_piso() + departamento.total_metros_departamento() < maximo_metros:
            departamento.agregar_ambiente(nuevo_ambiente)
        else:
            print("No hay suficiente espacio para agregar más ambientes")
            
        respuesta = input("Desea agregar otro ambiente? (s/n): ")
        if respuesta.lower() == "n":
            if departamento.tiene_banio() and departamento.tiene_minimo_ambientes():
                departamento.ordenar_ambientes()
                return departamento
            else:
                if not departamento.tiene_banio():
                    print("Falta agregar un baño")
                if not departamento.tiene_minimo_ambientes():
                    print("Falta agregar al menos 3 ambientes")
    
    
def seleccionar_ambiente():
    ambientes = {
    "AAA": ["COCINA", 20, 21000],
    "BBB": ["HABITACION", 12, 10000],
    "CCC": ["BAÑO ESTÁNDAR", 6, 9000],
    "DDD": ["HABITACION PREMIUM", 16, 15000],
    "EEE": ["BAÑO PREMIUM", 8, 12000],
    "FFF": ["ESCRITORIO", 10, 8000],
    "GGG": ["COMEDOR", 30, 25000]
}
    for codigo, (nombre, metros, precio) in ambientes.items():
        print(f"{codigo}: {nombre} - {metros} m2 - ${precio}")
    while True:
        codigo = input("Selecciona un ambiente: ").upper()
        if ambientes.get(codigo):
            tipo = ambientes[codigo][0]
            metros = ambientes[codigo][1]
            precio = ambientes[codigo][2]
            return Ambiente(tipo, metros, precio)
        else:
            print("Código no encontrado")
            
        
if __name__ == "__main__":
    main()