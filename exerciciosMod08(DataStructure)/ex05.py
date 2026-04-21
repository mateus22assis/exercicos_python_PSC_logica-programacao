'''Crie um código Python que solicite ao usuário que informe 5 CEPs.
Armazene os CEPs em uma lista. Em seguida, percorra a lista e, para cada CEP, liste os seguintes dados (utilizando a API ViaCEP):  

  CEP: CEP
  Logradouro: Logradouro
  Complemento: Complemento
  Bairro: Bairro
  Localidade: Localidade
  UF: UF

Caso a requisição não retorne dados válidos, imprima:
CEP inválido: CEP
'''

import requests

ceps = [input('Informe um CEP: ') for _ in range(5)]    

for cep in ceps:
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    dados_cep = resposta.json()
    
    if 'erro' in dados_cep:
        print(f'CEP inválido: {cep}')
    else:
        print(f'CEP: {dados_cep["cep"]}')
        print(f'Logradouro: {dados_cep["logradouro"]}')
        print(f'Complemento: {dados_cep["complemento"]}')
        print(f'Bairro: {dados_cep["bairro"]}')
        print(f'Localidade: {dados_cep["localidade"]}')
        print(f'UF: {dados_cep["uf"]}')
        print('---')