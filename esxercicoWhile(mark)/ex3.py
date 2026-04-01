
numero_secreto = 15
tentativas = 1
chute = int(input("Adivinhe o número secreto (entre 1 e 20): "))

while chute != numero_secreto:
    if chute < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")
    tentativas += 1
    chute = int(input("Tente novamente: "))

print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")