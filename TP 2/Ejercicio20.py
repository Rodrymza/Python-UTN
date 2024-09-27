"""Cree una clase Fracción con dos atributos, numerador y denominador. 
Agregue a la clase los siguientes 4 métodos e implemente los mismos:
sumarFracciones(Fraccion f1, Fraccion f2) 
restarFracciones(Fraccion f1, Fraccion f2) 
multiplicarFracciones(Fraccion f1, Fraccion f2) dividirFracciones(Fraccion f1, Fraccion f2) 
Todos los métodos deben retornar la fracción resultante de la operación.  
Cree una clase  OperacionesFraccion  que  contenga un método  main donde  se  solicite 
al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos 
Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos 
implementados  anteriormente  asignando  el  resultado  a  una  nueva  variable  de  tipo 
Fracción y mostrando por pantalla el resultado de las operaciones realizadas. """
import math
class Fraccion:
    def __init__(self,numerador, denominador) -> None:
        self.denominador = denominador
        self.numerador = numerador

        
    def __str__(self) -> str:
        if self.denominador == 1:
            return f"{self.numerador}"
        else:
             return f"{self.numerador} / {self.denominador}"
    
    @staticmethod
    def simplificar_numeros(numerador, denominador):
        mcd = math.gcd(numerador, denominador)
        numerador_simplificado = numerador // mcd
        denominador_simplificado = denominador // mcd
        return Fraccion(numerador_simplificado, denominador_simplificado)

    @staticmethod
    def sumar_fracciones(fraccion1, fraccion2):
        resultado_numerador = fraccion1.numerador * fraccion2.denominador + fraccion1.denominador * fraccion2.numerador
        resultado_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion.simplificar_numeros(resultado_numerador, resultado_denominador)
    
    @staticmethod
    def restar_fracciones(fraccion1, fraccion2):
        resultado_numerador = fraccion1.numerador * fraccion2.denominador - fraccion1.denominador * fraccion2.numerador
        resultado_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion.simplificar_numeros(resultado_numerador, resultado_denominador)
        
    @staticmethod
    def multiplicar_fracciones(fraccion1, fraccion2):
        resultado_numerador = fraccion1.numerador *  fraccion2.numerador
        resultado_denominador = fraccion1.denominador * fraccion2.denominador
        return Fraccion.simplificar_numeros(resultado_numerador, resultado_denominador)
    
    @staticmethod
    def dividir_fracciones(fraccion1, fraccion2):
        resultado_numerador = fraccion1.numerador * fraccion2.denominador
        resultado_denominador = fraccion1.denominador * fraccion2.numerador
        return Fraccion.simplificar_numeros(resultado_numerador, resultado_denominador)
        
class OperacionesFraccion:
    
    @staticmethod
    def main():
        numeros = []
        nombres = ["numerador de la fraccion 1", "denominador de la fraccion 1", "numerador de la fraccion 2", "denominador de la fraccion 2"]
        for i in range(4):
            print(f"Ingrese el {nombres[i]}")
            numeros.append(int(input()))
        fraccion_1 = Fraccion(numeros[0], numeros[1])
        fraccion_2 = Fraccion(numeros[2], numeros[3])
        
        print(f"Fracciones: {fraccion_1} ; {fraccion_2}")

        if fraccion_1.denominador < 1 or fraccion_2.denominador < 1:
            print("Ingresaste mal un denominador")
        else:
            print(f"Suma: {Fraccion.sumar_fracciones(fraccion_1, fraccion_2)}")
            print(f"Resta: {Fraccion.restar_fracciones(fraccion_1, fraccion_2)}")
            print(f"Multiplicacion: {Fraccion.multiplicar_fracciones(fraccion_1, fraccion_2)}")
            print(f"Division: {Fraccion.dividir_fracciones(fraccion_1, fraccion_2)}")
            
OperacionesFraccion.main()