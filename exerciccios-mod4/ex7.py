import math

N1 = float(input("digite o primeiro número: "))
N2 = float(input("digite o segundo número: "))

print("Escolha uma opção:")
print("1 - Somar os dois números")
print("2 - Multiplicar os dois números")
print("3 - Subtrair o número maior pelo número menor")
print("4 - Dividir o primeiro número pelo segundo")

opcao = int(input("digite a opção desejada: "))

if opcao == 1:
    resultado = N1 + N2
    print("O resultado da soma é:", resultado)
elif opcao == 2:
    resultado = N1 * N2
    print("O resultado da multiplicação é:", resultado)
elif opcao == 3:
    if N1 > N2:
        resultado = N1 - N2
    elif N2 > N1:
        resultado = N2 - N1
    else:
        resultado = 0
    print("O resultado da subtração é:", resultado)
elif opcao == 4:
    if N2 == 0:
        print("Erro: divisão por zero")
    else:        resultado = N1 / N2
    print("O resultado da divisão é:", resultado)
else:
    print("Opção inválida")




