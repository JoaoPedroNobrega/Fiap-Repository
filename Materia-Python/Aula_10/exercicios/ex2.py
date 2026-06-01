print('1 - O Dobro')
print('2 - A Metade')
print('3 - 10% do valor')
opcao = int(input('Escolha uma das opções acima: '))
numero = float(input('Digite um número: '))

match opcao:
    case 1:
        print(f'Dobro do número: {numero * 2}')
    case 2:
        print(f'A metade do número: {numero / 2}')
    case 3:
        print(f'10% do valor: {numero * 0.10}')
    case _:
        print('A opção selecionada é inválida')
