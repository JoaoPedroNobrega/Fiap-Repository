# Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o
# número lido é um número perfeito ou não. Número perfeito é aquele cuja soma de
# seus divisores, exceto ele próprio, é igual ao próprio número.
# Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6

n = int(input("Digite um número pra ver se ele é perfeito ou não: "))

soma = 0
cont = 1

while cont < n:
    if n % cont == 0:
        soma += cont
    cont += 1

if soma == n:
    print("É perfeito!")
else:
    print("Não é perfeito :(")

