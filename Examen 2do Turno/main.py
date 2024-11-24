from factura import Factura
def main():
    nueva_factura = crear_factura()
    cuil = pedir_cuil()

    asignar_cliente(cuil, nueva_factura)

    agregar_productos(nueva_factura)
    nueva_factura.asignar_iva_letra(cuil)
    nueva_factura.asignar_total()

    nueva_factura.mostrar_factura()




def crear_factura():
    fecha = input("Ingrese fecha de la factura: ")
    numero = int(input("Ingrese numero de factura: "))
    nueva_factura = Factura(fecha, numero)
    return nueva_factura

def pedir_cuil():
    while True:
        cuil = input("Ingrese el CUIL del cliente: ")
        if cuil[0:2] in ("20", "27", "30", "33"):
            return cuil
        else:
            print("CUIL invalido")

def asignar_cliente(cuil, factura: Factura):
    clientes = {
    "20110425417": "Rodolfo Fernandez",
    "30527419655": "Los Pollos Hnos",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}
    if clientes.get(cuil):
        print(clientes[cuil])
        factura.set_clienteFactura(clientes[cuil])
    else:
     factura.set_clienteFactura("Consumidor Final")
    
def agregar_productos(factura: Factura):
    productos = {
    "101": ["Leche", 250],
    "102": ["Gaseosa", 300],
    "103": ["Fideos", 150],
    "104": ["Arroz", 280],
    "105": ["Vino", 1200],
    "106": ["Manteca", 200],
    "107": ["Lavandina", 180],
    "108": ["Detergente", 460],
    "109": ["Jabón en Polvo", 960],
    "110": ["Galletas", 600]
}
    while True:
        for clave, (nombre, precio) in productos.items():
            print(f"{clave} - {nombre} - ${precio}")
        print("Ingrese 0000 para salir")
        codigo = input("Ingrese el codigo del producto: ")
        if codigo == "0000":
            break
        if productos.get(codigo):
            nombre = productos[codigo][0]
            precio = productos[codigo][1]
            cantidad = pedir_entero(f"Ingrese cantidad de {nombre}: ")

            factura.agregar_producto([codigo, nombre, cantidad, precio])
        else:
            print("Codigo invalido")

def pedir_entero(mensaje: str):
    while True:
        entero = input(mensaje)
        try:
            numero = int(entero)
            return numero
        except:
            print("Error, ingrese un numero entero")

if __name__ == "__main__":
    main()