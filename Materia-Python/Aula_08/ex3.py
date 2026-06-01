# Faça um algoritmo que verifica se um número inteiro informado pelo usuário é múltiplo de 3, utilizando o match-case.

num = int(input('Escolha uma das opções acima: '))

match num % 3:
    case 0:
        print("O seu número é múltiplo de 3")
    case _:
        print("Seu número não é múltiplo de 3")