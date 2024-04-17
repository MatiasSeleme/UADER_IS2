class Hamburguesa:
    def __init__(self):
        self.tipo = None
        self.pan = None
        self.carne = None
        self.ingredientes_extra = []

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_pan(self, pan):
        self.pan = pan

    def set_carne(self, carne):
        self.carne = carne

    def agregar_ingrediente_extra(self, ingrediente):
        self.ingredientes_extra.append(ingrediente)

    def entregar_en_mostrador(self):
        print("La hamburguesa está lista para ser recogida en el mostrador.")

    def enviar_por_delivery(self):
        print("La hamburguesa será enviada por delivery.")

    def __str__(self):
        return f"Hamburguesa {self.tipo} con {self.pan}, {self.carne} y {', '.join(self.ingredientes_extra)}"


class HamburguesaBuilder:
    def __init__(self):
        self.hamburguesa = Hamburguesa()

    def set_tipo(self, tipo):
        self.hamburguesa.set_tipo(tipo)
        return self

    def set_pan(self, pan):
        self.hamburguesa.set_pan(pan)
        return self

    def set_carne(self, carne):
        self.hamburguesa.set_carne(carne)
        return self

    def agregar_ingrediente_extra(self, ingrediente):
        self.hamburguesa.agregar_ingrediente_extra(ingrediente)
        return self

    def build(self):
        return self.hamburguesa


builder = HamburguesaBuilder()
hamburguesa = builder.set_tipo("Clásica").set_pan("Brioche").set_carne("Res").agregar_ingrediente_extra("Queso").build()

print(hamburguesa)
hamburguesa.entregar_en_mostrador()
hamburguesa.enviar_por_delivery()
