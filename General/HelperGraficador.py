import numpy as np
import matplotlib.pyplot as plt

class HelperGraficador:
    def __init__(self):
        pass

    def formula(self, x, funcion):
        return eval(funcion)

    def graficar(self, funcion, rango_deseado):
        #en un principio esta funcion siempre va a ser igual ya que
        #todas las funciones van a ser de grado uno pero cuando psoteriormente pueda añadir mas tipos de funciones
        #va a ser mas bonito uwu.
        x = np.array(rango_deseado)
        y = self.formula(x, funcion)
        plt.plot(x, y)
        plt.title("Grafico de f(x) ")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

    def graficar_asintotas(self, asintotas):
        x = np.linspace(-15, 15, 1000)
        for asintota in asintotas:
            if asintota['tipo'] == 'vertical':
                plt.axvline(x=asintota['valor'], color='red', linestyle='--', label='AV')
            elif asintota['tipo'] == 'horizontal':
                plt.axhline(y=asintota['valor'], color='red', linestyle='--', label='AH')

        plt.legend()
        plt.show()

