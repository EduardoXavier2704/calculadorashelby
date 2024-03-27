import math

class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.modo_angulo = 'rad'

    def adicionar(self, x, y):
        self.resultado = x + y
        return self.resultado

    def subtrair(self, x, y):
        self.resultado = x - y
        return self.resultado

    def multiplicar(self, x, y):
        self.resultado = x * y
        return self.resultado

    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida")
        self.resultado = x / y
        return self.resultado
    
    def potencia(self, x, y):
        self.resultado = x ** y
        return self.resultado

    def raiz_quadrada(self, x):
        self.resultado = math.sqrt(x)
        return self.resultado

    def exponencia(self, x, y):
        self.resultado = math.exp(y * math.log(x))
        return self.resultado

    def seno(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.sin(x)
        return self.resultado

    def cosseno(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.cos(x)
        return self.resultado

    def tangente(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.tan(x)
        return self.resultado

    def alterar_modo(self):
        if self.modo_angulo == 'rad':
            self.modo_angulo = 'deg'
        else:
            self.modo_angulo = 'rad'

