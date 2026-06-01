numero = int(input('Digite um número: '))

match numero % 3:
    case 0:
        print('É um múltiplo de 3')
    case _:
        print('Não é múltiplo de 3')