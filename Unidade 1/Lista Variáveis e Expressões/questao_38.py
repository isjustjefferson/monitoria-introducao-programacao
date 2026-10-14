# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 38
# Enunciado: Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
#            sabendo que ele recebeu um aumento de 25%.
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))
novo_salario = salario + salario * 0.25
print("Novo salário: R$", novo_salario)
