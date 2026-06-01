# Crie um algoritmo que identifique e exiba todos os números primos menores que 1 milhão.

n = 1

cont_divisores = 0
for a in range (1, 1000000):
    for i in range(1, n+1):
        if n % i == 0:
            cont_divisores += 1
            if cont_divisores > 2:
                break

    if cont_divisores == 2:
        print('É PRIMOOOOOOOO')
    else:
        print('Não é primooooooo')