lista = []
lista_soma = []
soma = 0
media_somatoria = 0
for cont in range(10):
    numero = int(input("Numero: "))
    lista.append(numero)
    media_somatoria += numero
    if numero % 2 == 0:
        lista_soma.append(numero)
        soma += numero
    media = media_somatoria/10

print(f"Média: {media}")
print(f"Soma dos número pares: {soma}")