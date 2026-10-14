# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 36
# Enunciado: Escreva um programa que, dado o valor da venda, imprima a comissão que
#            deverá ser paga ao vendedor. Considere a tabela:
#            Venda mensal                                  | Comissão
#            Maior ou igual a R$100.000,00                 | R$700,00 + 16%
#            Menor que R$100.000,00 e >= R$80.000,00       | R$650,00 + 14%
#            Menor que R$80.000,00 e >= R$60.000,00        | R$600,00 + 14%
#            Menor que R$60.000,00 e >= R$40.000,00        | R$550,00 + 14%
#            Menor que R$40.000,00 e >= R$20.000,00        | R$500,00 + 14%
#            Menor que R$20.000,00                         | R$400,00 + 14%
# -------------------------------------------------------------

venda = float(input("Digite o valor da venda: R$ "))

if venda >= 100000:
    comissao = 700 + venda * 0.16
elif venda >= 80000:
    comissao = 650 + venda * 0.14
elif venda >= 60000:
    comissao = 600 + venda * 0.14
elif venda >= 40000:
    comissao = 550 + venda * 0.14
elif venda >= 20000:
    comissao = 500 + venda * 0.14
else:
    comissao = 400 + venda * 0.14

print("Comissão: R$", comissao)
