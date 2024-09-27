unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
    "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veinte",
    "veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
decenas = [ "" ,"" ,"" , "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
                  "ochenta", "noventa"]
       
centenas= ["" ,"ciento", "doscientos", "trescientos", "cuatrocientos",  
           "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]


anio="1200"

milenio = int(anio[0])
centena = int(anio[1])
decada = int(anio[2:])

if milenio==1:
    print("Mil", end=" ")
else:
    print(f"{unidades[milenio]} mil", end=" ")

print(f"{centenas[centena]}", end=" ")

if decada<30:
    print(f"{unidades[decada]}")
else:
    print(f"{decenas[decada//10]} {unidades[decada%10]}")    
