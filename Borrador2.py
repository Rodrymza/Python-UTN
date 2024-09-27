nombre = "Rodrigo   Ramirez  "
nuevo_nombre=""
for i in range(len(nombre)-1):
    if nombre[i]==" " and nombre[i+1]==" ":
        i+=1
    else:
        nuevo_nombre+=nombre[i]

print(nuevo_nombre)