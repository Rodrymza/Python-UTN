class Factura:
    def __init__(self, fecha: str, numero: int) -> None:
        self.fecha = fecha
        self.numero = numero
        self.letra: str
        self.montoIva: float
        self.clienteFactura: str
        self.detalleFactura = []
        self.totalFactura: float

    def agregar_producto(self, producto: list):
        self.detalleFactura.append(producto)
        print(f"Producto {producto[1]} agregado")

    def set_clienteFactura(self, cliente):
        self.clienteFactura = cliente

    def calcular_total(self):
        total = 0
        for _, _, cantidad, precio in self.detalleFactura:
            total += precio * cantidad
        return total
    
    def asignar_iva_letra(self, cuil: str):
        if cuil[0:2] in ("20", "27"):
            self.letra = "B"
            self.montoIva = 0
        else:
            self.letra = "A"
            self.montoIva = round(self.calcular_total() * 0.21, 2)

    def asignar_total(self):
        self.totalFactura = self.calcular_total() + self.montoIva

    def mostrar_factura(self):
        print(f"{"Fecha":<35}{self.fecha}")
        print(f"{"Numero":<35}{self.numero}")
        print(f"{"Letra":<35}{self.letra}")
        print(f"{"Cliente":<35}{self.clienteFactura}")
        print(f"{"Codigo":<12}{'Detalle':<20}{'Cantidad':<10}{'Precio Unitario':<15}{"Subtotal":<15}")
        for producto in self.detalleFactura:
            print(f"{producto[0]:<12}{producto[1]:<20}{producto[2]:<10}{producto[3]:<15}{(producto[2]*producto[3]):<15}")
        print(f"{"IVA":>50}{self.montoIva:>10}")
        print(f"{"Total":>50}{self.totalFactura:>10}")

