#dois numeros interios que retorna a multiplicaçao do primeiro pelo segundo ultilizando somente a adição
def multiplicacao(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado


resultado = multiplicacao(5, 3)
print("o primeiro numero multiplicado pelo segundo é:", resultado)

