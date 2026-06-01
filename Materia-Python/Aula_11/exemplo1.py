# Validação de etrada do usuário
# Solicitar a nota do (aluno 0-10)


nota = float(input('Informe sua nota: '))
while nota < 0 or nota > 10:
    nota = float(input('Nota inválida. Digite novamente'))

    print(f' a nota informada foi {nota}')