# Um funcionário foi contratado em 2015 com um salário inicial de R$ 2.000,00. Em 2016 e nos anos
# seguintes ele passou a receber um aumento anual de 1,5% sobre o salário do ano anterior.
# Desenvolva um algoritmo que determine e exiba o salário deste funcionário no ano de 2026.

aumento = 0.015
salario = 2000
soma = 0

for i in range(2015, 2026):
    salario += (salario * aumento)

print(round(salario))