class Libros:
    prestado = False
    def __init__(self, nombre, autor, anio):
       self.nombre = nombre
       self.autor = autor
       self.anio = anio 
        
class Usuario:
    def __init__(self, nombre, id) -> None:
        self.nombre = nombre
        self.id = id
        prestamos = []
   
class Biblioteca:
    def __init__(self) -> None:
        self.usuarios = {}
        self.libros = []
        
    def registrar_usuario(self, usuario):
        existe = self.usuarios.get(usuario.id)
        if existe:
            print("Usuario ya registrado")
        else:
            self.usuarios[usuario.id] = usuario.nombre
            
    def mostrar_usuarios(self):
        for clave, valor in self.usuarios.items():
            print(clave, valor)
    
libros = [Libros("Cien años de soledad", "Garcia Marquez Gabriel", 1998)]
libros.append(Libros("El amor en los tiempos del colera", "Garcia Marquez Gabriel", 1990))

mi_biblioteca = Biblioteca()
rodry = Usuario("Rodrigo", 36499229)
rocy = Usuario("Rocio", 38473146)
mi_biblioteca.registrar_usuario(rodry)
mi_biblioteca.registrar_usuario(rocy)

mi_biblioteca.mostrar_usuarios()