# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 37
# Enunciado: As tarifas de certo parque de estacionamento são as seguintes:
#            - 1ª e 2ª hora - R$ 1,00 cada
#            - 3ª e 4ª hora - R$ 1,40 cada
#            - 5ª hora e seguintes - R$ 2,00 cada
#            O número de horas a pagar é sempre inteiro e arredondado por excesso. Os
#            momentos de chegada e partida são dados por pares de inteiros (hora e
#            minuto). Se a hora de chegada for maior que a de partida, a partida ocorreu
#            no dia seguinte.
# -------------------------------------------------------------

hora_chegada = int(input("Hora de chegada: "))
minuto_chegada = int(input("Minuto de chegada: "))
hora_partida = int(input("Hora de partida: "))
minuto_partida = int(input("Minuto de partida: "))

total_chegada = hora_chegada * 60 + minuto_chegada
total_partida = hora_partida * 60 + minuto_partida

if total_partida < total_chegada:
    total_partida = total_partida + 24 * 60

minutos = total_partida - total_chegada

# Arredonda as horas para cima (por excesso)
horas = minutos // 60
if minutos % 60 != 0:
    horas = horas + 1

if horas <= 2:
    preco = horas * 1.00
elif horas <= 4:
    preco = 2 * 1.00 + (horas - 2) * 1.40
else:
    preco = 2 * 1.00 + 2 * 1.40 + (horas - 4) * 2.00

print("Horas pagas:", horas)
print("Preço cobrado: R$", preco)
