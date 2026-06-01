def calcular_dobro (numero):
	dobro = numero * 2
	return dobro
	
n = int(input('Digite um número: '))
d = calcular_dobro(n)
print(f'O dobro de {n} é {d}')