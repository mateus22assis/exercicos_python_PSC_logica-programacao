#calculo da media de notas
N1 = int(input("Digite a primeira nota: "))
N2 = int(input("Digite a segunda nota: "))

media = (N1 + N2) / 2

print("A média é: ", media)

if media >= 7:
    print("Aprovado")   

else:
    print("Reprovado")  