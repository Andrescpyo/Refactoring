class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nDisponible: {'Sí' if self.disponible else 'No'}"