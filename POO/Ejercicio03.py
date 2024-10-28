
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
    
class Plato:
    def __init__(self):
        self.nombre_completo = input("Ingrese nombre del plato a agregar\n")
        self.precio = self.pedir_decimal("Ingrese precio del plato\n")
        self.esBebida = Plato.pedir_boolean("El plato es una bebida? (y/n)\n")
        self.lista_ingredientes = []
        
    def pedir_decimal(self, mensaje):
        while True:
            ingreso = input(mensaje)
            try:
                precio = float(ingreso)
                return precio
            except:
                print("El valor ingresado no es valido\n")
    
    @staticmethod 
    def pedir_boolean(mensaje, valores = ["y", "n"]):
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
            if not Plato.pedir_boolean("Desea agregar mas ingredientes?\n"):
                break
            
    def __str__(self):
        return f"Plato: {self.nombre_completo}\nPrecio ${self.precio}"
    
    def imprimir_ingredientes(self):
        if len(self.lista_ingredientes) > 0:
            print("Lista de ingredientes:")
            for elemento in self.lista_ingredientes:
                print(f"{elemento.cantidad} {elemento.unidad_medida} de {elemento.nombre}" )
                
class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []
        
    def main(self):
        while True:
            plato_actual = Plato()
            if not plato_actual.esBebida:
                plato_actual.agregar_ingredientes()
            self.platos_menu.append(plato_actual)
            
            if not Plato.pedir_boolean("Desea agrear mas platos?\n"):
                break
            
        print("--------MENU--------")
        for plato in self.platos_menu:
            print(plato)
            plato.imprimir_ingredientes()

menu = MenuRestaurant()
menu.main()
    
    