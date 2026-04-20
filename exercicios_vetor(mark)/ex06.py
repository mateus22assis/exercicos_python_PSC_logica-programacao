'''6. Faça um programa que solicite ao usuário que informe inicialmente os 6 números sorteados na Mega Sena. Em seguida, peça que ele digite os 6 números do cartão que jogou. Imprima a quantidade de pontos que ele fez no concurso.'''

# Função para validar a entrada entre 1 e 60
def ler_numero_mega(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            if 1 <= num <= 60:
                return num
            print("Erro: O número deve estar entre 1 e 60.")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

print("--- Sorteio da Mega Sena ---")
sorteados = [ler_numero_mega(f"Digite o {i+1}º número sorteado: ") for i in range(6)]

print("\n--- Seu Cartão ---")
jogados = [ler_numero_mega(f"Digite o {i+1}º número do cartão: ") for i in range(6)]

# Usando interseção de conjuntos (&) para contar os acertos de forma "automática"
pontos = len(set(sorteados) & set(jogados))
print(f"Quantidade de pontos: {pontos}")
