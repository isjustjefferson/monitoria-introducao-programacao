# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 3
# Enunciado: Leia um número real. Se o número for positivo imprima a raiz quadrada.
#            Do contrário, imprima o número ao quadrado.
# -------------------------------------------------------------

numero = float(input("Digite um número real: "))

if numero > 0:
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("Número ao quadrado:", numero ** 2)
