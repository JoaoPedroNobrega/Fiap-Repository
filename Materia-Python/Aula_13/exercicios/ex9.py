# Solicite a quantidade de alunos de uma turma
# e a quantidade de notas. Para cada aluno, solicite as
# suas notas e exiba a sua respectiva média

alunos = int(input("Digite a quantidade de alunos da sala: "))
notas = int(input("Digite a quantidade de notas: "))

media = 0

for cont in range(alunos):
    for cont2 in range(notas):
        nota = float(input("Digite a nota:"))
        media += nota
    print(f"Média do aluno {media/notas}")
    media = 0
print("Fim do programa")