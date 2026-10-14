# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 17
# Enunciado: Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
#            A = (baseMaior + baseMenor) * altura / 2.
#            Lembre-se: a base maior e a base menor devem ser números maiores que zero.
# -------------------------------------------------------------

base_maior = float(input("Digite a base maior: "))
base_menor = float(input("Digite a base menor: "))

if base_maior > 0 and base_menor > 0:
    altura = float(input("Digite a altura: "))
    area = (base_maior + base_menor) * altura / 2
    print("Área do trapézio:", area)
else:
    print("As bases devem ser maiores que zero.")
