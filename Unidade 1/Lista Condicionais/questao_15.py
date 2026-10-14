# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 15
# Enunciado: Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da
#            semana correspondente a este número. Isto é, domingo se 1, segunda-feira se
#            2, e assim por diante.
# -------------------------------------------------------------

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido")
