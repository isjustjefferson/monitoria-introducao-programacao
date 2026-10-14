# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 8
# Enunciado: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus
#            Celsius. A fórmula de conversão é: C = K - 273.15.
# -------------------------------------------------------------

kelvin = float(input("Digite a temperatura em Kelvin: "))
celsius = kelvin - 273.15
print("Temperatura em Celsius:", celsius)
