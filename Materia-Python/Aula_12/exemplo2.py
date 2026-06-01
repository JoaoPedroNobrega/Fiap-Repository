#Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a
#tabuada de N.
#Exemplo: para N = 7
#7 x 1 = 7
#7 x 2 = 14
# ...
#7 x 10 = 70

n = int(input("Digite qual número deseja saber a tabuada: "))
cont = 0

while cont < 10:
    cont += 1
    tab = n * cont
    print(f"{n} x {cont} = {tab}")