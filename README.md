# Refactoring
# BibliotecaVirtual
## Andres Cerdas Padilla  20231020053
## Fabian Yesith Aguilar Jimenez  20231020093

# ----------------------Documentación------------------------
### 1. `libro.py`

#### Refactoring:
- *Responsabilidad Única (SRP)*: La clase `Libro` tiene la única responsabilidad de representar un libro. No tiene funcionalidades adicionales, lo que cumple con el principio SRP.

#### Principios SOLID:
- *Abierto/Cerrado (OCP)*: La clase `Libro` está cerrada para modificaciones, pero puede ser extendida para añadir métodos o propiedades adicionales en el futuro, cumpliendo con el principio OCP.

### 2. `biblioteca.py`

#### Refactoring:
- *Responsabilidad Única (SRP)*: La clase `Biblioteca` se encarga de manejar las operaciones de la biblioteca (cargar, guardar, agregar, obtener), cumpliendo con el principio SRP.

#### Principios SOLID:
- *Abierto/Cerrado (OCP)*: La clase `Biblioteca` está cerrada para modificaciones, pero puede ser extendida para añadir funcionalidades relacionadas con la biblioteca sin alterar su código existente.
- *Sustitución de Liskov (LSP)*: Aunque no hay subclases en este archivo, el diseño permite la extensión sin afectar el comportamiento existente de la clase `Biblioteca`.

### 3. `biblioteca_virtual.py`

#### Refactoring:
- *Responsabilidad Única (SRP)*: La clase `BibliotecaVirtual` se encarga de interactuar con el usuario y gestionar las operaciones relacionadas con la biblioteca, cumpliendo con el principio SRP.

#### Principios SOLID:
- *Abierto/Cerrado (OCP)*: La clase `BibliotecaVirtual` está cerrada para modificaciones, pero puede ser extendida para añadir funcionalidades relacionadas con la interacción del usuario sin alterar su código existente.
- *Sustitución de Liskov (LSP)*: La clase `BibliotecaVirtual` utiliza la clase `Biblioteca` de manera que las instancias de `Biblioteca` pueden ser sustituidas sin afectar el comportamiento de `BibliotecaVirtual`.
- *Inversión de Dependencia (DIP)*: La clase `BibliotecaVirtual` depende de una instancia de la clase `Biblioteca`, cumpliendo con el principio DIP. Las dependencias están manejadas adecuadamente, lo que permite una fácil sustitución de componentes sin afectar el comportamiento del programa.
