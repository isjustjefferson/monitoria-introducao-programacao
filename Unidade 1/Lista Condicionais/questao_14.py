# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 14
# Enunciado: A nota final de um estudante é calculada a partir de três notas atribuídas
#            entre 0 e 10, respectivamente, a um trabalho de laboratório, a uma avaliação
#            semestral e a um exame final. A média obedece aos pesos: Trabalho de
#            Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5.
#            De acordo com o resultado, mostre se o aluno está reprovado (média entre 0 e
#            2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado.
# -------------------------------------------------------------

laboratorio = float(input("Nota do trabalho de laboratório: "))
semestral = float(input("Nota da avaliação semestral: "))
final = float(input("Nota do exame final: "))

media = (laboratorio * 2 + semestral * 3 + final * 5) / 10
print("Média final:", media)

if media < 3:
    print("Reprovado")
elif media < 5:
    print("Recuperação")
else:
    print("Aprovado")
