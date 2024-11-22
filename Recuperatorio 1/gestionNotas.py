from prettytable import PrettyTable
def main():
    lista_alumnos = {60902: "Rodolfo Fernandez",
            61654:"Luis Gomez",
            }

    notas_finales = []
    for nombre in lista_alumnos.values():
        cargar_notas(notas_finales, nombre)
        
    mostrar_notas_finales(notas_finales)
    promedio_mayor_final(notas_finales)

    
def cargar_notas(notas_finales: list, alumno: str):
    materias = [["Ciencias"],
                ["Historia"],
                ["Geografia"],
                ["Matematicas"],
                ["Fisica"]]
    nota_maxima = [0, ""]
    print(f"Estudiante {alumno}")
    for fila_materia in materias:
        nota1 = validar_entero(f"Ingrese Nota 1 de {fila_materia[0]}: ")
        fila_materia.append(nota1)
        nota_maxima = verificar_maximo(nota_maxima[0], nota1, nota_maxima[1], fila_materia[0] )
        nota2 = validar_entero(f"Ingrese Nota 2 de {fila_materia[0]}: ")
        nota_maxima = verificar_maximo(nota_maxima[0], nota2, nota_maxima[1], fila_materia[0])
        fila_materia.append(nota2)
        nota3 = round(float((nota1+nota2)/2),2)
        fila_materia.append(nota3)
        
    print(f"Alumno: {alumno}")
    mostrar_notas(materias)
    print(f"La nota maxima del alumno fue: {nota_maxima[0]} en la asignatura {nota_maxima[1]}")
    cargar_notas_finales(notas_finales ,materias, alumno)
                
def mostrar_notas(lista: list):
    tabla = PrettyTable()
    tabla.field_names = ["Materia", "Nota 1", "Nota 2", "Promedio"]
    for nombre, nota1, nota2, promedio in lista:
        tabla.add_row([nombre, nota1, nota2, promedio])
    print(tabla)       
        
def validar_entero(mensaje: str, minimo = 0 ,maximo =10):
    while True:
        ingreso = input(mensaje)
        try:
            entero = int(ingreso)
            if  minimo <= entero <= maximo:
                return entero
            else:
                print(f"El numero debe estar entre {minimo} y {maximo}")
        except:
            print("Valor invalido")
    
def verificar_maximo(acutal:int, nueva: int, materia_actual: str, materia_nueva: str):
    if nueva > acutal:
        return [nueva, materia_nueva]
    else:
        return [acutal, materia_actual]
    
def cargar_notas_finales(notas_finales: list, materias: list, alumno:str):
    suma = 0
    for _, _, _ , promedio in materias:
        suma += promedio
    promedio_notas = float(round(suma/len(materias),2))
    notas_finales.append([alumno, promedio_notas])

def mostrar_notas_finales(nota_final: list):
    tabla = PrettyTable()
    tabla.field_names = ["Nombre", "Promedio Global"]
    for nombre, nota in nota_final:
        tabla.add_row([nombre, nota])
    print(tabla)
            
def promedio_mayor_final(notas_finales: list):
    mayor = 0
    promedio_mayor = []
    for nombre, nota in notas_finales:
        if nota > mayor:
            mayor = nota
            promedio_mayor = [nombre, nota]
    print(f"El Alumno con mejor promedio es {promedio_mayor[0]} con promedio {promedio_mayor[1]}")
        
if __name__ == "__main__":
    main()