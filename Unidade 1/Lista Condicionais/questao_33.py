# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 33
# Enunciado: Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço
#            antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do
#            preço novo (de acordo com a segunda tabela).
#            Preço antigo -> percentual de aumento:
#            - até R$ 50 -> 5%
#            - entre R$ 50 e R$ 100 -> 10%
#            - acima de R$ 100 -> 15%
#            Preço novo -> mensagem:
#            - até R$ 80 -> Barato
#            - entre R$ 80 e R$ 120 (inclusive) -> Normal
#            - entre R$ 120 e R$ 200 (inclusive) -> Caro
#            - acima de R$ 200 -> Muito caro
# -------------------------------------------------------------

preco_antigo = float(input("Digite o preço antigo: R$ "))

if preco_antigo <= 50:
    preco_novo = preco_antigo + preco_antigo * 0.05
elif preco_antigo <= 100:
    preco_novo = preco_antigo + preco_antigo * 0.10
else:
    preco_novo = preco_antigo + preco_antigo * 0.15

print("Preço novo: R$", preco_novo)

if preco_novo <= 80:
    print("Barato")
elif preco_novo <= 120:
    print("Normal")
elif preco_novo <= 200:
    print("Caro")
else:
    print("Muito caro")
