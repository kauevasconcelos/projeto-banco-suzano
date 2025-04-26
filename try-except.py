#   Arquivo criado para deixar meus exercícios sobre try e except
#   Essas funções são usada para evitar que o código pare devido algum erro do usuário.
#   Nesse caso ele tenta (try) executar uma ação e, caso ele não consiga (except), ele continua rodando
#o código




# while True:
#     digite = input("Digite um número: ")
#     try:
#         digite = int(digite)
#         print("Você digitou um número!")
#         break
#     except:
#         print("Erro! Tente digitar um número dessa vez! ")

###
#               DESAFIO:
#O programa vai pensar em um número de 0 a 10.
#O usuário precisa tentar adivinhar o número correto.
#Se ele digitar algo que não seja número, o programa deve avisar e pedir novamente, sem travar.
#Quando acertar, exiba uma mensagem de parabéns e termine o jogo.
# ####

import random
n_secreto = random.randint(0, 10)

print("Desafio: Tente adivinhar o número de 0 a 10 que estou pensando")

while True:
    digite = input("Digite um número: ")
    try:
        digite = int(digite)
        if digite > 10 or digite < 0:
            print("O número está entre 0 e 10! Tente novamente")
        elif digite > n_secreto:
            print("Um pouco menos. Tente novamente!")
        elif digite < n_secreto:
            print('Um pouco mais. Tente novamente')
        elif digite == n_secreto:
            print(f"Parabéns! O número secreto é {n_secreto}")
            break
    except:
        print("Erro! Você não digitou um número!")