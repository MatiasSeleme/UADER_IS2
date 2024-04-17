from abc import ABC, abstractmethod

# Interfaz Abstracta de Fábrica GUI
class FabricaGUI(ABC):
    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_menu(self):
        pass

    @abstractmethod
    def crear_ventana(self):
        pass

# Fábrica Concreta para Windows
class FabricaWindows(FabricaGUI):
    def crear_boton(self):
        return BotonWindows()

    def crear_menu(self):
        return MenuWindows()

    def crear_ventana(self):
        return VentanaWindows()

# Fábrica Concreta para macOS
class FabricaMacOS(FabricaGUI):
    def crear_boton(self):
        return BotonMacOS()

    def crear_menu(self):
        return MenuMacOS()

    def crear_ventana(self):
        return VentanaMacOS()

# Interfaz para Botones
class Boton(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# Implementación de Botón para Windows
class BotonWindows(Boton):
    def renderizar(self):
        print("Renderizando Botón para Windows")

# Implementación de Botón para macOS
class BotonMacOS(Boton):
    def renderizar(self):
        print("Renderizando Botón para macOS")

# Interfaz para Menús
class Menu(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Implementación de Menú para Windows
class MenuWindows(Menu):
    def mostrar(self):
        print("Mostrando Menú para Windows")

# Implementación de Menú para macOS
class MenuMacOS(Menu):
    def mostrar(self):
        print("Mostrando Menú para macOS")

# Interfaz para Ventanas
class Ventana(ABC):
    @abstractmethod
    def abrir(self):
        pass

# Implementación de Ventana para Windows
class VentanaWindows(Ventana):
    def abrir(self):
        print("Abriendo Ventana para Windows")

# Implementación de Ventana para macOS
class VentanaMacOS(Ventana):
    def abrir(self):
        print("Abriendo Ventana para macOS")

if __name__ == "__main__":
    # Crear Fábrica Concreta para Windows
    fabrica_windows = FabricaWindows()
    boton_windows = fabrica_windows.crear_boton()
    boton_windows.renderizar()

    # Crear Fábrica Concreta para macOS
    fabrica_macos = FabricaMacOS()
    boton_macos = fabrica_macos.crear_boton()
    boton_macos.renderizar()
