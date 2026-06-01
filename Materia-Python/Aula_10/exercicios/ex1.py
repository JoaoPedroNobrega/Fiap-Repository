print('C - Clientes')
print('F - Funcionários')
print('V - Vips')
opcao = input('Escolha uma das opções acima: ')
preco = float(input('Informe o valor do produto: '))

match opcao:

    case 'C' | 'C':
        print(f'O valor final é: {preco}')
    case 'F' | 'f':
        print(f'O valor final é: {preco * 0.9}')
    case 'V' | 'v':
        print(f'O valor final é: {preco * 0.95}')
    case _:
        print('ERRO: Códio de cliente inválido')
