num=int(input("Ingresa un numero: "))
divisores=0
dividendo=1
while dividendo<=num and divisores<3:
    if num%dividendo==0:
        divisores+=1
    dividendo+=1
    
if divisores<=2 and num>1:
    print("Es un numero primo")
else:
    print("No es un numero primo")