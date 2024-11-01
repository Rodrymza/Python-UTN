from plato import Plato
class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []
        
    def iniciar_gestor(self):
        while True:
            plato_actual = Plato()
            if not plato_actual.esBebida:
                plato_actual.agregar_ingredientes()
            self.platos_menu.append(plato_actual)
            
            if not plato_actual.pedir_boolean("Desea agrear mas platos? (y/n)\n"):
                break
            
        print("--------MENU--------")
        for plato in self.platos_menu:
            print(plato)
            plato.imprimir_ingredientes()

menu = MenuRestaurant()
menu.iniciar_gestor()