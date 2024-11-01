from gestorfacturas import GestorFacturas
from funciones import pedir_boolean
def main():
    gestor = GestorFacturas()
    while True:
        gestor.iniciar_facturacion()
        if not pedir_boolean("Desea realizar una nueva facturacion?"):
            break
        
if __name__ == "__main__":
    main()