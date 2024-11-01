from expendedora import Expendedora
def main():
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

    expendedora_empresa = Expendedora()
    for lista in golosinas:
        expendedora_empresa.agregar_golosinas(lista)
    expendedora_empresa.agregar_empleados(empleados)

    while True:
        print("Seleccione opcion\n1 Pedir golosina\n2 Rellenar maquina\n3 Salir")
        ingreso = input()
        match ingreso:
            case "1": expendedora_empresa.pedir_golosina()
            case "2": expendedora_empresa.rellenar_maquina()
            case "3":
                print("Apagando sistema...") 
                break
            case _: print("Opcion incorrecta")
            
if __name__ == "__main__":
    main()