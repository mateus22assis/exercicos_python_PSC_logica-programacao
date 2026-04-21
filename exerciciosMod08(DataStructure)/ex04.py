'''Crie um código Python que solicite ao usuário que informe  o código de uma moeda (vide os códigos possíveis em https://economia.awesomeapi.com.br/xml/available/uniq). Utilizando a API AwsomeAPI (https://docs.awesomeapi.com.br/api-de-moedas), obtenha as informações sobre a cotação e imprima o nome da moeda (name), e em seguida as cotações de venda (bid) e compra (ask) da moeda em Reais.'''


import requests

codigo_moeda = input('Informe o código da moeda (ex: USD, EUR): ').upper()

resposta = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')

informacoes_moeda = resposta.json()
print(informacoes_moeda[f'{codigo_moeda}BRL']['name'])
print(informacoes_moeda[f'{codigo_moeda}BRL']['bid'])
print(informacoes_moeda[f'{codigo_moeda}BRL']['ask'])

