import math

menor = math.inf        # Infinito positivo
maior = -math.inf       # Infinito negativo

for cont in range(10):
    numero = int(input("Numero: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Menor: {menor}")
print(f"Maior: {maior}")