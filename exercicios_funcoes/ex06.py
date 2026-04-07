#um numero interio positivo que retorna a soma dos numeros de 1 ate o numero(inclusive)

def soma_numeros(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

soma_numero = soma_numeros(5)
print("soma:", soma_numero)