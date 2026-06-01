# Escreva um algoritmo que solicite quinze números informados pelo usuário e exiba a raiz quadrada de cada número

import math

for cont in range(15):
    numero = int(input("\nDigite um número: "))
    t = math.sqrt(numero)
    print(t)