# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 35
# Enunciado: Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela
#            equação: hipotenusa = raiz(a² + b²). Faça um programa que receba os valores
#            de a e b e calcule o valor da hipotenusa através da equação.
# -------------------------------------------------------------

import math

a = float(input("Digite o cateto a: "))
b = float(input("Digite o cateto b: "))

hipotenusa = math.sqrt(a ** 2 + b ** 2)
print("Hipotenusa:", hipotenusa)
