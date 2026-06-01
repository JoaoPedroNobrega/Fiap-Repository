# Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é
# fornecido pelo usuário.

n = int(input("Digite até que número quer saber quais são ímpares: "))

cont_impares = 0
num = 0
while num < n:
    num += 1
    if num % 2 != 0:
        print(num)
        cont_impares += 1
print(f"Foram encontrados {cont_impares} números ímpares")