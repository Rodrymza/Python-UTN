"""- En la clase FuncionesPrograma codifique una método getFechaDate estática que 
reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo 
date correspondiente."""

class FuncionesPrograma:
    def __init__(self, fecha_completa: str= "fecha formato dd/mm/yyyy") -> None:
        self.fecha_completa = fecha_completa
        formateo=fecha_completa.split("/")
        self.anio= int(formateo[2])
        self.mes = int(formateo[1])
        self.dia = int(formateo[0])
        
    def getFechaDate(self):
        fecha = True
        if self.anio<0 or self.anio>2300:
            fecha = False
            print("Año incorrecto")
       
        match self.mes:
            case 1 | 3 | 5 | 7 | 10 | 12:
                if self.dia > 31 or self.dia < 1:
                    print("Dia incorrecto para este mes")
                    fecha = False
            case 4 | 6 | 9 | 11:
                if self.dia > 30 or self.dia < 1:
                    print("Dia incorrecto para este mes")
                    fecha = False
            case 2:
                if (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0):
                    if self.dia<1 or self.dia>29:
                        fecha = False
                        print("Dia incorrecto para este mes")
                else:
                     if self.dia<1 or self.dia>28:
                        fecha = False
                        print("Dia incorrecto para este mes")
            case _:
                fecha = False
        return fecha
    
    def fecha_literal(self):
        if self.getFechaDate():
            
            unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
            "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veinte",
            "veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
       
            meses=["Enero" ,"Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                  "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            decenas = [ "" ,"" ,"" , "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
                        "ochenta", "noventa"]
       
            centenas= ["" ,"ciento", "doscientos", "trescientos", "cuatrocientos",  
                      "quinientos", "seiscientos", "setecientos", "ochocientos" , "novecientos"]
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
                anio_texto="Mil "
            else:
                anio_texto=f"{unidades[self.anio//1000]} Mil ".capitalize()
        #centena
            resto=self.anio%1000
            if resto==100:
                anio_texto+=" cien "
            else:
             anio_texto+=f"{centenas[resto//100]} ".capitalize()
            resto%=100
      # print("resto en decenas", resto)
            if resto<30:
                 anio_texto+=f"{unidades[resto]}"
            elif resto==30:
                 anio_texto+=f"{unidades[resto//10]}"
            else:
                anio_texto+=f" {decenas[resto//10]} y {unidades[resto%10]}"
            string_fecha=f"{dia_texto} de {mes_texto} de {anio_texto}"
         
            print(string_fecha)  
        else:
            print("La fecha ingresada es incorrecta")
fecha=(FuncionesPrograma("30/09/2015"))
fecha.fecha_literal()

fecha = (FuncionesPrograma("30/2/1998"))
fecha.fecha_literal()