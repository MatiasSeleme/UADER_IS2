class TextoFormato:
    def __init__(self, estilo, tamano, color):
        self.estilo = estilo
        self.tamano = tamano
        self.color = color

    def aplicar_formato(self, contenido):
        return f"<{self.estilo}>{contenido}</{self.estilo}>"

class TextoFormatoFactory:
    _formatos = {}

    @staticmethod
    def obtener_formato(estilo, tamano, color):
        clave = (estilo, tamano, color)
        if clave not in TextoFormatoFactory._formatos:
            TextoFormatoFactory._formatos[clave] = TextoFormato(estilo, tamano, color)
        return TextoFormatoFactory._formatos[clave]

class Documento:
    def __init__(self):
        self._contenido = []
        self._formatos = {}

    def agregar_texto(self, texto, estilo, tamano, color):
        formato = TextoFormatoFactory.obtener_formato(estilo, tamano, color)
        self._contenido.append((texto, formato))

    def imprimir(self):
        for texto, formato in self._contenido:
            texto_formateado = formato.aplicar_formato(texto)
            print(texto_formateado)

if __name__ == "__main__":
    documento = Documento()
    documento.agregar_texto("Texto en negrita", "negrita", 12, "rojo")
    documento.agregar_texto("Texto en cursiva", "cursiva", 10, "azul")
    documento.agregar_texto("Texto subrayado", "subrayado", 14, "verde")
    documento.agregar_texto("Otro texto en negrita", "negrita", 12, "rojo")

    documento.imprimir()