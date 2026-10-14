# ==============================================================
# Introdução à Programação
# Lista 1
# ==============================================================

# -------------------------------------------------------------
# Questão 1
# Enunciado: Sabendo que a área de um trapézio pode ser calculada como:
#            Área = ((BaseMaior + BaseMenor) * altura) / 2
#            Faça um programa que receba os dados de entrada necessários
#            e calcule a área do trapézio.
# -------------------------------------------------------------

base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

area = ((base_maior + base_menor) * altura) / 2

print("A área do trapézio é:", area)
