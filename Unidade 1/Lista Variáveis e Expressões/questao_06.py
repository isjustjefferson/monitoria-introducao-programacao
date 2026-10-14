# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 6
# Enunciado: Leia uma temperatura em graus Celsius e apresente-a convertida em graus
#            Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0.
# -------------------------------------------------------------

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * (9.0 / 5.0) + 32.0
print("Temperatura em Fahrenheit:", fahrenheit)
