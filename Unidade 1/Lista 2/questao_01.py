# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

# -------------------------------------------------------------
# Questão 1
# Enunciado: Faça um algoritmo que leia um número N e imprima "F1", "F2" ou "F3",
#            conforme a condição:
#            - "F1", se N menor ou igual 10
#            - "F2", se N maior 10 e N menor ou igual 100
#            - "F3", se N maior 100
# -------------------------------------------------------------

numero = int(input("Digite um número: "))

if numero <= 10:
    print("F1")
elif numero > 10 and numero <= 100:
    print("F2")
else:
    print("F3")
