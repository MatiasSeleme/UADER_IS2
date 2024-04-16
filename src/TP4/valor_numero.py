from abc import ABC, abstractmethod

class Numero(ABC):
    @abstractmethod
    def obtener_valor(self):
        pass

class NumeroBase(Numero):
    def __init__(self, valor):
        self.valor = valor

    def obtener_valor(self):
        return self.valor

class NumeroDecorator(Numero):
    def __init__(self, numero):
        self.numero = numero

    def obtener_valor(self):
        return self.numero.obtener_valor()

class SumarDos(NumeroDecorator):
    def obtener_valor(self):
        return self.numero.obtener_valor() + 2

class MultiplicarPorDos(NumeroDecorator):
    def obtener_valor(self):
        return self.numero.obtener_valor() * 2

class DividirPorTres(NumeroDecorator):
    def obtener_valor(self):
        return self.numero.obtener_valor() / 3

if __name__ == "__main__":
    numero_base = NumeroBase(5)

    print("Número sin modificaciones:")
    print(numero_base.obtener_valor())

    print("\nNúmero después de sumarle 2:")
    numero_modificado = SumarDos(numero_base)
    print(numero_modificado.obtener_valor())

    print("\nNúmero después de sumarle 2 y multiplicar por 2:")
    numero_modificado = MultiplicarPorDos(SumarDos(numero_base))
    print(numero_modificado.obtener_valor())

    print("\nNúmero después de sumarle 2, multiplicar por 2 y dividir por 3:")
    numero_modificado = DividirPorTres(MultiplicarPorDos(SumarDos(numero_base)))
    print(numero_modificado.obtener_valor())
