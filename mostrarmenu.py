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