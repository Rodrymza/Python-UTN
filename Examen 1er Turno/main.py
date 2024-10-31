from prettytable import PrettyTable
golosinas = [[1, "KitKat", 20],
             [2, "Chicles", 50],
             [3, "Caramelos de menta", 50],
             [4, "Huevos Kinder", 10],
             [5, "Chetoos", 10],
             [6, "Twix", 10],
             [7, "M&M's", 10],
             [8, "Papas Lays", 2],
             [9, "Milkybar", 10],
             [10, "Alfajor Tofi", 15],
             [11, "Lata Coca", 20],
             [12, "Chitos", 10],
             [13, "Ferne con coca", 0]]
empleados = {1100 : "Jose Alonso",
             1200 : "Federico Pacheco", 
             1300 : "Nelson Pereira", 
             1400 : "Osvaldo Tejada",
             1500 : "Gaston Guevara"}

claves_tecnico = ("admin", "CCCDDD", "2020")

golosinas_pedidas = []

def solicitar_legajo():
    while True:
        ingreso = input("Ingrese el legajo del empleado\n")
        try:
            legajo = int(ingreso)
            if empleados.get(legajo):
                print(f"Bienvenido {empleados[legajo]}")
                return empleados[legajo]
            else:
                print("El legajo ingresado no corresponde a un empleado")
                return False
        except:
            print("El valor ingresado es incorrecto")

def imprimir_golosinas():
    tabla = PrettyTable()
    tabla.field_names = ("Codigo", "Descripcion", "Stock")
    for codigo, nombre, stock in golosinas:
        tabla.add_row([codigo, nombre, stock])
    print(tabla)
    
def elegir_golosina():
    imprimir_golosinas()
    while True:
        ingreso = input("Ingrese codigo de golosina\n")  
        try:
            ingreso = int(ingreso) -1
            if ingreso >= 0 and ingreso < len(golosinas):
                print(f"Golosina seleccionada {golosinas[ingreso][1]}")
                return ingreso
            else:
                print("El numero no pertenece a una golosina")
        except:
            print("El valor ingresado es incorrecto")

def agregar_pedido(pedido):
    encontrado = False
    for i in range(len(golosinas_pedidas)):
            if pedido[0] == golosinas_pedidas[i][0]:
                golosinas_pedidas[i][1] += 1
                encontrado = True
    if not encontrado:
        golosinas_pedidas.append(pedido)

def pedir_boolean(mensaje):
    while True:
        ingreso = input(mensaje).lower()
        match ingreso:
            case "s": return False
            case "n": return True
            case _: print("Respuesta incorrecta")

def imprimir_pedido():
    tabla = PrettyTable()
    tabla.field_names = ["Nombre", "Cantidad"]
    for nombre, cantidad in golosinas_pedidas:
        tabla.add_row([nombre, cantidad])
    print(tabla)

def pedir_golosina():
    empleado = solicitar_legajo()
    if empleado:
        while True:
            codigo = elegir_golosina()
            if golosinas[codigo][2] > 0:
                golosinas[codigo][2] -= 1
                print(f"Extrajiste 1 unidad de {golosinas[codigo][1]}")
                agregar_pedido([golosinas[codigo][1], 1])
            else:
                print(f"Lo sentimos, la golosina {golosinas[codigo][1]} no tiene stock")
            if pedir_boolean("Desea agregar mas golosinas? (s/n)"):
                golosinas_pedidas.clear()
                break
        print(f"Pedido {empleado}:")
        imprimir_pedido()

def rellenar_maquina():
    num = 1
    for elemento in claves_tecnico:
        ingreso = input(f"Ingrese clave {num}\n")
        num += 1
        if ingreso != elemento:
            print("Clave incorreta, saliendo...")
            return
    print("Acceso correcto")
    imprimir_golosinas()
    while True:
        ingreso = input("Seleccione golosina a rellenar\n")
        try:
            ingreso = int(ingreso) - 1
            if ingreso >=0 and ingreso <= len(golosinas):
                cantidad = int(input(f"Ingrese cantidad de {golosinas[ingreso][1]} a rellenar\n"))
                golosinas[ingreso][2] += cantidad
                print(f"Cantidad actualizada {golosinas[ingreso][1]}: {golosinas[ingreso][2]}")
                return
        except:
            print("Valor incorrecto")

def main():
    while True:
        print("Seleccione opcion\n1 Pedir golosina\n2 Rellenar maquina\n3 Salir")
        ingreso = input()
        match ingreso:
            case "1": pedir_golosina()
            case "2": rellenar_maquina()
            case "3": break
            case _: print("Opcion incorrecta")
            
main()