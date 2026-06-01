lista = [1, 2, 3, 4]
lista.append(50)
print(lista)

numero = int(input('Digite um número: '))
lista.append(numero)
lista.insert(0, numero)
print(lista)
lista.pop()

lista.pop(2)
print(lista)

while 10 in lista:
    lista.remove(10)
print(lista)
