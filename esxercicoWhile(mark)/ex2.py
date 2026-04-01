
usuario_correto = "admin"
senha_correta = "1234"
tentativas = 1


usuario = input("Digite o nome de usuário (ou 0 para sair): ")

while usuario != "0": 
    senha = input("digite a senha: ")
    if usuario == usuario_correto and senha == senha_correta:
        print ("Acesso permitido")
        print("acertou com" ,tentativas, "tentativas")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente./n.")
        print("ja errou com" ,tentativas, "tentativas"  )

    tentativas += 1    
    usuario = input("Digite o nome de usuário (ou 0 para sair): ")