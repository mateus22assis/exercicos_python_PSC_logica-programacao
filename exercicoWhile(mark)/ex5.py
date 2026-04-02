''' Exercício 5: Simulador de crescimento
Simule uma população:
População A: 1000, cresce 3% ao ano 
População B: 2000, cresce 1.5% ao ano 
Use while até A ultrapassar B.
Dentro do loop:
Atualize valores 
Conte anos 
'''
populacaoA = 1000
populacaoB = 2000
crescimentoA = 0.03
crescimentoB = 0.015
anos = 0

while populacaoA <= populacaoB:
    populacaoA += populacaoA * crescimentoA
    populacaoB += populacaoB * crescimentoB
    anos += 1

print(f"A população A ultrapassou a população B em {anos} anos.")