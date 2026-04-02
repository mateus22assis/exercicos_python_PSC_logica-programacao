#programa que recebe a idade e o sexo de 10 pessoas e calcula a média de idade do grupo e o número de mulheres com idade entre 20 e 40 anos usando um loop for
contadorMulheres_20a40 = 0
soma_idade = 0
qtde_pessoas = 0
for i in range(10):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (m/f): ").upper()
    soma_idade += idade
    qtde_pessoas += 1
    if sexo == "F" and idade >= 20 and idade <= 40:
        contadorMulheres_20a40 += 1

media_idade = soma_idade / qtde_pessoas

print("A média de idade do grupo é: ", media_idade)
print("O número de mulheres com idade entre 20 e 40 anos é: ", contadorMulheres_20a40)