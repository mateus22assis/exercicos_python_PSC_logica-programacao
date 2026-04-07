#Um número inteiro e que retorne True se o número for par, e False caso contrário

def par(numero):
    if numero % 2 == 0:
        return True
    return False

valor = int(input("Digite um número inteiro: "))
if par(valor):
    print("True")
else:
    print("False")