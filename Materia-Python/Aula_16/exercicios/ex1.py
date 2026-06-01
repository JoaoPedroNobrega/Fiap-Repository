lista_pares = []
lista_impares = []
for cont in range(10):
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        lista_pares.append(numero)
    elif numero % 2 != 0:
        lista_impares.append(numero)
print(f"Números pares: {lista_pares}")
print(f"Números ímpares: {lista_impares}")