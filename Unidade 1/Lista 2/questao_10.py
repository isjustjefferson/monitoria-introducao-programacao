# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

# -------------------------------------------------------------
# Questão 10
# Enunciado: Crie um algoritmo que calcula o desconto previdenciário de um
#            funcionário. Dado um salário, o programa deve retornar o valor do
#            desconto proporcional ao mesmo. O cálculo segue a regra:
#            o desconto é de 11% do valor do salário, entretanto, o valor máximo
#            a ser descontado é R$ 318,20.
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))

desconto = salario * 0.11

# O desconto nunca pode passar de R$ 318,20
if desconto > 318.20:
    desconto = 318.20

salario_liquido = salario - desconto

print("Valor do desconto: R$", desconto)
print("Salário após o desconto: R$", salario_liquido)
