# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 39
# Enunciado: Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
#            tabela que considera o salário atual e o tempo de serviço. Leia o salário e o
#            tempo de serviço (anos) e imprima o salário reajustado, ou uma mensagem caso
#            o funcionário não tenha direito a nenhum aumento.
#            Salário Atual -> Reajuste:      Tempo de Serviço -> Bônus:
#            até 500,00     -> 25%           abaixo de 1 ano   -> sem bônus
#            até 1000,00    -> 20%           de 1 a 3 anos     -> 100,00
#            até 1500,00    -> 15%           de 4 a 6 anos     -> 200,00
#            até 2000,00    -> 10%           de 7 a 10 anos    -> 300,00
#            acima de 2000,00 -> sem reajuste mais de 10 anos -> 500,00
# -------------------------------------------------------------

salario = float(input("Digite o salário atual: R$ "))
tempo = int(input("Digite o tempo de serviço (anos): "))

if salario <= 500:
    reajuste = 0.25
elif salario <= 1000:
    reajuste = 0.20
elif salario <= 1500:
    reajuste = 0.15
elif salario <= 2000:
    reajuste = 0.10
else:
    reajuste = 0

if tempo < 1:
    bonus = 0
elif tempo <= 3:
    bonus = 100.00
elif tempo <= 6:
    bonus = 200.00
elif tempo <= 10:
    bonus = 300.00
else:
    bonus = 500.00

if reajuste == 0:
    print("O funcionário não tem direito a reajuste.")
else:
    salario_final = salario + salario * reajuste + bonus
    print("Salário final reajustado: R$", salario_final)
