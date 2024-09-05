class OperacionMatematica:
    def __init__(self, num1, num2, operacion):
        self.num1 = num1
        self.num2 = num2
        self.operacion= operacion
        
    def sumarNumeros(self):
        print("La suma da", self.num1+self.num2)
    
    def restarNumeros(self):
        print("La resta da", self.num1-self.num2)
    
    def multiplicarNumeros(self):
        print("La multiplicacion da", (self.num1*self.num2))
    
    def dividirNumeros(self):
        print("La division da", self.num1/self.num2)
    
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