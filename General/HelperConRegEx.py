import re

class HelperConRegEx:
    #Se va a encargar de recibir una funcion y a partir de ella retornar una lista de los elementos numericos que la conforman

    def __init__(self, funcion):
        self.funcion = funcion
        self.retornarListaDeValoresNumericos()

    def retornarListaDeValoresNumericos(self):
        patron_numero = r'-?\d+'
        valores = re.findall(patron_numero, self.funcion)
        self.valores_numericos = [int(num) for num in valores]
        return self.valores_numericos


