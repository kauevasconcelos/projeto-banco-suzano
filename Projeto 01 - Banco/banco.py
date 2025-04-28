#Código de desenvolvimento do exercício proposto

#Regras 
qtd_saque = 3
saldo = 1000
extrato = []
LIMITE_DE_SAQUE = 500
QTD_MAX_DE_SAQUE = 3

# Escolha do usuário

print("Qual operação deseja realizar?")
print("Saque: Digite [s]")
print("Depósito: Digite [d]")
print("Extrato: Digite [e]")
print("Sair: Digite [q]")

#Lógica das operações

while True:
    
    escolha = input('Escolha a operação: ')

    if escolha == "s": #Usuário escolheu fazer saque
        print(f"Você tem {saldo} reais e pode fazer {qtd_saque} saques")
        saque = float(input("Quanto quer sacar? "))
        
        if saque > LIMITE_DE_SAQUE: # Limite de saque
            print('Você não pode sacar mais de 500 reais de uma vez') 
        elif saque > saldo: # Saldo insuficiente
            print("Você não tem saldo suficiente para fazer o saque!") 
        elif saque < 0: # Valores negativos
            print("Você não pode sacar valores negativos!")
        elif qtd_saque == 0:
            print("Você não pode mais fazer saques hoje! Volte amanhã. ")
        else:
            print("Saque realizado com sucesso")
            saldo -= saque
            qtd_saque -= 1
            print(f"Seu saldo atual é de {saldo} e você ainda pode fazer {qtd_saque} saques")
            extrato.append(f"Saque no valor de {saque}")
            
    elif escolha == "d": #Usuário escolheu fazer depósito
        print(f"Você possui {saldo} reais de saldo")
        deposito = float(input("Quanto quer depositar? "))

        if deposito <= 0:
            print("Você não pode depositar um valor negativo ou zero!")
        else:
            saldo += deposito
            print(f"Depósito realizado com sucesso! Seu saldo atual é de {saldo} reais!")
            extrato.append(f"Depósito de {deposito}")

    elif escolha == "e": #Usuário escolheu consultar seu extrato
        print("========EXTRATO========")
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print("Não houve movimentações")

    elif escolha == "q": #Usuário escolheu sair
        print("Saindo...")
        break

    else: #Usuário digitou um valor desconhecido
        print("Não entendi. Digite novamente")    
