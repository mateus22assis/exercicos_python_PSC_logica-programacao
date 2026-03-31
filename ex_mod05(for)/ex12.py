numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

if numero < 0:
    print("Fatorial não é definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é: {fatorial}")