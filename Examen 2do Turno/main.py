from factura import Factura
import funciones
from prettytable import PrettyTable

productos = [[101, "Leche", 250],
             [102, "Gaseosa", 300],
             [103, "Fideos", 150],
             [104, "Arroz", 280],
             [105, "Vino", 1200],
             [106, "Manteca", 200],
             [107, "Lavandina", 180],
             [108, "Detergente", 460],
             [109, "Jabon en polvo", 960],
             [110, "Galletas", 600]]

clientes = {"20110425417" : "Rodolfo Fernandez",
            "30527419655" : "Los Pollos Hermanos",
            "27289425478" : "Andrea Pereyra",
            "33536549878" : "Multimarca Repuestos",
            "20291122568" : "Luis Peric",}

def main():
    while True:
        nueva_factura = Factura()
        cuil = solicitar_cliente()
        nueva_factura.ingresar_cliente(asignar_cuil(cuil))
        while True:
            ingreso = input("Ingrese codigo de producto (0000 para salir)\n")
            if ingreso == "0000":
                break
            else:
                producto = producto_en_lista(ingreso)
                if producto:
                    nueva_factura.agregar_producto(producto)
        nueva_factura.asignar_letra(cuil)
        nueva_factura.asignar_montoIva(cuil)
        nueva_factura.asignar_total()
        nueva_factura.imprimir_factura(cuil)
        if funciones.pedir_boolean("Nueva factura?"):
            break


def producto_en_lista(busqueda):
    try: 
        busqueda = int(busqueda)
        for codigo, nombre, precio in productos:
            if codigo == busqueda:
                return [codigo, nombre, 1, precio, precio]
    except:
        print("El valor ingresado es incorrecto")
        return False
    print("El codigo de existe")
    return False    

def solicitar_cliente():
    while True:
        cuil = input("Ingrese numero de cliente\n")
        if clientes.get(cuil):
            return cuil
        elif cuil[0:2] in ("20", "27", "30", "33"):
            return cuil
        else:
            print("El cuil ingresado es incorrecto")

def asignar_cuil(cuil):
    if clientes.get(cuil):
        return clientes[cuil]
    else:
        return "Consumidor Final"

main()