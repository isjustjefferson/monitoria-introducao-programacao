# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 30
# Enunciado: Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor
#            correspondente em dólares.
# -------------------------------------------------------------

valor_reais = float(input("Digite o valor em reais: R$ "))
cotacao_dolar = float(input("Digite a cotação do dólar: R$ "))

valor_dolares = valor_reais / cotacao_dolar
print("Valor em dólares: US$", valor_dolares)
