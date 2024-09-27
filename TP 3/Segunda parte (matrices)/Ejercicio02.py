import Ejercicio01
matriz = Ejercicio01.crear_matriz(3,3)

for filas in matriz:
    suma=sum(filas)
    print(filas)
    
print(f"La suma de todos los valores dentro de la matriz da: {suma}")
