"""Cree  una  clase  OperacionMatematica  con  dos  atributos  valor1  y  valor2  y  un 
atributo de nombre operación.  Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente: 
sumarNumeros() 
restarNumeros()
multiplicarNumeros() 
dividirNumeros()
El quinto método será el siguiente:  aplicarOperacion(operacion)"""

class OperacionMatematica:
    def __init__(self, valor1, valor2, operacion):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion= operacion
        
    def sumarNumeros(self):
        print(f"Suma: {self.valor1} + {self.valor2} = {self.valor1+self.valor2}")
    
    def restarNumeros(self):
        print(f"Resta: {self.valor1} - {self.valor2} = {self.valor1-self.valor2}")
    
    def multiplicarNumeros(self):
        print(f"Multiplicacion: {self.valor1} x {self.valor2} = {self.valor1*self.valor2}")
    
    def dividirNumeros(self):
        print(f"Division: {self.valor1} / {self.valor2} = {round(self.valor1/self.valor2,2)}")
    
    def aplicarOperacion(self):
        match self.operacion:
            case "+":
                self.sumarNumeros()
            case "-":
                self.restarNumeros()
            case "*":
                self.multiplicarNumeros()
            case "/":
                self.dividirNumeros()
            case _:
                print("Operacion invalida")        
                
operacion1=OperacionMatematica(23,43,"*")
operacion1.aplicarOperacion()

operacion2 = OperacionMatematica(23,12,"+")
operacion2.aplicarOperacion()       