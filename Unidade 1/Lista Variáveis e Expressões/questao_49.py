# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 49
# Enunciado: Implemente um programa que calcule o ano de nascimento de uma pessoa a
#            partir de sua idade e do ano atual.
# -------------------------------------------------------------

idade = int(input("Digite a idade: "))
ano_atual = int(input("Digite o ano atual: "))

ano_nascimento = ano_atual - idade
print("Ano de nascimento:", ano_nascimento)
