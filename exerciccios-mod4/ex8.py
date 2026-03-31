diarias = int(input("Digite a quantidade de diárias: "))

volor_diaria = 500
tx = 0
#volor_pagar = ((diarias * volor_diaria) + (tx * diarias))

if diarias < 15:
    tx = 15
elif diarias == 15:
    tx = 10
else:
    tx = 5

volor_pagar = ((diarias * volor_diaria) + (tx * diarias))


print(f" Para uma estadia de {diarias} dias, O valor total a pagar é: R$ {volor_pagar:.2f}")