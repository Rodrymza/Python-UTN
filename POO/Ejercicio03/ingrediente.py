class Ingrediente:
    def __init__(self):
        self.nombre = input("Ingrese nombre del ingrediente\n")
        self.cantidad = self.pedir_entero("Ingrese cantidad de ingrediente\n")
        self.unidad_medida = input("Ingrese unidad de medida\n")
        
    def pedir_entero(self, mensaje):
        while True:
            ingreso = input(mensaje)
            try:
                precio = int(ingreso)
                return precio
            except:
                print("El valor ingresado no es valido\n")