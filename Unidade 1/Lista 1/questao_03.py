# ==============================================================
# Introdução à Programação
# Lista 1
# ==============================================================

# -------------------------------------------------------------
# Questão 3
# Enunciado: Faça um programa que receba o ano de nascimento de uma pessoa
#            e o ano atual e, com estes valores, calcule aproximadamente:
#            a) A idade da pessoa em anos.
#            b) A idade da pessoa em meses (1 ano = 12 meses).
#            c) A idade da pessoa em dias (1 ano = 365 dias).
#            d) A idade dessa pessoa em semanas (1 ano = 52 semanas).
# -------------------------------------------------------------

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)
