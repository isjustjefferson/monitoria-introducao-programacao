# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 34
# Enunciado: Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De
#            acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma
#            redução de conceito.
#            Nota          Até 20 faltas | Mais de 20 faltas
#            9.0 a 10.0         A               B
#            7.5 a 8.9          B               C
#            5.0 a 7.4          C               D
#            4.0 a 4.9          D               E
#            0.0 a 3.9          E               E
# -------------------------------------------------------------

nota = float(input("Digite a nota: "))
faltas = int(input("Digite o número de faltas: "))

if faltas > 20:
    if nota >= 9.0:
        conceito = "B"
    elif nota >= 7.5:
        conceito = "C"
    elif nota >= 5.0:
        conceito = "D"
    elif nota >= 4.0:
        conceito = "E"
    else:
        conceito = "E"
else:
    if nota >= 9.0:
        conceito = "A"
    elif nota >= 7.5:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    elif nota >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

print("Conceito:", conceito)
