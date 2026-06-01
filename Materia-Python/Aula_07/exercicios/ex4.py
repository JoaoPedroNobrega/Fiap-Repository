vogal = ["a","e","i","o","u"]
consoante = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

letra = input("Digite uma letra minúscula: ")

if letra in vogal:
    print(f"{letra} é uma Vogal")
elif letra in consoante:
    print(f"{letra} é uma Consoante")
else:
    print("Opção Inválida")