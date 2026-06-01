nome = input("Digite o nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
faltas = int(input("Quantidade de faltas: "))

media = (nota1 + nota2)/2

if media >= 6 and faltas < 20:
    print(f"O aluno {nome} aprovado")
    print(f"Média: {media}")
    print(f"Faltas: {faltas}")
elif media >= 6 and faltas >= 20:
    print(f"O aluno {nome} reprovado por faltas")
    print(f"Média: {media}")
    print(f"Faltas: {faltas}")
elif media < 6 and faltas < 20:
    print(f"O aluno {nome} reprovado por média")
    print(f"Média: {media}")
    print(f"Faltas: {faltas}")
else:
    print(f"O aluno {nome} reprovado por média e por faltas")
    print(f"Média: {media}")
    print(f"Faltas: {faltas}")