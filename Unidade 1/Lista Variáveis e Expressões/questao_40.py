# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 40
# Enunciado: Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
#            solicite o número de dias trabalhados pelo encanador e imprima a quantia
#            líquida que deverá ser paga, sabendo-se que são descontados 8% para
#            imposto de renda.
# -------------------------------------------------------------

dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

valor_bruto = dias_trabalhados * 30.00
imposto = valor_bruto * 0.08
valor_liquido = valor_bruto - imposto

print("Valor líquido a receber: R$", valor_liquido)
