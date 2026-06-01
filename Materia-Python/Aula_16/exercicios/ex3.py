import math
import random

menor = math.inf        # Infinito positivo
maior = -math.inf       # Infinito negativo
soma_lista = 0

numero = []
for i in range(0,19):
    aux = random.randint(1,50)
    numero.append(aux)
    soma_lista += aux
    if aux > maior:
        maior = aux
    if aux < menor:
        menor = aux


print(numero)
print(soma_lista)
print(f"Menor: {menor}")
print(f"Maior: {maior}")