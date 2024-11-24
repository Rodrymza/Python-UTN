from atleta import Atleta
class Carrera:
    def __init__(self, pais: str, nombre: str, kmCarrera: float):
        self.nombre = nombre.title()
        self.pais = pais.title()
        self.kmCarreera = kmCarrera
        self.promedio: float
        self.ganador: Atleta
        self.competidores = [] 
        self.podioCarrera = []
        
    def mostrar_carrera(self):
        print(f"Nombre de la carrera: {self.nombre}")
        print(f"Pais: {self.pais}")
        print(f"km Carrera: {self.kmCarreera}")
        print(f"Ganador Carrera: {self.ganador.nombre}")
        self.mostrar_podio()
    
    def determinar_podio(self):
        podio = sorted(self.competidores, key= lambda atleta: atleta.tiempoRealizado)
        podio3 = podio[0:3]
        return podio3
                    
    def mostrar_podio(self):
        atleta: Atleta
        print("Podio Atletas".center(30, "-"))
        medallas = ["ORO", "PLATA", "BRONCE"]
        for medalla, atleta in zip(medallas,self.podioCarrera):
            print(f"{medalla}:  {atleta.nombre} Tiempo: {atleta.tiempoRealizado}")
        print("".center(30, "-"))
        
        
    def mostrar_atletas(self):
        atleta: Atleta
        print("Lista de competidores".center(30, "-"))
        for atleta in self.competidores:
            print(atleta)
            
    def agregar_atleta(self, atleta_nuevo: Atleta):
        self.competidores.append(atleta_nuevo)
        print(f"Atleta {atleta_nuevo.nombre} agregado")
        
    def calcular_promedio_tiempos(self):
        lista_tiempos = [atleta.tiempoRealizado for atleta in self.competidores]
        total_tiempo = sum(lista_tiempos)
        return round(total_tiempo / len(self.competidores))
    
    def asignar_valores(self):
        self.podioCarrera = self.determinar_podio()
        self.ganador = self.podioCarrera[0]
        self.promedio = self.calcular_promedio_tiempos()
    
        
    