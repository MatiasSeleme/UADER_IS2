from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class AvionBuilder(ABC):
    """
    The AvionBuilder interface specifies methods for creating the different parts of
    the Avion objects.
    """

    @property
    @abstractmethod
    def avion(self) -> None:
        pass

    @abstractmethod
    def construir_body(self) -> None:
        pass

    @abstractmethod
    def construir_turbinas(self) -> None:
        pass

    @abstractmethod
    def construir_alas(self) -> None:
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass


class AvionComercialBuilder(AvionBuilder):
    """
    The Concrete AvionBuilder classes follow the AvionBuilder interface and provide
    specific implementations of the building steps for commercial airplanes.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank avion object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._avion = Avion()

    @property
    def avion(self) -> Avion:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base AvionBuilder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getAvion` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        avion = self._avion
        self.reset()
        return avion

    def construir_body(self) -> None:
        self._avion.add("Body comercial")

    def construir_turbinas(self) -> None:
        self._avion.add("2 turbinas comerciales")

    def construir_alas(self) -> None:
        self._avion.add("2 alas comerciales")

    def construir_tren_aterrizaje(self) -> None:
        self._avion.add("Tren de aterrizaje comercial")


class AvionEjecutivoBuilder(AvionBuilder):
    """
    The Concrete AvionBuilder classes follow the AvionBuilder interface and provide
    specific implementations of the building steps for executive airplanes.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank avion object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._avion = Avion()

    @property
    def avion(self) -> Avion:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base AvionBuilder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getAvion` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        avion = self._avion
        self.reset()
        return avion

    def construir_body(self) -> None:
        self._avion.add("Body ejecutivo")

    def construir_turbinas(self) -> None:
        self._avion.add("2 turbinas ejecutivas")

    def construir_alas(self) -> None:
        self._avion.add("2 alas ejecutivas")

    def construir_tren_aterrizaje(self) -> None:
        self._avion.add("Tren de aterrizaje ejecutivo")


class Avion:
    """
    It makes sense to use the Builder pattern only when your aviones are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated aviones. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Avion parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing aviones according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> AvionBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: AvionBuilder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled avion.
        """
        self._builder = builder

    """
    The Director can construct several avion variations using the same
    building steps.
    """

    def build_comercial_avion(self) -> None:
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()

    def build_ejecutivo_avion(self) -> None:
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    comercial_builder = AvionComercialBuilder()
    ejecutivo_builder = AvionEjecutivoBuilder()

    director.builder = comercial_builder
    print("Comercial Avion: ")
    director.build_comercial_avion()
    comercial_builder.avion.list_parts()

    print("\n")

    director.builder = ejecutivo_builder
    print("Ejecutivo Avion: ")
    director.build_ejecutivo_avion()
    ejecutivo_builder.avion.list_parts()

    print("\n")
