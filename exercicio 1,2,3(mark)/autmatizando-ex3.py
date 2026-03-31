import requests

print("--- Conversor Automático de Dólar para Real ---")

try:
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    response = requests.get(url)
    data = response.json()
    
    cotacao_atual = float(data["USDBRL"]["bid"])

    print(f"Cotação atual do dólar buscada com sucesso: R$ {cotacao_atual:.2f}")
  
    valor_dolar = float(input("Digite o valor que você possui em dólares: "))
   
    valor_reais = cotacao_atual * valor_dolar
    print(f"\nCom US$ {valor_dolar:.2f}, você tem aproximadamente R$ {valor_reais:.2f}")

except Exception as e:
    print("Erro ao buscar a cotação. Verifique sua conexão com a internet.")
