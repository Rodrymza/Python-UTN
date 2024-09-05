"""Cree una clase FuncionesPrograma y codifique una función estática getFechaString
que reciba como parámetro una fecha y retorne la fecha como una cadena literal. 
Ejemplo recibo 15/10/1900, la salida debe ser
Quince de Octubre de mil novecientos."""

"""Falta completar"""
class FuncionesPrograma:
    def __init__(self, fecha_completa: str= "fecha formato dd/mm/yyyy") -> None:
        self.fecha_completa = fecha_completa
        formateo=fecha_completa.split("/")
        self.anio= int(formateo[2])
        self.mes = int(formateo[1])
        self.dia = int(formateo[0])
    
    def fecha_literal(self):
       unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
    "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veinte",
    "veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
       
       meses=["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio"
              "Julio" , "Agosto", "Septiembre", "Octubre", "Noviembre"
              "Diciembre"]
       decenas = [ "" ,"" ,"" , "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
                  "ochenta", "noventa"]
       
       centenas= ["" ,"ciento", "doscientos", "trescientos", "cuatrocientos",  
                  "quinientos", "seiscientos", "setecientos", "ochocientos"
                  , "novecientos"]
       #dia a texto
       if self.dia<30:
            dia_texto=unidades[self.dia].capitalize()
       elif self.dia==30:
           dia_texto=decenas[self.dia//10].capitalize()
       else:
           dia_texto=f"{decenas[self.dia//10]} y {unidades[self.dia%10]}".capitalize()
       #mes a texto
       mes_texto=meses[self.mes-1]
       #anio a texto
       if self.anio//1000==1:
           anio_texto="mil"
       else:
           anio_texto=f"{unidades[self.anio//1000]} mil"

       resto=self.anio%1000
       if resto==100:
            anio_texto+=" cien"
       else:
            anio_texto+=f" {centenas[resto//100]}"
       resto%=100
       print("resto en decenas", resto)
       if resto<30:
            anio_texto+=f" {unidades[resto]}"
       elif resto==30:
           anio_texto+=f" {unidades[resto//10]}"
       else:
           anio_texto+=f" {decenas[resto//10]} y {unidades[resto%10]}"
       print(f"{dia_texto} de {mes_texto} de {anio_texto}")    
           
fecha=FuncionesPrograma("30/05/1991")
fecha.fecha_literal()

fechauno=FuncionesPrograma("15/05/1985")
fechauno.fecha_literal()