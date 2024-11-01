from ingrediente import Ingrediente
class Plato:
    def __init__(self):
        self.nombre_completo = input("Ingrese nombre del plato a agregar\n")
        self.precio = self.pedir_decimal("Ingrese precio del plato\n")
        self.esBebida = self.pedir_boolean("El plato es una bebida? (y/n)\n")
        self.lista_ingredientes = []
        
    def pedir_decimal(self, mensaje):
        while True:
            ingreso = input(mensaje)
            try:
                precio = float(ingreso)
                return precio
            except:
                print("El valor ingresado no es valido\n")
     
    def pedir_boolean(self, mensaje, valores = ["y", "n"]):
        while True:
            esbebida = input(mensaje).lower()
            if esbebida in (valores):
                return True if esbebida=="y" else False
            else:
                print("No ingresaste una respuesta valida\n")
    
    def agregar_ingredientes(self):
        while True:
            ingrediente_actual = Ingrediente()
            self.lista_ingredientes.append(ingrediente_actual)
            if not self.pedir_boolean("Desea agregar mas ingredientes (y/n)?\n"):
                break
            
    def __str__(self):
        return f"Plato: {self.nombre_completo}\nPrecio ${self.precio}"
    
    def imprimir_ingredientes(self):
        if len(self.lista_ingredientes) > 0:
            print("Lista de ingredientes:")
            for elemento in self.lista_ingredientes:
                print(f"{elemento.cantidad} {elemento.unidad_medida} de {elemento.nombre}" )