# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 8
# Enunciado: Escreva um algoritmo que leia dois inteiros, início e fim, e exiba
#            todos os números primos presentes dentro desse intervalo fechado.
# -------------------------------------------------------------

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print("Números primos entre", inicio, "e", fim, ":")

# Um número é primo se for maior que 1 e tiver apenas 2 divisores: 1 e ele mesmo
for numero in range(inicio, fim + 1):
    quantidade_divisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            quantidade_divisores = quantidade_divisores + 1

    if quantidade_divisores == 2:
        print(numero)
