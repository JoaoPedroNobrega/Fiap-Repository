#solicitar a idade de 10 pessoas e calcular a média das idades

cont = 0        # variável contadora
soma = 0        # variávelsomadora
quantidade = int(input('Informe o número de pessoas que vão responder: '))

while cont < quantidade:
    idade = int(input('Digite sua idade: '))
    soma += idade
    cont += 1

media = soma / 10
print(f'Média das idades: {media:.2f}')