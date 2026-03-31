maior_temperatura = float('-inf') # Inicializa com um valor muito baixo
menor_temperatura = float('inf')  # Inicializa com um valor muito alto

print("Por favor, digite as 10 temperaturas coletadas:")

for i in range(10):
    temperatura = float(input("Digite a temperatura (em graus Celsius): "))
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura
    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

print(f"\nA maior temperatura informada foi: {maior_temperatura}°C")
print(f"A menor temperatura informada foi: {menor_temperatura}°C")