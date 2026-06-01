# Faça um programa que receba um número, digitado pelo usuário e mostre
# o menu para selecionar o tipo de cálculo que deve ser realizado.
# Exiba o valor do cálculo efetuado.

# 1 - O dobro
# 2 - A metade
# 3 - 10% do número

print('1 - O dobro')
print('2 - A metade')
print('3 - 10% do número')
opcao = int(input('Escolha uma das opções acima: '))

match opcao:
    case 1 | 2 | 3:
        a = float(input("Informe um número: "))

match opcao:
    case 1:
        print(f'O dobro do número: {a * 2}')
    case 2:
        print(f'A metade do número: {a / 2}')
    case 3:
        print(f'10% do número: {a * 0.1}')
    case _:
        print("ERRO: Opção Inválida")