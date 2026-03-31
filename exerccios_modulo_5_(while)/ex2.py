import math
numero = int(input("Digite um número: "))
while numero >= 0:
    print("valor lido: ", numero)
    print("quadrado: ", numero ** 2)
    print("cubo: ", numero ** 3)
    print(f"raiz quadrada: {math.hypot(numero) :.2f}" )
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")
    numero = int(input("Digite um número: "))