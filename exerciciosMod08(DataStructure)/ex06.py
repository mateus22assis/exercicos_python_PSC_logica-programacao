'''7) Solicite ao usuário que informe o código de uma moeda (vide os códigos possíveis em https://economia.awesomeapi.com.br/xml/available/uniq). Solicite também que informe uma quantidade de cotações. Faça uma consulta, através da API AwsomeAPI (https://docs.awesomeapi.com.br/api-de-moedas), que retorne as últimas N cotações da moeda, em Reais, bem como a data da cotação.  

Dica: utilize a biblioteca datetime e a função fromtimestamp
'''

import requests
from datetime import datetime

codigo_moeda = input('Informe o código da moeda (ex: USD, EUR): ').upper()
quantidade_cotacoes = int(input('Informe a quantidade de cotações: '))  

resposta = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{codigo_moeda}-BRL/{quantidade_cotacoes}')

if resposta.status_code == 200:
    cotacoes = resposta.json()

    for cotacao in cotacoes:
        # Convertendo o timestamp de string para int antes de usar no datetime
        data_cotacao = datetime.fromtimestamp(int(cotacao['timestamp']))
        valor_cotacao = float(cotacao['bid'])
        
        # Formatando a data para o padrão brasileiro (DD/MM/AAAA)
        print(f'Data: {data_cotacao.strftime("%d/%m/%Y")}, Cotação: R$ {valor_cotacao:.2f}')
else:
    print("Erro ao buscar dados. Verifique o código da moeda.")
