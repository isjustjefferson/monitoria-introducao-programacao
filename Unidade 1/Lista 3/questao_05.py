# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 5
# Enunciado: Desenvolva um algoritmo em python que receba 5 números do usuário e,
#            ao final, imprima quantos destes valores são pares e ímpares.
# -------------------------------------------------------------

quantidade_pares = 0
quantidade_impares = 0

for contador in range(5):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:          # % 2 igual a 0 significa que o número é par
        quantidade_pares = quantidade_pares + 1
    else:
        quantidade_impares = quantidade_impares + 1

print("Quantidade de pares:", quantidade_pares)
print("Quantidade de ímpares:", quantidade_impares)
