print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('Escolha uma das opções acima: '))
numero1 = float(input('informe o primeiro número: '))
numero2 = float(input('informe o primeiro número: '))

if opcao == 1:
    print(f'Resultado da Soma: {numero1 + numero2}')
elif opcao == 2:
    print(f'Resultado da Subtração: {numero1 - numero2}')
elif opcao == 3:
    print(f'Resultado da Multiplicação: {numero1 * numero2}')
elif opcao == 4:
    if numero2 != 0:
        print(f'Resultado da Divisão: {numero1 / numero2}')
    else:
        print('Não é possível fazer uma divisão por zero')
else:
    print('Opção Inválida')