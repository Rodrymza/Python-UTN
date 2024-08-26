
numero = int(input("Ingrese un numero entero: "))
variable_3=0
variable_9=0
    
if numero%2==0:
    print("El número cumple el criterio de divisibilidad 2.")
 
for i in str(numero):
    variable_3+=int(i) 
if variable_3%3==0:
    print("El número cumple el criterio de divisibilidad 3.")
    
if int(str(numero)[-1])==5 or int(str(numero)[-1])==0:
    print("El número cumple el criterio de divisibilidad 5.")
    
for i in str(numero):
    variable_9+=int(i) 
if variable_9%9==0:
    print("El número cumple el criterio de divisibilidad 9.")
    
if int(str(numero)[-1])==0:
    print("El número cumple el criterio de divisibilidad 10.")
    