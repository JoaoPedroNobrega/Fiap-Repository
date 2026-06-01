numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro outro número: '))

if numero1 == numero2 == numero3:
    print("São todos iguais")
elif numero1 < numero2 and numero1 < numero3:
    print(f"{numero1} é o menor número")
elif numero2 < numero1 and numero2 < numero3:
    print(f"{numero2} é o menor número")
elif numero3 < numero1 and numero3 < numero2:
    print(f"{numero3} é o menor número")

print("Fim do código!")