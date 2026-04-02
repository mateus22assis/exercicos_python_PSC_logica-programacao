''' a prefeitura fez uma pesquisa entre os habitantes de uma cidade, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:
a) A média do salário dos habitantes;  
b) A média do número de filhos;
 o final da leitura dos dados é indicado por um salário negativo.'''

salario = float(input("Digite o salário do habitante (ou negativo para sair): "))
respostas = 0

soma_salarios = 0
soma_filhos = 0

while salario >= 0:
    numero_filhos = int(input("Digite o número de filhos do habitante: "))
    soma_salarios += salario
    soma_filhos += numero_filhos
    respostas += 1
    salario = float(input("Digite o salário do habitante (ou negativo para sair): "))

if respostas > 0:
    media_salarios = soma_salarios / respostas
    media_filhos = soma_filhos / respostas
    print(f"A média do salário dos habitantes é: {media_salarios:.2f}")
    print(f"A média do número de filhos dos habitantes é: {media_filhos:.2f}")
   
else:
    print("salario negativo foi digitado. Nenhum dado foi coletado.")