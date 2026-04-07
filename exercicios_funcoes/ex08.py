#dois numeros interios que retorne a potencia do primeiro elevado ao segundo ultilizando somente multiplicaçao

def potenciacao(num1, num2):
    resultado = 1
    for i in range(num2):
        resultado *= num1
    return resultado

resultado = potenciacao(2, 3)
print("o primeiro numero elevado ao segundo é:", resultado)


