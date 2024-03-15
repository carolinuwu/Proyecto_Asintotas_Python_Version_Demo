from HelperGraficador import HelperGraficador
from HelperConRegEx import HelperConRegEx
import numpy as np

class AsintotasHelper:
    def __init__(self):
        self.funcion = None
        self.asintotas = None
        self.pedir_funcion()
        self.procesarFuncion()

    def __init__(self, funcion):
        self.funcion = funcion
        self.asintotas = None
        self.procesarFuncion()

    def pedir_funcion(self):
        self.funcion = input('Por favor ingresa una función lineal compuesta como máximo de un binomio en numerador y de un binomio en denominador: ')

    def procesarFuncion(self):
        if self.funcion:
            funcion_sin_las_x = self.funcion.split('x')
            if len(funcion_sin_las_x) > 1:
                funcion_sin_el_cociente = ' '.join(funcion_sin_las_x)
                funcion_sin_el_cociente = funcion_sin_el_cociente.split('/')

                helper_expresiones_regulares = HelperConRegEx(str(funcion_sin_el_cociente))
                valores_numericos = helper_expresiones_regulares.retornarListaDeValoresNumericos()
                if valores_numericos is not None:
                    asintota_vertical_valor_escalar = -(valores_numericos[3] / valores_numericos[2])
                    asintota_horizontal_valor_escalar = - (valores_numericos[0] / valores_numericos[2])

                    asintota_vertical = {'tipo': 'vertical', 'valor': asintota_vertical_valor_escalar}
                    asintota_horizontal = {'tipo': 'horizontal', 'valor': asintota_horizontal_valor_escalar}
                    self.asintotas = [asintota_vertical, asintota_horizontal]

                    helper_graficador = HelperGraficador()
                    helper_graficador.graficar(self.funcion, np.linspace(-10, 10, 100))
                    helper_graficador.graficar_asintotas(self.asintotas)
            else:
                asintota_vertical = None
                asintota_horizontal = funcion_sin_las_x[1]
        else:
            print("No me proporcionaste una función.")
