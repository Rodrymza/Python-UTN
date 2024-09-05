"""- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y 
monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
centavos. Plantee el algoritmo planteando métodos para su resolución."""

dinero = float(input("Ingrese la cantidad de dinero: \n"))

billetes = [200, 100, 50, 20 ,10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]

for i in billetes:
    resultado=dinero//i
    if resultado>0:
        text="Billetes" if dinero>1 else "Monedas"
        print(f"{text} de {i}: {int(resultado)}")
    dinero%=i