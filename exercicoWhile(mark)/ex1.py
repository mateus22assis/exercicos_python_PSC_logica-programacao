# Simulador de caixa eletrônico usando estrutura de repetição while
saldo = 1000
opçao = 0  

while opçao != 4: 
    print("\n--- Menu ---")
    print("1 -> Ver saldo")
    print("2 -> Sacar")
    print("3 -> Depositar")
    print("4 -> Sair")
    opçao = int(input("Digite a opção desejada: "))

    if opçao == 4:
        print("Saindo do caixa eletrônico. Obrigado!")
    elif opçao == 1:
        print(f"Seu saldo é: R$ {saldo:.2f}") 
    elif opçao == 2:
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque > saldo:
            print("Saldo insuficiente para saque.")
        else:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso.")
    elif opçao == 3:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito <= 0:
            print("Valor de depósito deve ser positivo.")
        else:
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso. ")
    else:
        print("Opção inválida, tente novamente.")
    