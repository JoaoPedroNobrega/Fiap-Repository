# Escreva um programa que calcule o somatório de todos os números que sejam múltiplos de 3 ou
# múltiplos de 5 no intervalo de 1 a 999 (menores que 1000)


soma = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(soma)