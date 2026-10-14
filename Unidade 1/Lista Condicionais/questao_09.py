# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 9
# Enunciado: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se
#            a prestação for maior que 20% do salário imprima: "Empréstimo não
#            concedido", caso contrário imprima: "Empréstimo concedido".
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))
prestacao = float(input("Digite o valor da prestação: R$ "))

limite = salario * 0.20

if prestacao > limite:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
