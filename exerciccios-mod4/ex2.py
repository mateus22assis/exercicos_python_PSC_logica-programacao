N1 = int(input("Digite a primeira nota: "))
N2 = int(input("Digite a segunda nota: "))
N3 = int(input("Digite a terceira nota: "))

media = (N1 + N2 + N3) / 3
print("A média é: ", media)

if media >= 7:
    print("Aprovado")   
elif media >= 3:
    print("exame")
else:
    print("Reprovado")  