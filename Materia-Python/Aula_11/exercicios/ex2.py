cont = 0
cont_menor = 0

while cont < 10:
    idade = int(input('Digie sua idade: '))
    if idade  < 18:
        cont_menor += 1
    cont += 1
print('O número de pessoas com menos de 18 anos é {cont_menor}')
