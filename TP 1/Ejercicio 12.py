dia=0
while dia<1 or dia>7:
    dia=int(input("Ingrese el dia de la semana: "))
if dia==1 or dia==2 or dia==3 or dia==4 or dia==5:
    print("Es un dia laborable")
else:
    print("Es fin de semana")