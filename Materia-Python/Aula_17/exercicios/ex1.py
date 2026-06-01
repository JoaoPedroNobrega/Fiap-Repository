import random

lista = []

for i in range(10):
    numero_aleatorio = random.randint(1, 20)
    lista.append(numero_aleatorio)
    verificar = lista.count(numero_aleatorio)
    if verificar > 1:
        lista.clear()
        numero_aleatorio = random.randint(1, 20)
        lista.append(numero_aleatorio)

print(lista)