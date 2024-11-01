from prettytable import PrettyTable
class Expendedora:
    def __init__(self):
        self.empleados = {}
        self.golosinas = []
        self.pedidos = []
        self.claves_tecnico = ("admin", "CCCDDD", "2020")
        
    def agregar_empleados(self, diccionario):
        """agregar diccionario de empleados"""
        self.empleados = diccionario
        
    def agregar_golosinas(self, lista_golosina: list):
        """lista con 3 elementos (codigo, nombre, stock)"""
        self.golosinas.append(lista_golosina)
            
    def mostrar_golosinas(self):
        """muestra en un tabla la lista de golosinas y stock disponible"""
        tabla = PrettyTable()
        tabla.field_names = ("Codigo", "Descripcion", "Stock")
        for codigo, nombre, stock in self.golosinas:
            tabla.add_row([codigo, nombre, stock])
        print(tabla)
    
    def mostrar_empleados(self):
        """muestra en una tabla la lista de empleados y su legajo"""
        tabla = PrettyTable()
        tabla.field_names = ("Legajo", "Empleado")
        for legajo, nombre in self.empleados.items():
            tabla.add_row([legajo, nombre])
        print(tabla)
        
    def solicitar_legajo(self):
        """solicita legajo de empleado y busca si esta dentro del diccionario"""
        while True:
            ingreso = input("Ingrese el legajo del empleado\n")
            try:
                legajo = int(ingreso)
                if self.empleados.get(legajo):
                    print(f"Bienvenido {self.empleados[legajo]}")
                    return self.empleados[legajo]
                else:
                    print("El legajo ingresado no corresponde a un empleado")
                    return False
            except:
                print("El valor ingresado es incorrecto")
                
    def elegir_golosina(self):
        """selecciona la golosina con el valor del codigo"""
        self.mostrar_golosinas()
        while True:
            ingreso = input("Ingrese codigo de golosina\n")  
            try:
                ingreso = int(ingreso) -1
                if ingreso >= 0 and ingreso < len(self.golosinas):
                    return ingreso
                else:
                    print("El numero no pertenece a una golosina")
            except:
                print("El valor ingresado es incorrecto")
                
    def imprimir_pedido(self, pedido):
        tabla = PrettyTable()
        tabla.field_names = ["Nombre", "Cantidad"]
        for nombre, cantidad in pedido:
            tabla.add_row([nombre, cantidad])
        print(tabla)
        
    def pedir_golosina(self):
        empleado = self.solicitar_legajo()
        if empleado:
            while True:
                codigo = self.elegir_golosina()
                if self.golosinas[codigo][2] > 0:
                    self.golosinas[codigo][2] -= 1
                    print(f"Extrajiste 1 unidad de {self.golosinas[codigo][1]}")
                    self.pedidos.append([self.golosinas[codigo][1], 1])
                else:
                    print(f"Lo sentimos, la golosina {self.golosinas[codigo][1]} no tiene stock")
                if not self.pedir_boolean("Desea agregar mas golosinas al pedido?"):
                    print(f"Empleado: {empleado}")
                    self.imprimir_pedido()
                    self.pedidos.clear()
                    return
                    
    def rellenar_maquina(self):
        num = 1
        for elemento in self.claves_tecnico:
            ingreso = input(f"Ingrese clave {num}\n")
            num += 1
            if ingreso != elemento:
                print("Clave incorreta, saliendo...")
                return
        print("Acceso correcto")
        self.mostrar_golosinas()
        while True:
            ingreso = input("Seleccione golosina a rellenar\n")
            try:
                ingreso = int(ingreso) - 1
                if ingreso >=0 and ingreso <= len(self.golosinas):
                    cantidad = int(input(f"Ingrese cantidad de {self.golosinas[ingreso][1]} a rellenar\n"))
                    self.golosinas[ingreso][2] += cantidad
                    self.mostrar_golosinas()
                    print(f"Cantidad actualizada {self.golosinas[ingreso][1]}: {self.golosinas[ingreso][2]}")
                    if self.pedir_boolean("Desea agregar mas golosinas?"):
                        return 
            except:
                print("Valor incorrecto")
                
    def pedir_boolean(self, mensaje):
        while True:
            ingreso = input(mensaje + "\n").lower()
            match ingreso:
                case "s": return True
                case "n": return False
                case _: print("Respuesta incorrecta")
    
    def imprimir_pedido(self):
        tabla = PrettyTable()
        tabla.field_names = ["Nombre", "Cantidad"]
        for nombre, cantidad in self.pedidos:
            tabla.add_row([nombre, cantidad])
        print(tabla)