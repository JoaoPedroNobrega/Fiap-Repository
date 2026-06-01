# Faça um programa para uma calculadora simples com as seguintes operações: adição, subtração,
# multiplicação e divisão.
# O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
# Calculadora:
# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão
# 5 - Sair do programa
# Selecione sua opção:
# Crie uma função chamada Menu, que exiba o menu acima e retorna a opção do usuário para o
# programa principal. Se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
# opção válida.
# De acordo com a opção do usuário, chame uma das seguintes funções: adicao, subtracao,
# multiplicacao, divisao, passando como parâmetros dois números também informados pelo usuário.
# Após a execução da operação o programa volta a apresentar o menu inicial até que o usuário encerre
# o programa com a opção 5.
def Menu(nome):
    while True:
        print('Calculadora:')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair do programa')
        opcao = int(input('Selecione sua opção: '))
        if 1 <= opcao <= 5:
            return opcao
        print('Opção inválida. Tente novamente.')

Menu("Joao")