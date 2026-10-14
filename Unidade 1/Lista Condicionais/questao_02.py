# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 2
# Enunciado: Leia um número fornecido pelo usuário. Se esse número for positivo, calcule
#            a raiz quadrada do número. Se o número for negativo, mostre uma mensagem
#            dizendo que o número é inválido.
# -------------------------------------------------------------

numero = float(input("Digite um número: "))

if numero >= 0:
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("Número inválido")
