horas = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))

if 23 >= horas and 59 >= minutos:
    print(f"A hora é válida {horas}:{minutos}")
elif 23 < horas and 59 >= minutos:
    print(f"O minuto é válido ({minutos}), mas a hora é inválida ({horas})")
elif 23 >= horas and 59 < minutos:
    print(f"A hora é válida ({horas}), mas os minutos é inválido ({minutos})")
elif 23 < horas and 59 < minutos:
    print("Tá tudo errado!")