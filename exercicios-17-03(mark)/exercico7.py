#calculo de nivel do jogador
#  ENTRADA 
pontuacao = int(input("Digite a pontuação do jogador: "))

#  REGRAS 
nivel = ""
bonus = ""
mensagem_extra = ""

if pontuacao == 0:
    mensagem_extra = "Tente novamente!"

if pontuacao < 1000:
    nivel = "Iniciante"
elif pontuacao <= 4999:
    nivel = "Intermediário"
elif pontuacao <= 9999:
    nivel = "Avançado"
else:
    nivel = "Mestre"

if pontuacao >= 8000:
    bonus = "Parabéns! Você ganhou um bônus especial!"

#  SAIDA 
print(f"Nível do jogador: {nivel}")

if bonus != "":
    print(bonus)

if mensagem_extra != "":
    print(mensagem_extra)
    