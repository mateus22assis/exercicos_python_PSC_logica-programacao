#Um número inteiro e que retorne True se o número for primo, e False caso contrário
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

valor = int(input("Digite um número inteiro: "))
if primo(valor):
    print("True")
else:
    print("False")
