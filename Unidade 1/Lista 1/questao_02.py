# ==============================================================
# Introdução à Programação
# Lista 1
# ==============================================================

# -------------------------------------------------------------
# Questão 2
# Enunciado: Faça um programa que leia o raio de um círculo e calcule:
#            a) O comprimento da circunferência: Comprimento = 2 * PI * Raio
#            b) A área da circunferência: Área = PI * Raio ao quadrado
#            c) O volume da esfera: Volume = (4/3) * PI * Raio ao cubo
#            OBS: Para utilizar a função PI, pode-se utilizar a instrução
#            math.pi, importando a biblioteca math, com a instrução import math.
# -------------------------------------------------------------

import math

raio = float(input("Digite o raio do círculo: "))

comprimento = 2 * math.pi * raio
area_circulo = math.pi * raio ** 2
volume_esfera = (4 / 3) * math.pi * raio ** 3

print("Comprimento da circunferência:", comprimento)
print("Área do círculo:", area_circulo)
print("Volume da esfera:", volume_esfera)
