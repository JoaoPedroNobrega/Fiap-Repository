# Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.

def dobrando(inteiro):
    dobro = inteiro * 2
    return dobro

num = int(input("Digite um número inteiro: "))

dobro_calculo = dobrando(num)

print(dobro_calculo)