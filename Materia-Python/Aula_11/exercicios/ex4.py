n = int(input('Digite o número de vezes que deseja rodar o programa: '))
somapar = 0
somaimpar = 0
quantpar = 0
quantimpar = 0

cont = 1
while cont <= n:
    num = int(input(f"Digite o {cont}º número: "))
    if num % 2 == 0:
        somapar += num
        quantpar += 1
    else :
        somaimpar += num
        quantimpar += 1
    cont += 1

if quantpar > 0:
    mediapar = somapar / quantpar
    print(f'Média dos números pares: {mediapar}')
else:
    print('Nenhum número par foi informado')
if quantimpar > 0:
    mediaimpar = somaimpar / quantimpar
    print(f'Média dos números pares: {mediaimpar}')
else:
    print('Nenhum núemro par foi informado')