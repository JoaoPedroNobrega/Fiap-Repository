def calcularArea(circulo):
	area = 3.14 * (circulo * circulo)
	return area

def calcularPerimetro(circulo):
	perimetro = 3.14 * (2 * circulo)
	return perimetro

num = int(input('Digite o número do raio do círculo: '))
calculo_area = calcularArea(num)
calculo_perimetro = calcularPerimetro(num)

print(f'O valor da área do círculo é {calculo_area} e o perímetro é {calculo_perimetro}')
