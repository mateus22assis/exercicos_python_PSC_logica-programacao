cont_idade30_40 = 0
soma = 0
qtde_pessoas = 0
idade = int(input("Digite uma idade: "))
while idade >= 0:
  qtde_pessoas += 1
  soma += idade
  if idade >= 20 and idade <= 40:
    cont_idade += 1
  idade = int(input("Digite uma idade: "))

print("exite(m)", cont_idade, "pessoa(s) entre 20 e 40 anos")
media = soma / qtde_pessoas

print("soma: ", soma)
print("qtde: ", qtde_pessoas)
print("media: ", media)
print("exite(m)", cont_idade, "pessoa(s) entre 20 e 40 anos")