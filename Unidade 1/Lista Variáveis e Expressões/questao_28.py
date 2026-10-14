# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 28
# Enunciado: Faça a leitura de três valores e apresente como resultado a soma dos
#            quadrados dos três valores lidos.
# -------------------------------------------------------------

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

soma_dos_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2
print("Soma dos quadrados:", soma_dos_quadrados)
