# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 30
# Enunciado: Faça um programa que receba três números e mostre-os em ordem crescente.
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero1 > numero3:
    numero1, numero3 = numero3, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Ordem crescente:", numero1, numero2, numero3)
