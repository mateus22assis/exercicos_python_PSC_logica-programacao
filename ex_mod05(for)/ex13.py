#programa que recebe dois números do usuário e calcula a potência do primeiro número elevado ao segundo número usando apenas multiplicação e um loop for
base = int(input("Digite a base (primeiro número): "))
expoente = int(input("Digite o expoente (segundo número, não-negativo): "))

resultado = 1

if expoente < 0:
    print("Para calcular a potência usando apenas multiplicação, o expoente deve ser não-negativo.")
elif expoente == 0:
    
    print(f"{base} elevado a {expoente} é: 1")
else:
    for _ in range(expoente):
        resultado *= base
    print(f"{base} elevado a {expoente} é: {resultado}")