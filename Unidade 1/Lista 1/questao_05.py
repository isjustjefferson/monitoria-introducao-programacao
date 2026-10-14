# ==============================================================
# Introdução à Programação
# Lista 1
# ==============================================================

# -------------------------------------------------------------
# Questão 5
# Enunciado: Construa um algoritmo que, tendo como dados de entrada dois
#            pontos quaisquer no plano, P(x1, y1) e P(x2, y2), escreva a
#            distância entre eles. A fórmula que efetua tal cálculo é:
#            distância = raiz de ((x2 - x1) ao quadrado + (y2 - y1) ao quadrado)
#            Para a raiz quadrada pode-se utilizar a instrução math.sqrt(),
#            importando a biblioteca math, com a instrução import math.
# -------------------------------------------------------------

import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("A distância entre os pontos é:", distancia)
