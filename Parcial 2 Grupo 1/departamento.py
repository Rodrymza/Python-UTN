from ambiente import Ambiente
class Departamento:
    def __init__(self, letra: str):
        self.letra = letra
        self.lista_ambientes = []
        
    def mostrar_departamento(self):
        print(f"Departamento {self.letra}")
        print("Ambientes".center(40,"-"))
        ambiente: Ambiente
        for ambiente in self.lista_ambientes:
            ambiente.mostrar_ambiente()
        print(f"Total metros cuadrados Departamento {self.total_metros_departamento()} metros")
        print("".center(40, "-"))    
            
    def agregar_ambiente(self, ambiente: Ambiente):
        self.lista_ambientes.append(ambiente)
        print(f"{ambiente.tipo_ambiente} agregado a Departamento {self.letra}")
        
    def tiene_banio(self):
        ambiente: Ambiente
        for ambiente in self.lista_ambientes:
            if ambiente.tipo_ambiente.startswith("BAÑO"):
                return True
        return False

    def tiene_minimo_ambientes(self, minimo = 3):
        return len(self.lista_ambientes) >= minimo
    
    def total_metros_departamento(self):
        total = 0
        ambiente: Ambiente
        for ambiente in self.lista_ambientes:
            total += ambiente.metros_cuadrados
        return total
    
    def total_costo_departamento(self):
        total = 0
        ambiente: Ambiente
        for ambiente in self.lista_ambientes:
            total += ambiente.costo_ambiente
        return total
    
    def ordenar_ambientes(self):
        self.lista_ambientes.sort(key=lambda ambiente: ambiente.tipo_ambiente)