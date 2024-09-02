"""Pedir dos cadenas por teclado e indicar si la segunda cadena se encuentra dentro de la primera"""

word1=input("Ingrese una palabra\n")
word2=input("Ingrese otra palabra\n")

print(word1.count(word2))

if word1.count(word2):
    print(f"La palabra {word2} se encuentra dentro de {word1}")
else:
    print(f"La palabra {word2} no se encuentra dentro de {word1}")
