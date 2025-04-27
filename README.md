# Funções 💬  

Uma função também pode ser chamada de bloco de código. Ele serve para me retornar um bloco de código que eu defini anteriormente.

Ele ajuda a organizar o código, reutilizá-lo e deixar o programa mais legível. Ex:

    def ola_mundo():
        print("Olá mundo")
Depois eu posso chamar esse função digitando: ola_mundo():

### Funções com parâmetros 📄

Serve para eu colocar variáveis dentro das funções e depois dar valor pra essas variáveis. Ex:

    def ola_nome(nome):
        print(f'Olá, {nome}')

    ola_nome("Kauê")
    ola_nome("Cecília")


### Funções para retornar valores ↪↩

Às vezes queremos que nossas funções calculem algo e depois retornem o resultado. Nesse caso usamos o "return"

    def soma(a, b):
        return a + b

    resultado = soma(5, 3)
    print(resultado)               #retorna 8
