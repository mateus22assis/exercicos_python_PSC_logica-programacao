#um numero interio que retorna o seu fatorial

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

fatorial_numero = fatorial(3)
print("fatorial:", fatorial_numero)