# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 50
# Enunciado: Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule
#            sua distância da origem (0, 0).
# -------------------------------------------------------------

import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

distancia = math.sqrt(x ** 2 + y ** 2)
print("Distância da origem:", distancia)
