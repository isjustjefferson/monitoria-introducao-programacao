# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 4
# Enunciado: Faça um programa que leia um número e, caso ele seja positivo, calcule e
#            mostre:
#            - O número digitado ao quadrado
#            - A raiz quadrada do número digitado
# -------------------------------------------------------------

numero = float(input("Digite um número: "))

if numero > 0:
    print("Número ao quadrado:", numero ** 2)
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("O número não é positivo.")
