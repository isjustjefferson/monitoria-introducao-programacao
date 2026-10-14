# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 35
# Enunciado: Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
#            entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias
#            em anos bissextos, e 28 dias em anos não bissextos.
# -------------------------------------------------------------

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_valida = False

if mes >= 1 and mes <= 12:
    if mes == 2:
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            if dia >= 1 and dia <= 29:
                data_valida = True
        else:
            if dia >= 1 and dia <= 28:
                data_valida = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            data_valida = True
    else:
        if dia >= 1 and dia <= 31:
            data_valida = True

if data_valida:
    print("Data válida")
else:
    print("Data inválida")
