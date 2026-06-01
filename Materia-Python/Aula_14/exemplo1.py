# Solicite um número inteiro N e imprima um quadrado de N*N asteriscos.
# Exemplo para N = 4:
# ****
# ****
# ****
# ****

n = int(input('Digite um número: '))
for cont in range(n):
    print("*" * n)