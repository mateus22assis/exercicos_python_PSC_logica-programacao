#o ano de nascimento de uma pessoa e um ano base que retorna a idade da pessoa  no ano base

def idade(ano_nascimento, ano_base):
    return ano_base - ano_nascimento 

idade_ano_base = idade(1990, 2020)
print("idade:", idade_ano_base)


