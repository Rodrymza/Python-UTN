#Sistema de gestion de inventario de Tienda

def mostrar_inventario(inventario):
    for clave in inventario.keys():
        print(f"Codigo: {clave}, Descripcion : {inventario[clave][1]}, Precio ${inventario[clave][2]}")
            
def buscar_producto(inventario, codigo):
    encontrado = False
    if codigo in inventario:
            print(f"Producto encontrado: '{inventario[codigo][0]}' Precio ${inventario[codigo][2]}")
    else:
        print("No se encontro el producto")
        
def modificar_precio(inventario, codigo, nuevo_precio):
    if codigo in inventario:
        auxiliar = inventario.pop(codigo)
        inventario[codigo] = auxiliar[0], auxiliar[1], nuevo_precio
        print(f"El precio del producto '{inventario[codigo][0]}' ha sido actualizado a ${inventario[codigo][2]}")
    else:
        print("Codigo incorrecto")

def eliminar_producto(inventario,codigo):
    if codigo in inventario:
        inventario.pop(codigo)
        print(f"El producto con codigo '{codigo}' ha sido eliminado")
    else:
        print("Codigo incorrecto")

def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    encontrados = False
    diccionario_auxiliar = {}
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}")
    for clave in inventario.keys():
        
        if inventario[clave][2]>= min_precio and inventario[clave][2]<= max_precio:
            diccionario_auxiliar[clave] = inventario[clave]
            encontrados = True
    
    if encontrados:
        mostrar_inventario(diccionario_auxiliar)
    else:
        print("No se encontraron productos en el rango de precios")    
    
inventario = {"A001" : ("Mouse Inhalambrico", "Marca Trust, con pilas", 12000),
              "A002" : ("Teclado Genius BT", "Teclado marca genius, inalambrico, luces RGB", 2500),
              "A003" : ("Pendrive 128 GB", "Pendrive 128 GB de almacenamiento marca Datatraveler", 50000),
              "A004" : ("Monitor Samsung 20'", "Monitor Samsung 20 pulgadas, HDMI", 70000),
              "A005" : ("Impresora Brother DCP 1200", "Chorro de tinta, 3 cartuchos, WiFi", 90000)}
mostrar_inventario(inventario)
buscar_producto(inventario, "A003")
modificar_precio(inventario, "A001", 15000)
eliminar_producto(inventario,"A001")
productos_por_rango_de_precio(inventario, 2000, 50000)