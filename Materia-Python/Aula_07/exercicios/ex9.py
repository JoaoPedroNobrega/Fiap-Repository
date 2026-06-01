lado1 = int(input('Digite o tamanho do lado 1: '))
lado2 = int(input('Digite o tamanho do lado 2: '))
lado3 = int(input('Digite o tamanho do lado 3: '))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print("O triângulo é isósceles!")
elif lado1 != lado2 != lado3:
    print("O triângulo é escaleno!")
else:
    print("O seu triângulo é bizarro!")