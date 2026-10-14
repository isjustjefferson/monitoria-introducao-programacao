# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 10
# Enunciado: Faça um programa que receba a altura e o sexo de uma pessoa e calcule e
#            mostre seu peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
#            - Homens: (72.7 * h) - 58
#            - Mulheres: (62.1 * h) - 44.7
# -------------------------------------------------------------

altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal (homem):", peso_ideal)
else:
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal (mulher):", peso_ideal)
