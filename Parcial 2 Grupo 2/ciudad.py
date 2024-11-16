from actividad import Actividad
class Ciudad:
        def __init__(self, nombreCiudad, nombrePais) -> None:
            self.nombreCiudad = nombreCiudad
            self.nombrePais = nombrePais
            self.lista_actividades = []

        def actividad_repetida(self, actividad_nueva: Actividad):
            actividad: Actividad
            for actividad in self.lista_actividades:
                 if actividad.tipo_actividad[0:5] == actividad_nueva.tipo_actividad[0:5]:
                      return True
            return False
        
        def mostrar_cuidad(self):
             print(f"Ciudad: {self.nombreCiudad} Pais: {self.nombrePais}")
             actividad: Actividad
             for actividad in self.lista_actividades:
                  actividad.mostrar_actividad()
             print("".center(20,"-"))
  

        def calcular_costo_total(self):
             actividad: Actividad
             costo = 0
             for actividad in self.lista_actividades:
                  costo += actividad.costo_actividad
             return costo
        
        def minimo_actividades(self, minimo = 3):
             return len(self.lista_actividades) >= minimo
        
        def agregar_actividad(self, actividad_nueva: Actividad):
                if self.actividad_repetida(actividad_nueva):
                    print("No se puede agregar la actividad, ya que es repetida")
                else:
                     self.lista_actividades.append(actividad_nueva)
                     print(f"Actividad {actividad_nueva.tipo_actividad} agregada")