#dois numeros interios que retorna a multiplicaçao do primeiro pelo segundo ultilizando somente a adição
def multiplicacao(primeiro, segundo):
    resultado = 0
    for i in range(segundo):
        resultado += primeiro
    return resultado


resultado = multiplicacao(5, 3)
print("o primeiro numero multiplicado pelo segundo é:", resultado)

