# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 46
# Enunciado: Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito
#            por linha.
# -------------------------------------------------------------

numero = int(input("Digite um número de quatro dígitos (1000 a 9999): "))

milhar = numero // 1000
centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
