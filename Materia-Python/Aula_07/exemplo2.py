nome = input("Digite o nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
faltas = int(input("Quantidade de faltas: "))

media = (nota1+nota2)/2

if media >= 6:
    if faltas <20:
        print(f"O aluno {nome} está aprovado com: {media} e {faltas} faltas.")
    else:
        print(f"O aluno {nome} está aprovado com: {media}, mas reprovado por excesso de faltas.")
else:
    if faltas > 20:
        print(f"O aluno {nome} está reprovado com: {media} e excesso de faltas.")
    else:
        print(f"O aluno {nome} está reprovado com: {media}, mesmo com apenas {faltas} faltas.")

print("Final da execução.")