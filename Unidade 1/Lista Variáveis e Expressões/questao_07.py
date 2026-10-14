# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 7
# Enunciado: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
#            Celsius. A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0.
# -------------------------------------------------------------

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print("Temperatura em Celsius:", celsius)
