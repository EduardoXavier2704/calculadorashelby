import math
from calculadora import Calculadora
from mostrarmenu import mostrar_menu
from mostrarmenu import obter_operacao
from mostrarmenu import obter_numero
from mostrarmenu import obter_input


def executar_calculadora(calculadora):
    while True:
        mostrar_menu(calculadora)
        operacao = obter_operacao("Digite o número da operação desejada: ")
        if operacao == 1:
            x = obter_numero("Digite o primeiro número: ")
            y = obter_numero("Digite o segundo número: ")
            resultado = calculadora.adicionar(x, y)
            print("O resultado é:", resultado)
        elif operacao == 2:
            x = obter_numero("Digite o primeiro número: ")
            y = obter_numero("Digite o segundo número: ")
            resultado = calculadora.subtrair(x, y)
            print("O resultado é:", resultado)
        elif operacao == 3:
            x = obter_numero("Digite o primeiro número: ")
            y = obter_numero("Digite o segundo número: ")
            resultado = calculadora.multiplicar(x, y)
            print("O resultado é:", resultado)
        elif operacao == 4:
            x = obter_numero("Digite o dividendo: ")
            y = obter_numero("Digite o divisor: ")
            try:
                resultado = calculadora.dividir(x, y)
                print("O resultado é:", resultado)
            except ValueError as e:
                print(e)
        elif operacao == 5:
            x = obter_numero("Digite a base: ")
            y = obter_numero("Digite o expoente: ")
            resultado = calculadora.potencia(x, y)
            print("O resultado é:", resultado)
        elif operacao == 6:
            x = obter_numero("Digite o número: ")
            if x < 0:
                print("Não é possível calcular a raiz quadrada de um número negativo")
            else:
                resultado = calculadora.raiz_quadrada(x)
                print("O resultado é:", resultado)
        elif operacao == 7:
            x = obter_numero("Digite a base: ")
            y = obter_numero("Digite o expoente: ")
            resultado = calculadora.exponencia(x, y)
            print("O resultado é:", resultado)
        elif operacao == 8:
            x = obter_numero("Digite o ângulo em radianos: ")
            resultado = calculadora.seno(x)
            print("O resultado é:", resultado)
        elif operacao == 9:
            x = obter_numero("Digite o ângulo em radianos: ")
            resultado = calculadora.cosseno(x)
            print("O resultado é:", resultado)
        elif operacao == 10:
            x = obter_numero("Digite o ângulo em radianos: ")
            resultado = calculadora.tangente(x)
            print("O resultado é:", resultado)
        elif operacao == 11:
            x = obter_numero("Digite o ângulo em graus: ")
            resultado = calculadora.seno(x)
            print("O resultado é:", resultado)
        elif operacao == 12:
            x = obter_numero("Digite o ângulo em graus: ")
            resultado = calculadora.cosseno(x)
            print("O resultado é:", resultado)
        elif operacao == 13:
            x = obter_numero("Digite o ângulo em graus: ")
            resultado = calculadora.tangente(x)
            print("O resultado é:", resultado)
        elif operacao == 14:
            calculadora.alterar_modo()
            print("Modo de ângulo alterado para", calculadora.modo_angulo)
        elif operacao == 15:
            expressao = input("Digite a expressão matemática: ")
            resultado = eval(expressao)
            print("O resultado é:", resultado)
        elif operacao == 'e':
            break
        elif operacao == 16:
            break
        else:
            print("Operação inválida, tente novamente!")

def main():
    calculadora = Calculadora()
    executar_calculadora(calculadora)

main()