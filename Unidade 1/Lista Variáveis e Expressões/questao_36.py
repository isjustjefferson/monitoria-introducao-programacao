# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 36
# Enunciado: Leia a altura e o raio de um cilindro circular e imprima o volume do
#            cilindro. A fórmula é: V = PI * raio² * altura, onde PI = 3.141592.
# -------------------------------------------------------------

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = 3.141592 * raio ** 2 * altura
print("Volume do cilindro:", volume)
