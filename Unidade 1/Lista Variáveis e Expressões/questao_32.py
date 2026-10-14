# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 32
# Enunciado: Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
#            antecessor de seu dobro.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

sucessor_do_triplo = numero * 3 + 1
antecessor_do_dobro = numero * 2 - 1
resultado = sucessor_do_triplo + antecessor_do_dobro

print("Resultado:", resultado)
