lista_nome = []
lista_idade = []
lista_dmaior = []

for cont in range(10):
    nome = (input("Digite um nome: "))
    idade = int(input(f"Digite a idade do {nome}: "))
    lista_nome.append(nome)
    lista_idade.append(idade)
    if idade >= 18:
        lista_dmaior.append(nome)

print(f"Maiores de idade: {lista_dmaior}")