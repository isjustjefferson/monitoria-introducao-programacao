# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 37
# Enunciado: Faça um programa que leia o valor de um produto e imprima o valor com
#            desconto, tendo em vista que o desconto foi de 12%.
# -------------------------------------------------------------

valor_produto = float(input("Digite o valor do produto: R$ "))
valor_com_desconto = valor_produto - valor_produto * 0.12
print("Valor com desconto: R$", valor_com_desconto)
