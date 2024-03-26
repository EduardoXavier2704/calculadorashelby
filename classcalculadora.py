import math

class Calculator:
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

def mostrar_menu(calculadora):
    print("Calculadora Científica")
    print("-------------------")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potencia")
    print("6. Raiz Quadrada")
    print("7. Exponencia")
    print("8. Seno (em radianos)")
    print("9. Cosseno (em radianos)")
    print("10. Tangente (em radianos)")
    print("11. Seno (em graus)")
    print("12. Cosseno (em graus)")
    print("13. Tangente (em graus)")
    print("14. Alterar modo de ângulo (atualmente em " + calculadora.modo_angulo + ")")
    print("15. Sair")

def obter_input(texto):
    return input(texto)

def obter_numero(texto):
    return float(obter_input(texto))

def obter_operacao(texto):
    return int(obter_input(texto))
