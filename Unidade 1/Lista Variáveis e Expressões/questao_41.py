# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 41
# Enunciado: Faça um programa que leia o valor da hora de trabalho (em reais) e o número
#            de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário,
#            adicionando 10% sobre o valor calculado.
# -------------------------------------------------------------

valor_hora = float(input("Digite o valor da hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

valor = valor_hora * horas_trabalhadas
valor_com_aumento = valor + valor * 0.10

print("Valor a ser pago: R$", valor_com_aumento)
