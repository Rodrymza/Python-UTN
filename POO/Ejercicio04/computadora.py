from prettytable import PrettyTable #libreria para generar tabla al mostrar datos
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
            tabla = PrettyTable()
            tabla.field_names = ["Componente", "Marca", "Precio", "Cantidad", "Subtotal"]
            for elemento in self.lista_componentes:
                tabla.add_row([elemento.componente, elemento.marca, elemento.cantidad, elemento.precio, elemento.cantidad*elemento.precio])
            print(tabla)
            self.calcular_precio()
            
    def calcular_precio(self):
        precio_costo = 0
        for elemento in self.lista_componentes:
            precio_costo += elemento.precio * elemento.cantidad
        print(f"\t\t\t\t\t\t\t Costo total: ${precio_costo}")
        costo = precio_costo*0.3 if precio_costo <5000 else precio_costo*0.4
        print(f"El precio sugerido de venta es {precio_costo} + {costo} = ${precio_costo + costo}")