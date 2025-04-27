"""O fatiamento de strings é usado quando eu quero pegar só um trecho da minha string, por quanlquer
motivo que seja. Isso será feito utilizando índices.
    Cada string tem um índice, que começa de 0 e vai até a quantidade de caracteres da string.
    Ex: casa vai de 0 a 3. Para eu usar só o último caractere eu utilizo: casa[3]
        0123
"""

#              1 DESAFIO  com a palavra "Aprendizado"

# 1. Mostre só as 5 primeiras letras
# 2. Mostre as letras do meio (índices 4 até 8)
# 3. Mostre a palavra ao contrário
# 4. Mostre só as letras em posição par (pule de 2 em 2)

# palavra = "Aprendizado"

# print(palavra[0:6])
# print(palavra[4:9])
# print(palavra[::-1])
# print(palavra[::2])

#                          2 DESAFIO DA SENHA
#               Crie uma senha secreta a partir do nome do usuário

# 1. Pegue os 3 primeiros caracteres do nome
# 2. Pegue os 2 últimos caracteres
# 3. Crie a senha unindo os pedaços + '123'
# Exemplo: Se o nome for "Kauê", a senha seria "Kauêê123"

# nome = input("Digite seu nome: ")

# inicio = nome[0:3]
# cont = len(nome)
# ultimo = nome[cont-1] * 2
# senha = inicio + ultimo + "123"
# print(senha)


#                   Desafio 3 – Cortando e Reorganizando
"""
Peça para o usuário digitar uma palavra e faça:
Pegue da 2ª letra até a penúltima.
Inverta esse pedaço.
Mostre o resultado final.
"""

# palavra = input("Digite uma palavra: ")

# fatiamento = palavra[1: len(palavra) - 1:]
# print(fatiamento[::-1])

#                   Desafio 4 - Iniciais do nome

#Peça para o usuário digitar nome completo e pegue as iniciais para criar um "apelido".

nome = input("Digite seu nome completo: ")

corte = nome.split()
print(corte[0:1])
print(len(corte))

iniciais = ""
for palavra in corte:
    iniciais += palavra[0]
    print(iniciais)