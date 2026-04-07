#um numero interio que retorna a soma dos numeros pares de 1 ate o numero(inclusive)


def soma_numeros(numero):
    soma = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            soma += i
    return soma

soma_numero = soma_numeros(5)
print("soma:", soma_numero)