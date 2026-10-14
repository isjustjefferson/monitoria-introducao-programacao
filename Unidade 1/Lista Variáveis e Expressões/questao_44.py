# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 44
# Enunciado: Receba a altura do degrau de uma escada e a altura que o usuário deseja
#            alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá
#            subir para atingir seu objetivo.
# -------------------------------------------------------------

import math

altura_degrau = float(input("Digite a altura do degrau: "))
altura_objetivo = float(input("Digite a altura a ser alcançada: "))

quantidade_degraus = math.ceil(altura_objetivo / altura_degrau)
print("Quantidade de degraus a subir:", quantidade_degraus)
