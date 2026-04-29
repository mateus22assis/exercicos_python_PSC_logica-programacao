'''3. Sistema de Cadastro de Produtos
Crie vetores paralelos para armazenar 5 produtos:
Nome do produto 
Preço 
Implemente métodos para:
Cadastrar produtos 
Verificar o preço que pago ao comprar 3 produtos diferentes  
'''
nomes = [""] * 5
precos = [0.0] * 5

def cadastrar_produtos(nnomes, precos, n):
    for i in range(n):
        nomes[i] = input(f"Digite o nome do produto {i+1}: ")
        precos[i] = float(input(f"Digite o preço do produto {i+1}: "))  

def exibir_produtos(nomes, precos, n):
    print("\nprodutos disponiveis:")
    for i in range(n):
        print(f"{nomes[i]} - R${precos[i]:.2f}")

def buscar_produto(nomes, n, nome_busca):
    for i in range(n):
        if nomes[i].lower() == nome_busca.lower():
            return i
    return -1


def calcular_preco_total(nomes, precos, n):
    total = 0.0
    print("\ndigite 3 produtos pelo nome")
    for i in range(3):
        nome = input(f"Digite o nome do produto {i+1}: ")
        pos = buscar_produto(nomes, nome, n)

        if pos == -1:
            print("Produto não encontrado.")
        else:
            total += precos[pos]

    return total


    




# Programa principal
n = 5
cadastrar_produtos(nomes, precos, n)
exibir_produtos(nomes, precos, n)

total = calcular_preco_total(nomes, precos, n)
print(f"Total a pagar: R${total:.2f}")