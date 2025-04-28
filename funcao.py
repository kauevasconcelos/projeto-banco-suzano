#códigos para praticar funções

# def par_impar(numero):
#     if numero % 2 == 0:
#         return f"{numero} é par!"
#     else:
#         return f"{numero} é impar"
    
# digite = int(input("Digite o número: "))
# print(par_impar(digite))


"""

def cadastrar_usuario(nome, cidade, email):
    print(f'Nome é {nome}')
    print(f'Cidade é {cidade}')
    print(f'Email é {email}')

cad = cadastrar_usuario(nome = "Cecília", cidade = "Altinho", email = "cecilia@teste.teste")
print(cad)

"""


"""Desafio: Cadastro de Aluno
Crie uma função chamada cadastrar_aluno que receba 4 informações:

nome (str)
idade (int)
curso (str)
matricula (int)

Dentro da função, ela deve apenas imprimir:

O nome do aluno
A idade
O curso
O número de matrícula"""


""" CÓDIGO

def cadastro(nome, idade, curso, matricula):
    print(f'Nome é {nome}')
    print(f'Idade é {idade}')
    print(f'Curso é {curso}')
    print(f'Matrícula é {matricula}')

cadastro(nome = "Cecília", idade = 18, curso = "Mecatrônica", matricula = "2022G6CR2218")
"""


# DESAFIO COM ARGS E KWARGS

"""

Crie uma função chamada lista_compras que aceite:

Quantos produtos você quiser (usando *args).
Informações extras como forma de pagamento, valor total, etc. (usando **kwargs).

Dentro da função, você deve:

Mostrar a lista de produtos (um por linha).
Mostrar também as informações extras de forma bonitinha."""

def lista_compras(*produtos, **info_extra):
    coisas = ""
    for coisas in produtos:
        print(coisas)

    for extra in info_extra:
        print(extra)

    
lista_compras("Arroz", "Feijão", "Macarrão", pagamento="Cartão", total="R$ 45,00")

