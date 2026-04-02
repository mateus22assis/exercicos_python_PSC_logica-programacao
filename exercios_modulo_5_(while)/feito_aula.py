#programa de gerenciamento das idades de um grupo de pessoas, onde o usuário digita as idades e o programa deve calcular a soma, a quantidade de pessoas, a média, a quantidade de pessoas entre 20 e 40 anos, a menor idade e a maior idade. O programa deve continuar solicitando as idades até que o usuário digite um número negativo.
cont_idade20_40 = 0
soma = 0
qtde_pessoas = 0
idade = int(input("Digite uma idade: "))
menor = idade
maior = idade
while idade >= 0:
  qtde_pessoas += 1
  soma += idade

  if idade < menor:
    menor = idade

  if idade > maior:
    maior = idade

  if idade >= 20 and idade <= 40:
    cont_idade20_40 += 1
  idade = int(input("Digite uma idade: "))

if (qtde_pessoas == 0):
  print("Nenhuma idade valida digitada")
else:
  media = soma / qtde_pessoas

  print("soma: ", soma)
  print("qtde: ", qtde_pessoas)
  print("media: ", media)
  print("exite(m)", cont_idade20_40, "pessoa(s) entre 20 e 40 anos")
  print("menor idade: ", menor)
  print("maior idade: ", maior)