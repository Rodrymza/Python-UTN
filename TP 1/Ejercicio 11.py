contraseña = "password"
contador = 1
intento=""

while contador < 4 and intento != contraseña:
    intento = input("Ingrese la contraseña: ")
    contador += 1
    
if intento == contraseña:
    print("Acceso correcto.")
else:
    print("El acceso se ha bloqueado después de los 3 intentos.")