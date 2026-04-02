#programa que recebe um número do usuário e calcula a soma dos números de 1 até esse número usando um loop for
numero = int(input("Digite um número: "))
soma = 0
for i in range(1, numero + 1):
    soma += i
print(f"A soma dos números de 1 a {numero} é: {soma}")