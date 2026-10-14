# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 19
# Enunciado: Faça um programa para verificar se um determinado número inteiro é divisível
#            por 3 ou 5, mas não simultaneamente pelos dois.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

divisivel_por_3 = numero % 3 == 0
divisivel_por_5 = numero % 5 == 0

if (divisivel_por_3 or divisivel_por_5) and not (divisivel_por_3 and divisivel_por_5):
    print("O número é divisível por 3 ou por 5, mas não pelos dois.")
else:
    print("O número não atende à condição.")
