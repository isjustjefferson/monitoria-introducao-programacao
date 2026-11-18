# ==============================================================
# Introdução à Programação
# Prova da 1ª Unidade
# ==============================================================

# -------------------------------------------------------------
# Questão 10
# Enunciado: Temperaturas. Leia temperaturas até o usuário 
# digitar 999 (valor sentinela, que não entra nos cálculos). 
# Ao final, mostre a quantidade de leituras, a média, a maior 
# e a menor temperatura. Se nenhuma temperatura for informada,
# mostre uma mensagem adequada, sem dividir po zero.
# -------------------------------------------------------------
# Exemplo de execução:
# Temperatura (999 para encerrar): 28.5
# Temperatura (999 para encerrar): 31
# Temperatura (999 para encerrar): 26
# Temperatura (999 para encerrar): 999
# Leituras: 3 | Média: 28.50 | Maior: 31.0 | Menor: 26.0
# -------------------------------------------------------------

leituras = 0
total = 0
maior = 0
menor = 999

while True:
    temperatura = float(input("Temperatura (999 para encerrar): "))
    if temperatura == 999:
        break
    leituras += 1
    total += temperatura
    maior = temperatura if temperatura > maior else maior
    menor = temperatura if temperatura < menor else menor

if leituras == 0:
    print("Nenhuma temperatura informada.")
else:
    print(f"Leituras: {leituras}", f"Média: {(total/leituras):.2f}", f"Maior: {maior:.1f}", f"Menor: {menor:.1f}", sep=" | ")