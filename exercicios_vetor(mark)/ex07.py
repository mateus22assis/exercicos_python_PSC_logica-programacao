''' Faça um programa que solicite ao usuário que digite o número do mês do ano, e que imprima o nome do mês correspondente. O programa não poderá utilizar a estrutura condicional IF.'''

# Lista de meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Função para validar a entrada entre 1 e 12
def ler_numero_mes(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            if 1 <= num <= 12:
                return num
            print("Erro: O número deve estar entre 1 e 12.")
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

# Solicita ao usuário que digite o número do mês
numero_mes = ler_numero_mes("Digite o número do mês (1-12): ")

# Imprime o nome do mês correspondente
print("Nome do mês:", meses[numero_mes - 1])