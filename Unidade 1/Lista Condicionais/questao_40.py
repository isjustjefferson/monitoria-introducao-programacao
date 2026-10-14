# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 40
# Enunciado: O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
#            comissão do distribuidor e dos impostos. A comissão e os impostos são
#            calculados sobre o custo de fábrica, conforme a tabela:
#            Custo de fábrica          | % Distribuidor | % Impostos
#            até R$12.000,00           |      5         | isento
#            entre R$12.000,00 e 25.000,00 |   10        | 15
#            acima de R$25.000,00      |     15         | 20
#            Leia o custo de fábrica e escreva o custo ao consumidor.
# -------------------------------------------------------------

custo_fabrica = float(input("Digite o custo de fábrica: R$ "))

if custo_fabrica <= 12000:
    percentual_distribuidor = 0.05
    percentual_impostos = 0
elif custo_fabrica <= 25000:
    percentual_distribuidor = 0.10
    percentual_impostos = 0.15
else:
    percentual_distribuidor = 0.15
    percentual_impostos = 0.20

comissao = custo_fabrica * percentual_distribuidor
impostos = custo_fabrica * percentual_impostos
custo_consumidor = custo_fabrica + comissao + impostos

print("Custo ao consumidor: R$", custo_consumidor)
