from departamento import Departamento
class Piso:
    def __init__(self, nroPiso: int):
        self.nroPiso = nroPiso
        self.lista_departamentos = []
        
    def mostrar_piso(self):
        print(f"Piso {self.nroPiso}")
        print("Departamentos del piso".center(40, "-"))
        departamento: Departamento
        for departamento in self.lista_departamentos:
            departamento.mostrar_departamento()
            
    def agregar_departamento(self, departamento: Departamento):
        self.lista_departamentos.append(departamento)
        print(f"Departamento {departamento.letra} agregado a Piso {self.nroPiso}")
        
    def total_metros_piso(self):
        depto: Departamento
        total = 0
        for depto in self.lista_departamentos:
            total += depto.total_metros_departamento()
        return total
    
    def total_costo_piso(self):
        depto: Departamento
        total = 0
        for depto in self.lista_departamentos:
            total += depto.total_costo_departamento()
        return total