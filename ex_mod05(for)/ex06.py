num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

for i in range(menor, maior + 1):
    print(i)