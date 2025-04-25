MAIOR_IDADE = 18

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar a sua CNH!")
else:
    print("Você ainda não pode tirar sua primeira CNH!")

# -----------------------------------------------

ano = int(input("Digite o ano: "))

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')