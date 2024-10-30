#Clase: marca(cadena), modelo (cadena), lista de objetos componenteCPU [

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
class Computadora:
    def __init__(self):
        self.marca = input("Ingrese marca de computadora\n")
        self.modelo = input("Ingrese modelo\n")
        self.lista_componentes = []
    
    def agregar_compoente(self, componente_actual):
            self.lista_componentes.append(componente_actual)
            
    def imprimir_computadora(self):
            print(f"-------Computadora-------\nMarca: {self.marca}\nModelo: {self.modelo}")
            print("Componentes:")
            print("Componente\t Marca\t Cantidad\t Precio U\t Subtotal\t Total")
            for elemento in self.lista_componentes:
                print(f"{elemento.componente}\t {elemento.marca}\t {elemento.cantidad} \t {elemento.precio}\t {elemento.cantidad*elemento.precio}")
            self.calcular_precio()
            
    def calcular_precio(self):
        precio_costo = 0
        for elemento in self.lista_componentes:
            precio_costo += elemento.precio * elemento.cantidad
        print(f"\t\t\t\t\t\t\t Costo total: ${precio_costo}")
        costo = precio_costo*0.3 if precio_costo <5000 else precio_costo*0.4
        print(f"El precio sugerido de venta es {precio_costo} + {costo} = ${precio_costo + costo}")
        
def main():
    lista_computadoras = []
    while True:
        computadora_actual = Computadora()
        while True:
            componente_actual = ComponenteCPU()
            componente_actual.agregar_cantidades()
            computadora_actual.agregar_compoente(componente_actual)
            if pedir_boolean("Desea agregar otro componente? (s/n)\n"):
                break
        lista_computadoras.append(computadora_actual)
        computadora_actual.imprimir_computadora()
        if pedir_boolean("Desea agregar otra PC? (s/n)\n"):
            break
            
def pedir_boolean(mensaje, valores = ["s", "n"]):   #valores invertidos 0 1 para funcionalidad de pregunta
        while True:
            ingreso = input(mensaje).lower()
            if ingreso in valores:
                return valores.index(ingreso)
                print(valores.index(ingreso))
            else:
                print("Respuesta incorrecta")
        
        
if __name__ == "__main__":
    main()