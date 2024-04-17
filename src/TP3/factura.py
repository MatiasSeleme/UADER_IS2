import copy

class Factura:
    def __init__(self, importe):
        self.importe = importe

    def calcular_iva(self, tipo_iva):
        if tipo_iva == "Responsable":
            return self.importe * 0.21
        elif tipo_iva == "No Inscripto":
            return 0
        elif tipo_iva == "Exento":
            return 0
        else:
            raise ValueError("Tipo de IVA no válido")

    def __str__(self):
        tipo_iva = "Responsable"  # Se puede modificar según el tipo de cliente
        total_con_iva = self.importe + self.calcular_iva(tipo_iva)
        return f"Factura - Importe: {self.importe}, Total con IVA ({tipo_iva}): {total_con_iva}"

class FacturaPrototype:
    def __init__(self):
        self.prototypes = {}

    def registrar_prototipo(self, tipo_iva, factura):
        self.prototypes[tipo_iva] = factura

    def obtener_prototipo(self, tipo_iva):
        if tipo_iva in self.prototypes:
            return copy.deepcopy(self.prototypes[tipo_iva])
        else:
            raise ValueError("Prototipo de factura no encontrado")

prototype_factory = FacturaPrototype()

factura_responsable = Factura(100)
prototype_factory.registrar_prototipo("Responsable", factura_responsable)

factura_no_inscripto = Factura(100)
prototype_factory.registrar_prototipo("No Inscripto", factura_no_inscripto)

factura_exento = Factura(100)
prototype_factory.registrar_prototipo("Exento", factura_exento)

factura_cliente_responsable = prototype_factory.obtener_prototipo("Responsable")
factura_cliente_no_inscripto = prototype_factory.obtener_prototipo("No Inscripto")
factura_cliente_exento = prototype_factory.obtener_prototipo("Exento")

print(factura_cliente_responsable)
print(factura_cliente_no_inscripto)
print(factura_cliente_exento)

