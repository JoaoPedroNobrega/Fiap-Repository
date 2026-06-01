# solicitar 10 números e contar a quantidade de pares

cont = 0                # variável contadora
cont_pares = 0          # variável contadora
while cont < 10:
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        cont_pares += 1 # incrementa a variável contadora de pares
    cont += 1           # incrementa a variável contadora de repetições
