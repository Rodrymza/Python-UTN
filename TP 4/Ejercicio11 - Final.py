#Sistema de gestion de inventario de Tienda

inventario = {"A001" : ("Mouse Inalambrico", "Mouse Marca Trust, con pilas", 12000),
              "A002" : ("Teclado Genius BT", "Teclado marca genius, inalambrico, luces RGB", 2500),
              "A003" : ("Pendrive 128 GB", "Pendrive 128 GB de almacenamiento marca Datatraveler", 50000),
              "A004" : ("Monitor Samsung 20'", "Monitor Samsung 20 pulgadas, HDMI", 70000),
              "A005" : ("Impresora Brother DCP 1200", "Chorro de tinta, 3 cartuchos, WiFi", 90000)}

def mostrar_inventario(inventario):
    for clave, (nombre, descripcion, precio)  in inventario.items():
        print(f"Codigo: {clave}, Descripcion : {descripcion}, Precio ${precio}")
            
def buscar_producto(inventario, codigo):
    producto = inventario.get(codigo)   #devuelve valor si encuentra la clave sino retorna un None
    if producto:
        print(f"Producto encontrado : {producto[0]} Precio $ {producto[2]}")
    else:
        print(f"Producto con codigo '{codigo}' no encontrado")
    return producto
                 
def modificar_precio(inventario, codigo, nuevo_precio):
    producto = buscar_producto(inventario, codigo)
    if producto:
        inventario.pop(codigo)
        tupla = (producto[0], producto[1], nuevo_precio)
        inventario[codigo] = tupla
        print(f"El precio del producto '{producto[0]}' ha sido actualizado a ${nuevo_precio}")
        
def eliminar_producto(inventario,codigo):
    producto = buscar_producto(inventario, codigo)
    if producto:
        inventario.pop(codigo)
        print(f"El producto con codigo '{codigo}' ha sido eliminado")

def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    encontrados = False
    diccionario_auxiliar = {}
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}")
    for clave, (nombre, descripcion, precio) in inventario.items():
        
        if precio >= min_precio and precio <= max_precio:
            diccionario_auxiliar[clave] = inventario.get(clave)
            encontrados = True
    
    if encontrados:
        mostrar_inventario(diccionario_auxiliar)
    else:
        print("No se encontraron productos en el rango de precios")    
    
#mostrar_inventario(inventario)
#buscar_producto(inventario, "A006")
#modificar_precio(inventario, "A001", 15000)
#modificar_precio(inventario, "A089", 12000)
#eliminar_producto(inventario,"A001")
#eliminar_producto(inventario,"A008")
#productos_por_rango_de_precio(inventario, 2000, 50000)