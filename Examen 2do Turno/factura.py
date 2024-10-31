from prettytable import PrettyTable
import funciones

class Factura:
    def __init__(self) -> None:
        self.fecha = input("Ingrese fecha de la factura (dd/mm/aaa)\n")
        self.numeroFactura = funciones.pedirentero("Ingrese numero de la factura")
        self.letra = ""
        self.total = 0.0
        self.montoiva = 0
        self.clienteFactura = ""
        self.detalleFactura = []

    def ingresar_cliente(self, cliente):
        self.clienteFactura = cliente            

    def agregar_producto(self, producto):
        encontrado = False
        for i in range(len(self.detalleFactura)):    
            if self.detalleFactura[i] [0] == producto[0]:
                self.detalleFactura[i] [2] += 1
                self.detalleFactura[i] [4] = self.detalleFactura[i] [2] * self.detalleFactura[i] [3]
                print(f"Producto {producto[1]} sumado")
                encontrado = True
                break
        if not encontrado:
            print(f"Producto {producto[1]} agregado")
            self.detalleFactura.append(producto)
        
    def calcularTotal(self):
        total = 0
        for elemento in self.detalleFactura:
            total += elemento[4]
        return total
    
    def asignar_montoIva(self, cuil):
        if cuil[0:2] in ["20", "27"]:
            self.montoiva = 0
        else:
            self.montoiva = 21
    
    def asignar_letra(self, cuil):
        if cuil[0:2] in ["20", "27"] or self.clienteFactura == "Consumidor Final":
            self.letra = "B"
        else:
            self.letra = "A"
    
    def asignar_total(self):
        self.total = self.calcularTotal()
        if self.montoiva == 21:
            self.total += float(self.calcularTotal() * self.montoiva / 100)
            
    def imprimir_factura(self, cuil):
        tabla = PrettyTable()
        print(f"Cliente {self.clienteFactura} Cuil: {cuil}")
        print(f"Letra {self.letra}")
        print(f"Iva: {self.montoiva}")
        print("Lista productos")
        tabla.field_names = ["Codigo", "Nombre", "Cantidad", "Precio", "Subtotal"]
        for codigo, nombre, cantidad, precio, subtotal in self.detalleFactura:
            tabla.add_row([codigo, nombre, cantidad, precio, subtotal])
        print(tabla)
        print(f"Total sin impuestos ${self.calcularTotal()}")
        print(f"Total: ${self.total}")