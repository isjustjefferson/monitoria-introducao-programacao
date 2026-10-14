# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 42
# Enunciado: Receba o salário-base de um funcionário. Calcule e imprima o salário a
#            receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o
#            salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
# -------------------------------------------------------------

salario_base = float(input("Digite o salário-base: R$ "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_a_receber = salario_base + gratificacao - imposto

print("Salário a receber: R$", salario_a_receber)
