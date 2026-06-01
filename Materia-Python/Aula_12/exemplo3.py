# Construa um algoritmo que mostre todos os valores ímpares entre
# X e Y, onde X e Y são fornecidos pelo usuário.

x = int(input("Digite o número inicial pra saber onde começa a lista: "))
y = int(input("Digite o número inicial pra saber onde termina a lista: "))

while x < y:
    if x % 2 != 0:
        print(x)
    x += 1