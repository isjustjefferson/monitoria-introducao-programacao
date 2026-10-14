# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 6
# Enunciado: Escreva um programa que, dados dois números inteiros, mostre na tela o maior
#            deles, assim como a diferença existente entre ambos.
# -------------------------------------------------------------

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("Maior:", numero1)
    print("Diferença:", numero1 - numero2)
else:
    print("Maior:", numero2)
    print("Diferença:", numero2 - numero1)
