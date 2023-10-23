#------------------------- ANTES ---------------------------------------#


"""from bibliotecaVirtual import *

def main():
    biblioteca = BibliotecaVirtual()

    while True:
        print("\n--- Biblioteca Virtual Universidad Distrital ---")
        print("1. Mostrar biblioteca")
        print("2. Pedir prestado un libro")
        print("3. Devolver un libro")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            biblioteca.mostrar_biblioteca()
        elif opcion == "2":
            titulo = input("Ingresa el título del libro que deseas pedir prestado: ")
            tipo_usuario = input("Eres '1' (estudiante) o '2' (profesor): ")
            biblioteca.pedir_libro(titulo, tipo_usuario)
        elif opcion == "3":
            titulo = input("Ingresa el título del libro que deseas devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "4":
            biblioteca.guardar_en_archivo("biblioteca.txt")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()"""

#------------------------------------  DESPUÉS -----------------------------------------------------------#

from biblioteca import Biblioteca
from libro import Libro

class BibliotecaVirtual:
    def _init_(self):
        self.biblioteca = Biblioteca()
        self.biblioteca.cargar_desde_archivo("biblioteca.txt")

    def mostrar_biblioteca(self):
        for libro in self.biblioteca.libros.items():
            print(f"\n{libro}")

    def pedir_libro(self, titulo, tipo_usuario):
        nombre = input("Ingresa tu nombre: ")
        libro = self.biblioteca.obtener_libro(titulo)
        if libro:
            self._realizar_prestamo(libro, nombre, tipo_usuario)
        else:
            print(f"'{titulo}' no se encuentra en la biblioteca.")

    def devolver_libro(self, titulo):
        nombre = input("Ingresa tu nombre: ")
        libro = self.biblioteca.obtener_libro(titulo)
        if libro:
            self._realizar_devolucion(libro, nombre)
        else:
            print(f"'{titulo}' no se encuentra en la biblioteca.")

    def _realizar_prestamo(self, libro, nombre, tipo_usuario):
        if libro.disponible:
            print(f"{nombre} ha pedido prestado '{libro.titulo}'!")
            libro.disponible = False
        else:
            print(f"'{libro.titulo}' no está disponible en este momento.")

    def _realizar_devolucion(self, libro, nombre):
        if not libro.disponible:
            print(f"{nombre} ha devuelto '{libro.titulo}'. Gracias por regresarlo.")
            libro.disponible = True
        else:
            print(f"'{libro.titulo}' ya está disponible en la biblioteca.")

def main():
    biblioteca = BibliotecaVirtual()
    bib = Biblioteca()

    while True:
        print("\n--- Biblioteca Virtual Universidad Distrital ---")
        print("1. Mostrar biblioteca")
        print("2. Pedir prestado un libro")
        print("3. Devolver un libro")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            biblioteca.mostrar_biblioteca()
        elif opcion == "2":
            titulo = input("Ingresa el título del libro que deseas pedir prestado: ")
            tipo_usuario = input("Eres '1' (estudiante) o '2' (profesor): ")
            biblioteca.pedir_libro(titulo, tipo_usuario)
        elif opcion == "3":
            titulo = input("Ingresa el título del libro que deseas devolver: ")
            biblioteca.devolver_libro(titulo)
        elif opcion == "4":
            bib.guardar_en_archivo("biblioteca.txt")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()