# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 4
# Enunciado: Desenvolva um algoritmo em python que receba dez números do usuário
#            e imprima a soma da metade de todos os números digitados.
# -------------------------------------------------------------

soma_das_metades = 0

for contador in range(10):
    numero = float(input("Digite um número: "))
    soma_das_metades = soma_das_metades + numero / 2

print("A soma das metades é:", soma_das_metades)
