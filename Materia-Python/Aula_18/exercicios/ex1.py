# Escreva um programa para solicitar as notas de duas provas. Faça uma função que receba as duas
# notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. Considere
# 6.0 a média mínima para aprovação.

def calcularMedia(nota1,nota2):
    media = (nota1+nota2)/2
    if media >= 6:
        print("Você foi aprovado!")
    elif media < 6:
        print("Você foi reprovado!")

num1 = float(input("Digite a nota 1: "))
num2 = float(input("Digite a nota 2: "))

calcularMedia(num1,num2)
