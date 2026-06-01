n = int(input("Informe um número: "))

cont_divisores = 0
for i in range(1, n+1):
    if n % i == 0:
        cont_divisores += 1
        if cont_divisores > 2:
            break

if cont_divisores == 2:
    print('É PRIMOOOOOOOO')
else:
    print('Não é primooooooo')