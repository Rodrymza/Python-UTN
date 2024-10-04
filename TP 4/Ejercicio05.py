"""Ejercicio 5: Contar elementos en una tupla 
Dada la siguiente tupla: 
numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
a) Cuenta cuántas veces aparece el número 4 en la tupla. b) Imprime el resultado."""

numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
numero_a_contar = 4
        
print(f"El numero {numero_a_contar} aparece {numeros.count(numero_a_contar)} veces en la tupla")
