#------------------------- ANTES ---------------------------------------#

"""import os
from libro import Libro

class BibliotecaVirtual:
    def __init__(self):
        self.libros = {}
        self.cargar_desde_archivo("biblioteca.txt")

    def cargar_desde_archivo(self, nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(", ")
                    titulo, autor, disponibilidad = datos[0], datos[1], datos[2]
                    libro = Libro(titulo, autor, disponibilidad == "Disponible")
                    self.libros[titulo] = libro

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            for libro in self.libros.values():
                disponibilidad = "Disponible" if libro.disponible else "No disponible"
                archivo.write(f"{libro.titulo}, {libro.autor}, {disponibilidad}\n")

    def mostrar_biblioteca(self):
        for titulo, libro in self.libros.items():
            print(f"\n{libro}")

    def pedir_libro(self, titulo, tipo_usuario):
        nombre = input("Ingresa tu nombre: ")
        if titulo in self.libros:
            libro = self.libros[titulo]
            if libro.disponible:
                if tipo_usuario == "1":
                    print(f"{nombre} ha pedido prestado '{titulo}'!")
                    libro.disponible = False
                elif tipo_usuario == "2":
                    print(f"{nombre} ha pedido prestado '{titulo}'!")
                    libro.disponible = False
                else:
                    print("Tipo de usuario no válido. Debes ser '1' (estudiante) o '2' (profesor).")
            else:
                print(f"'{titulo}' no está disponible en este momento.")
        else:
            print(f"'{titulo}' no se encuentra en la biblioteca.")

    def devolver_libro(self, titulo):
        nombre = input("Ingresa tu nombre: ")
        if titulo in self.libros:
            libro = self.libros[titulo]
            if not libro.disponible:
                print(f"{nombre} ha devuelto '{titulo}'. Gracias por regresarlo.")
                libro.disponible = True
            else:
                print(f"'{titulo}' ya está disponible en la biblioteca.")
        else:
            print(f"'{titulo}' no se encuentra en la biblioteca.")
"""

#------------------------------------  DESPUÉS -----------------------------------------------------------#


from libro import Libro
import os

class Biblioteca:
    def _init_(self):
        self.libros = {}

    def cargar_desde_archivo(self, nombre_archivo):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(", ")
                    titulo, autor, disponibilidad = datos[0], datos[1], datos[2]
                    libro = Libro(titulo, autor, disponibilidad == "Disponible")
                    self.libros[titulo] = libro

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            for libro in self.libros.values():
                disponibilidad = "Disponible" if libro.disponible else "No disponible"
                archivo.write(f"{libro.titulo}, {libro.autor}, {disponibilidad}\n")

    def agregar_libro(self, libro):
        self.libros[libro.titulo] = libro

    def obtener_libro(self, titulo):
        return self.libros.get(titulo)