# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 13
# Enunciado: Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A
#            primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
#            mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A
#            nota para aprovação deve ser igual ou superior a 60 pontos.
# -------------------------------------------------------------

prova1 = float(input("Digite a nota da prova 1: "))
prova2 = float(input("Digite a nota da prova 2: "))
prova3 = float(input("Digite a nota da prova 3: "))

media = (prova1 * 1 + prova2 * 1 + prova3 * 2) / 4
print("Média ponderada:", media)

if media >= 60:
    print("Aprovado")
else:
    print("Reprovado")
