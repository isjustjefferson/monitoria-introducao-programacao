# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 47
# Enunciado: Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.
# -------------------------------------------------------------

total_segundos = int(input("Digite o total de segundos: "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
