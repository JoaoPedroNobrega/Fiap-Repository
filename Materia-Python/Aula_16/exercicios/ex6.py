lista = []
nota = 0
quantidade_notas = 0
soma_notas = 0
media = 0
acima_media = 0
quantidade_notas_acima_media = 0

while True:
    nota = int(input("Digite uma nota: "))
    if nota >= 0:
        lista.append(nota)
        quantidade_notas += 1
        soma_notas += nota
    print(f"Nota {nota} adicionada!")
    if nota < 0:
        print(f"Quantidade de notas informadas: {quantidade_notas}")
        print(lista)
        media = soma_notas/quantidade_notas
        print(f"Média aritmética {media:.2f}")
        for item in lista:
            if item >= media:
                quantidade_notas_acima_media += 1
        print(f"Quantidade de notas acima da média {quantidade_notas_acima_media}")
        break