''' Exercício 4: Controle de estoque
Simule um estoque de produto:
Quantidade inicial: 50 
Menu: 
1 → Vender 
2 → Repor 
3 → Ver estoque 
4 → Sair 
Regras:
Não vender mais do que tem 
Alertar se estoque < 10 
'''
estoque_inicial = 50
opcao = 0

while opcao != 4:
    print("\n--- Menu ---")
    print("1 -> Vender")
    print("2 -> Repor")
    print("3 -> Ver estoque")
    print("4 -> Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 4:
        print("Saindo do controle de estoque. Obrigado!")
    elif opcao == 1:
        quantidade_venda = int(input("Digite a quantidade a ser vendida: "))
        if quantidade_venda > estoque_inicial:
            print("Não é possível vender mais do que o estoque disponível.")
        else:
            estoque_inicial -= quantidade_venda
            print(f"Venda realizada com sucesso.")
            if estoque_inicial < 10:
                print(f"Alerta: Estoque baixo! Restam apenas {estoque_inicial} unidades.")
    elif opcao == 2:
        quantidade_reposicao = int(input("Digite a quantidade a ser reposta: "))
        if quantidade_reposicao <= 0:
            print("Quantidade de reposição deve ser positiva.")
        else:
            estoque_inicial += quantidade_reposicao
            print(f"Reposição realizada com sucesso.")
    elif opcao == 3:
        print(f"Estoque atual: {estoque_inicial} unidades.")
    else:
        print("Opção inválida, tente novamente.")
