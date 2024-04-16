from abc import ABC, abstractmethod

class LaminasAcero:
    def __init__(self, implementador):
        self.implementador = implementador

    def producir_laminas(self):
        return self.implementador.producir_laminas()

class TrenLaminador(ABC):
    @abstractmethod
    def producir_laminas(self):
        pass

class TrenLaminador5Metros(TrenLaminador):
    def producir_laminas(self):
        print("Produciendo láminas de acero de 0.5” de espesor, 1.5 metros de ancho y 5 metros de largo.")

class TrenLaminador10Metros(TrenLaminador):
    def producir_laminas(self):
        print("Produciendo láminas de acero de 0.5” de espesor, 1.5 metros de ancho y 10 metros de largo.")

if __name__ == "__main__":

    laminas_5_metros = LaminasAcero(TrenLaminador5Metros())
    print("Láminas producidas por el tren laminador de 5 metros:")
    laminas_5_metros.producir_laminas()

    print("\n")

    laminas_10_metros = LaminasAcero(TrenLaminador10Metros())
    print("Láminas producidas por el tren laminador de 10 metros:")
    laminas_10_metros.producir_laminas()