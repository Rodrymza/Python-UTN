class OperacionMatematica:
    def __init__(self, num1, num2, operacion):
        self.num1 = num1
        self.num2 = num2
        self.operacion= operacion
        
    def sumarNumeros(self):
        print(f"Suma: {self.num1} + {self.num2} = {self.num1+self.num2}")
    
    def restarNumeros(self):
        print(f"Resta: {self.num1} - {self.num2} = {self.num1-self.num2}")
    
    def multiplicarNumeros(self):
        print(f"Multiplicacion: {self.num1} x {self.num2} = {self.num1*self.num2}")
    
    def dividirNumeros(self):
        print(f"Division: {self.num1} / {self.num2} = {round(self.num1/self.num2,2)}")
    
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