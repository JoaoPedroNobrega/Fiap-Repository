# Escreva um algoritmo que solicite 10 números e informe qual foi o menor número digitado.

cont = 0

menor = int(input("Numero: "))

while cont < 9:
    numero = int(input("Numero: "))
    if numero > menor:
        menor = numero
    cont += 1

print(numero)