print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
opcao = int(input('Escolha uma das opções acima: '))

match opcao:
    case 1 | 2 | 3 | 4:
        a = float(input("Informe um número: "))
        b = float(input("Informe outro número: "))

match opcao:
    case 1:
        print(f'Resultado da soma: {a + b}')
    case 2:
        print(f'Resultado da subtração: {a - b}')
    case 3:
        print(f'Resultado da multiplicação: {a * b}')
    case 4:
        match b:
            case 0:
                print("Erro: não é possível dividir por zero")
            case _:
                print(f'Resultado da divisão: {a / b}')
    case _:
        print("ERRO: Opção Inválida")