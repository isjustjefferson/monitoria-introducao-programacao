# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 11
# Enunciado: Escreva um programa que leia um número inteiro maior do que zero e devolva,
#            na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251
#            corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que
#            zero, o programa terminará com a mensagem "Número inválido".
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro maior que zero: "))

if numero > 0:
    soma = 0
    while numero > 0:
        soma = soma + numero % 10   # pega o último algarismo
        numero = numero // 10       # remove o último algarismo
    print("Soma dos algarismos:", soma)
else:
    print("Número inválido")
