#  Escreva um algoritmo que solicite um número
#  inteiro e exiba todos os divisores desse número.

n = int(input("Informe um número: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)