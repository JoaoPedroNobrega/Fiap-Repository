# Solicitar a idade de N pessoas e calcular a média das idades
# Finalizar a entrada de dados quando o usuário indicar uma idade negaiva

soma = 0
cont = 0

while True:
    idade = int(input('Informe a idade: '))
    if idade < 0:
        break
    soma += idade
    cont += 1

media = soma / cont
print(f'A média das idades é: {media}')

