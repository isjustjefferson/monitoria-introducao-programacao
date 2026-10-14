# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 39
# Enunciado: A importância de R$ 780.000,00 será dividida entre três ganhadores de um
#            concurso. Sendo que da quantia total:
#            - O primeiro ganhador receberá 46%;
#            - O segundo receberá 32%;
#            - O terceiro receberá o restante.
#            Calcule e imprima a quantia ganha por cada um dos ganhadores.
# -------------------------------------------------------------

importancia = 780000.00

primeiro = importancia * 0.46
segundo = importancia * 0.32
terceiro = importancia - primeiro - segundo

print("Primeiro ganhador: R$", primeiro)
print("Segundo ganhador: R$", segundo)
print("Terceiro ganhador: R$", terceiro)
