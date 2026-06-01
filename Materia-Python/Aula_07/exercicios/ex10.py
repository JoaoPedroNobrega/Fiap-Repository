salario = int(input('Digite o salário fixo: '))
vendas = int(input('Digite o valor das vendas: '))

if vendas > 1500:
    p5 = vendas - 1500
    p3 = 1500 * 0.03
    vendas = (p5 * 0.05)+p3

    total = vendas + salario

else:
    total = (vendas * 0.03) + salario

print(total)

