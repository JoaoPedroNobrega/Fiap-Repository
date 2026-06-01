lista = [12, 19, 3, 3, 67, 19, 38]
qt = 0

adivinhar = int(input("Digite um número: "))

while True:
    for item in lista:
        if adivinhar == item:
            qt += 1

    if qt == 0:
        print(f"{adivinhar} aparece nenhuma vez na lista")
        adivinhar = int(input("Digite um número: "))
    elif qt == 1:
        print(f"{adivinhar} aparece uma vez na lista!")
        adivinhar = int(input("Digite um número: "))
    elif qt >= 2:
        print(f"{adivinhar} aparece {qt} vezes na lista!")
        adivinhar = int(input("Digite um número: "))