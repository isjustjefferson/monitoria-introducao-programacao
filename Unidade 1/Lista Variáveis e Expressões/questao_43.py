# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 43
# Enunciado: Escreva um programa de ajuda para vendedores. A partir de um valor total
#            lido, mostre:
#            - o total a pagar com desconto de 10%;
#            - o valor de cada parcela, no parcelamento de 3x sem juros;
#            - a comissão do vendedor, no caso da venda ser à vista
#              (5% sobre o valor com desconto);
#            - a comissão do vendedor, no caso da venda ser parcelada
#              (5% sobre o valor total).
# -------------------------------------------------------------

valor_total = float(input("Digite o valor total da venda: R$ "))

total_com_desconto = valor_total - valor_total * 0.10
valor_parcela = valor_total / 3
comissao_a_vista = total_com_desconto * 0.05
comissao_parcelada = valor_total * 0.05

print("Total a pagar com desconto: R$", total_com_desconto)
print("Valor de cada parcela (3x): R$", valor_parcela)
print("Comissão à vista: R$", comissao_a_vista)
print("Comissão parcelada: R$", comissao_parcelada)
