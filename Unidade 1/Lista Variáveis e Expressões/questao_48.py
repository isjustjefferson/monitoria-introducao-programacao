# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

# -------------------------------------------------------------
# Questão 48
# Enunciado: Faça um programa para ler o horário (hora, minuto e segundo) de início e a
#            duração, em segundos, de uma experiência biológica. O programa deve resultar
#            com o novo horário (hora, minuto e segundo) do término da mesma.
# -------------------------------------------------------------

hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))
segundo_inicio = int(input("Digite o segundo de início: "))
duracao = int(input("Digite a duração em segundos: "))

total_segundos = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + duracao

hora_termino = (total_segundos // 3600) % 24
minuto_termino = (total_segundos % 3600) // 60
segundo_termino = total_segundos % 60

print("Horário de término:", hora_termino, ":", minuto_termino, ":", segundo_termino)
