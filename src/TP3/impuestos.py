from abc import ABC, abstractmethod

class CalculadoraImpuestos(ABC):

    @abstractmethod
    def calcular_impuestos(self, monto_base: float) -> float:
        pass

class CalculadoraIVA(CalculadoraImpuestos):

    def calcular_impuestos(self, monto_base: float) -> float:
        return monto_base * 0.21

class CalculadoraIIBB(CalculadoraImpuestos):

    def calcular_impuestos(self, monto_base: float) -> float:
        return monto_base * 0.05

class CalculadoraContribucionesMunicipales(CalculadoraImpuestos):

    def calcular_impuestos(self, monto_base: float) -> float:
        return monto_base * 0.012

class FabricaDeImpuestos:


    @staticmethod
    def crear_calculadora(tipo_calculadora: str) -> CalculadoraImpuestos:


        if tipo_calculadora == "IVA":
            return CalculadoraIVA()
        elif tipo_calculadora == "IIBB":
            return CalculadoraIIBB()
        elif tipo_calculadora == "Municipal":
            return CalculadoraContribucionesMunicipales()
        else:
            raise ValueError("Tipo de calculadora de impuestos no válido")


if __name__ == "__main__":
    monto_base = 1000  

    calculadora_iva = FabricaDeImpuestos.crear_calculadora("IVA")
    impuesto_iva = calculadora_iva.calcular_impuestos(monto_base)

    calculadora_iibb = FabricaDeImpuestos.crear_calculadora("IIBB")
    impuesto_iibb = calculadora_iibb.calcular_impuestos(monto_base)

    calculadora_municipal = FabricaDeImpuestos.crear_calculadora("Municipal")
    impuesto_municipal = calculadora_municipal.calcular_impuestos(monto_base)

    impuesto_total = impuesto_iva + impuesto_iibb + impuesto_municipal

    print("Total de impuestos a pagar cuando el monto base es: ", monto_base)
    print(f"IVA: {impuesto_iva}")
    print(f"IIBB: {impuesto_iibb}")
    print(f"Contribuciones municipales: {impuesto_municipal}")
    print(f"Total: {impuesto_total}")