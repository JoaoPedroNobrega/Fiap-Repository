# Uma loja fornece 10% de desconto para funcionários e 5% de desconto para
# clientes vips. Faça um programa que calcule o valor total a ser pago por uma pessoa.
# O programa deverá solicitar o valor total da compra efetuada e um código que
# identifique se o comprador é um cliente comum ("C"), funcionário ("F") ou vip ("V").

print('C - Cliente')
print('F - Funcionário')
print('V - VIP')
opcao = input('Escolha uma das opções acima: ')

match opcao:
    case 'C' | 'F' | 'V' | 'c' | 'f' | 'v':
        valor = float(input("Informe o valor total: "))

match opcao:
    case 'C':
        print(f"O valor a ser pago é {valor}")
    case 'F':
        print(f"O valor a ser pago é {(valor * 0.9)}")
    case 'V':
        print(f"O valor a ser pago é {(valor * 0.95)}")
    case _:
        print("Opção Inválida")