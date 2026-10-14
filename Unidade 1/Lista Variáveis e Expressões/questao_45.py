# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 45
# Enunciado: Faça um programa que leia um número inteiro positivo de três dígitos
#            (de 100 a 999). Gere outro número formado pelos dígitos invertidos do
#            número lido. Exemplo: NúmeroLido = 123 -> NúmeroGerado = 321.
# -------------------------------------------------------------

numero = int(input("Digite um número de três dígitos (100 a 999): "))

centena = numero // 100
dezena = (numero // 10) % 10
unidade = numero % 10

invertido = unidade * 100 + dezena * 10 + centena
print("Número invertido:", invertido)
