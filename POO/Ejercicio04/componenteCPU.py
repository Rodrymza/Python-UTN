class ComponenteCPU:
    def __init__(self):
        self.componente = input("Ingrese nombre de componente\n").title()
        self.marca = input("Ingrese marca\n").title()
        self.cantidad = 0
        self.precio = 0.0
        
    def agregar_cantidades(self):
        self.cantidad = self.pedir_entero("Ingrese cantidad\n")
        self.precio = self.pedir_decimal("Ingrese precio\n")
        
    def pedir_entero(self, mensaje):
        while True:
            ingreso = input(mensaje)
            try:
                precio = int(ingreso)
                return precio
            except:
                print("El valor ingresado no es valido\n")
    
    def pedir_decimal(self, mensaje):
        while True:
            ingreso = input(mensaje)
            try:
                precio = float(ingreso)
                return precio
            except:
                print("El valor ingresado no es valido\n")