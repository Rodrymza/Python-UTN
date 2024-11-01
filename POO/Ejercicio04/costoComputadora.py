from computadora import Computadora
from componenteCPU import ComponenteCPU

class CostoComputadora:
    def __init__(self):
        self.lista_computadoras = []
        
    def iniciar_gestion(self):
        while True:
            computadora_actual = Computadora()
            while True:
                componente_actual = ComponenteCPU()
                componente_actual.agregar_cantidades()
                computadora_actual.agregar_compoente(componente_actual)
                if not self.pedir_boolean("Desea agregar otro componente?"):
                    break
            self.lista_computadoras.append(computadora_actual)
            if not self.pedir_boolean("Desea agregar otra PC?"):
                break
            
    def pedir_boolean(self, mensaje):   #valores invertidos 0 1 para funcionalidad de pregunta
        while True:
            ingreso = input(mensaje + "(s/n)\n").lower()
            match ingreso:
                case "s": return True
                case "n": return False
                case _: print("Respuesta incorrecta")
                
    def imprimir_computadoras(self):
        for computadora in self.lista_computadoras:
            computadora.imprimir_computadora()
    
gestion = CostoComputadora()
gestion.iniciar_gestion()
gestion.imprimir_computadoras()