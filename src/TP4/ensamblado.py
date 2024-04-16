from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class Subconjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

pieza1 = Pieza("Pieza 1")
pieza2 = Pieza("Pieza 2")
pieza3 = Pieza("Pieza 3")
pieza4 = Pieza("Pieza 4")
pieza5 = Pieza("Pieza 5")
pieza6 = Pieza("Pieza 6")
pieza7 = Pieza("Pieza 7")
pieza8 = Pieza("Pieza 8")
pieza9 = Pieza("Pieza 9")
pieza10 = Pieza("Pieza 10")
pieza11 = Pieza("Pieza 11")
pieza12 = Pieza("Pieza 12")

subconjunto1 = Subconjunto("Subconjunto 1")
subconjunto2 = Subconjunto("Subconjunto 2")
subconjunto3 = Subconjunto("Subconjunto 3")

subconjunto1.agregar_componente(pieza1)
subconjunto1.agregar_componente(pieza2)
subconjunto1.agregar_componente(pieza3)
subconjunto1.agregar_componente(pieza4)

subconjunto2.agregar_componente(pieza5)
subconjunto2.agregar_componente(pieza6)
subconjunto2.agregar_componente(pieza7)
subconjunto2.agregar_componente(pieza8)

subconjunto3.agregar_componente(pieza9)
subconjunto3.agregar_componente(pieza10)
subconjunto3.agregar_componente(pieza11)
subconjunto3.agregar_componente(pieza12)

producto_principal = Subconjunto("Producto Principal")
producto_principal.agregar_componente(subconjunto1)
producto_principal.agregar_componente(subconjunto2)
producto_principal.agregar_componente(subconjunto3)

producto_principal.mostrar()
