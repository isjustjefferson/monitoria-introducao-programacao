# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 51
# Enunciado: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser
#            repartido proporcionalmente ao valor que cada um deu para a realização da
#            aposta. Faça um programa que leia quanto cada apostador investiu, o valor do
#            prêmio, e imprima quanto cada um ganharia do prêmio com base no valor
#            investido.
# -------------------------------------------------------------

investimento1 = float(input("Digite o valor investido pelo apostador 1: R$ "))
investimento2 = float(input("Digite o valor investido pelo apostador 2: R$ "))
investimento3 = float(input("Digite o valor investido pelo apostador 3: R$ "))
premio = float(input("Digite o valor do prêmio: R$ "))

total_investido = investimento1 + investimento2 + investimento3

parte1 = premio * (investimento1 / total_investido)
parte2 = premio * (investimento2 / total_investido)
parte3 = premio * (investimento3 / total_investido)

print("Apostador 1 recebe: R$", parte1)
print("Apostador 2 recebe: R$", parte2)
print("Apostador 3 recebe: R$", parte3)
