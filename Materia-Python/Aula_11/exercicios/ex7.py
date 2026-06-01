num = 1

numero = int(input('Digite um número: '))
cont = numero

while numero < 0:
    print('O número deve ser postivo. Informe novamente.')
    numero = int(input('Digite um número positivo: '))




while cont >= 1:
    num *= cont
    cont -= 1

print(f'{numero} = {fatorial}')
