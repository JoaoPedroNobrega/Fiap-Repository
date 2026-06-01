nome = input("Nome do vendedor: ")
carrosVendidos = float(input("Quantidade de carros vendidos: "))
totalVendas = float(input("Valor total das vendas: "))

comissaoCarro = 200 * carrosVendidos
acrescimoValorTotal = totalVendas * 0.02

salario = 2500 + comissaoCarro + acrescimoValorTotal

print(f"O vendedor {nome} receberá um salário de R${salario}")