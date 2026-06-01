# Faça um algoritmo que solicite o código da palestra de um evento e exiba o local
# em que ela será realizada, conforme a tabela a seguir

print('1 - Linux')
print('2 - Banco de Dados')
print('3 - Windows Server')
print('4 - Lógica de Programação')
cod = int(input('Informe o código da palestra pra saber onde será realizada: '))

match cod:
    case 1:
        print("A palestra de Linux ocorrerá no Auditório 1")
    case 2:
        print("A palestra de Linux ocorrerá no Auditório 2")
    case 3:
        print("A palestra de Linux ocorrerá no Auditório 3")
    case 4:
        print("A palestra de Linux ocorrerá no Auditório Prinicipal")
    case _:
        print("Opção Inválida")