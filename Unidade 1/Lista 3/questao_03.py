# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 3
# Enunciado: Desenvolva um algoritmo em python que receba dez números do usuário
#            e imprima a soma de todos os números digitados.
# -------------------------------------------------------------

soma = 0

for contador in range(10):
    numero = float(input("Digite um número: "))
    soma = soma + numero

print("A soma de todos os números é:", soma)
