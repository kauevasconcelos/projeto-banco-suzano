# For - Serve para que eu possa repetir algo por uma quantidade de vezes que eu determinar. 
# Ex: repetir 5 vezes.
# 🧠 Como funciona?
# Você fornece uma sequência de valores e o for percorre essa sequência, um por um.

# for i in range(5):
#     print(i)



# While - Serve para repetir algo por uma quantidade de vezes indeterminada, até que a condição seja
# saciada.

# contador = 0

# while contador < 10:
#     contador += 1
#     print(contador)

n_secreto = 6
print("Estou pensando em um número de 0 a 10. Tente adivinhar")
while True:
    digite = int(input("Digite um número: "))

    if digite > n_secreto:
        print('Um pouco menos   que isso.')
        
    elif digite < n_secreto:
        print("Um pouco mais que isso!")
    elif digite == n_secreto:
        print(f"Correto! O número que eu pensei era {n_secreto}")
        break
      


        
