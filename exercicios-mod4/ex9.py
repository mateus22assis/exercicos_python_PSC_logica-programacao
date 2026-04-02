#mensalidade de uma academia, onde o valor varia de acordo com a idade e o sexo do cliente:
Idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (M/F): ").upper() 

if sexo == 'M':
    if Idade <= 15:
        mensalidade = 60.00
    elif Idade <= 18:
        mensalidade = 75.00
    elif Idade <= 30:
        mensalidade = 90.00
    elif Idade <= 40:
        mensalidade = 85.00
    else:
        mensalidade = 80.00
elif sexo == 'F':
    if Idade <= 18:
        mensalidade = 60.00
    elif Idade <= 25:
        mensalidade = 90.00
    elif Idade <= 40:
        mensalidade = 85.00
    else:
        mensalidade = 80.00
else:
    print("Sexo inválido")

print(f"A mensalidade a ser paga é: R$ {mensalidade:.2f}")  

