'''Crie um dicionário e armazene o nome e e-mail de 5 pessoas informados por você. Em seguida, solicite ao usuário que informe um nome. Imprima o e-mail da pessoa informada, caso exista no dicionário. Caso não exista, emita uma mensagem.
Utilize a mesma estratégia para um e-mail informado pelo usuário. 
'''

dicionario_emails = {
    'João': 'joao@email.com',
    'Maria': 'maria@email.com',
    'Pedro': 'pedro@email.com',
    'Ana': 'ana@email.com',
    'Carlos': 'carlos@email.com'
}

nome = input('Informe um nome: ')

if nome in dicionario_emails:
    print(f'O e-mail da pessoa {nome} é {dicionario_emails[nome]}')
else:   print(f'O nome {nome} não existe no dicionário.')

email = input('Informe um e-mail: ')

if email in dicionario_emails.values():
    print(f'O e-mail {email} existe no dicionário.')
else:   print(f'O e-mail {email} não existe no dicionário.')