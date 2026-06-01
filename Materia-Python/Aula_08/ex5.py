# Faça um algoritmo que exiba um Menu com as opções de um cardápio de restaurante.
# O cliente deve escolher o código do prato desejado e na sequência, informar se aceita pagar uma taxa de serviço de 10%.
# Se o usuário aceitar, mostrar o valor final (valor do prato + 10%), caso contrário, mostrar somente o valor do prato


print('1 - Picanha')
print('2 - Lasanha')
print('3 - Strogonoff')
print('4 - Bife Acebolado')
print('5 - Pão com Ovo')
prato = int(input('Informe o código da palestra pra saber onde será realizada: '))

match prato:
    case 1 | 2 | 3 | 4| 5:
        print('S - SIM/YES')
        print('N - NÃO/NO')
        servico = input('Aceita pagar uma taxa de 10% pela taxa de serviço?: ')
match prato:
    case 1:
        match servico:
            case 'S'|'s':
                print(f"O valor a ser pago é {25 + (25 * 0.1)}")
            case 'N'|'n':
                print(f"O valor a ser pago é {25}")
            case _:
                print("ERRO: Opção inválida na pergunta de taxa de serviço")
    case 2:
        match servico:
            case 'S' | 's':
                print(f"O valor a ser pago é {20 + (20 * 0.1)}")
            case 'N' | 'n':
                print(f"O valor a ser pago é {20}")
            case _:
                print("ERRO: Opção inválida na pergunta de taxa de serviço")
    case 3:
        match servico:
            case 'S' | 's':
                print(f"O valor a ser pago é {20 + (20 * 0.1)}")
            case 'N' | 'n':
                print(f"O valor a ser pago é {20}")
            case _:
                print("ERRO: Opção inválida na pergunta de taxa de serviço")
    case 4:
        match servico:
            case 'S' | 's':
                print(f"O valor a ser pago é {15 + (15 * 0.1)}")
            case 'N' | 'n':
                print(f"O valor a ser pago é {15}")
            case _:
                print("ERRO: Opção inválida na pergunta de taxa de serviço")
    case 5:
        match servico:
            case 'S' | 's':
                print(f"O valor a ser pago é {5 + (5 * 0.1)}")
            case 'N' | 'n':
                print(f"O valor a ser pago é {5}")
            case _:
                print("ERRO: Opção inválida na pergunta de taxa de serviço")
    case _:
        print("ERRO: Opção Inválida no tipo de prato")