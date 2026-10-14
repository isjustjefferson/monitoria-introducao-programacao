# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 38
# Enunciado: Leia uma data de nascimento fornecida através de três números inteiros: Dia,
#            Mês e Ano. Teste a validade desta data: dia > 0, dia <= 28 para fevereiro
#            (29 se bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31
#            nos outros meses. Mês > 0 e mês < 13. Ano <= ano atual (use uma constante
#            igual a 2008). Imprimir "data válida" ou "data inválida".
# -------------------------------------------------------------

ANO_ATUAL = 2008

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_valida = False

if mes >= 1 and mes <= 12 and ano <= ANO_ATUAL:
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
    print("data válida")
else:
    print("data inválida")
