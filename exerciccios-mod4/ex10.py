diarias = float(input("Digite a quantidade de diárias: "))
tipo_apto = input("Digite o tipo de apartamento (Simples ou duplo): ")

if tipo_apto.lower() == "simples":
    if diarias < 10:
        valor_diaria = 100
    elif diarias <= 15:
        valor_diaria = 90
    else:
        valor_diaria = 80   
elif tipo_apto.lower() == "duplo":
    if diarias < 10:
        valor_diaria = 140
    elif diarias <= 15:
        valor_diaria = 120
    else:
        valor_diaria = 100

valor_total = diarias * valor_diaria
print(f"O valor total a pagar é: R$ {valor_total:.2f}") 