# Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e False se
# for ímpar.

def validador(inteiro):
    if inteiro % 2 == 0:
        return True
    elif inteiro % 2 != 0:
        return False

num = int(input("Digite um número inteiro pra ver se é par: "))

verificador = validador(num)

print(verificador)