# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

# -------------------------------------------------------------
# Questão 3
# Enunciado: Construa um algoritmo que receba como entrada três valores
#            e os imprima em ordem crescente.
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
numero3 = float(input("Digite o terceiro valor: "))

# Comparações para colocar em ordem (do menor para o maior).
# A linha abaixo troca os valores de lugar se a condição for verdadeira.
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

if numero1 > numero3:
    numero1, numero3 = numero3, numero1

if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Em ordem crescente:", numero1, numero2, numero3)
