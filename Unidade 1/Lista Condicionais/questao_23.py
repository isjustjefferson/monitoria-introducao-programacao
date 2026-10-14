# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 23
# Enunciado: Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
#            se for divisível por 400 ou se for divisível por 4 e não for divisível por
#            100. Por exemplo: 1988, 1992, 1996.
# -------------------------------------------------------------

ano = int(input("Digite um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
