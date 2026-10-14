# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

# -------------------------------------------------------------
# Questão 4
# Enunciado: Considere que o último concurso vestibular apresentou três provas:
#            Português, Matemática e Conhecimentos Gerais. Considerando que para
#            cada candidato tem-se um registro contendo o seu nome e as notas
#            obtidas em cada uma das provas, construa um algoritmo que forneça:
#            a) o nome e as notas em cada prova do candidato
#            b) a média do candidato
#            c) uma informação dizendo se o candidato foi aprovado ou não.
#            Considere que um candidato é aprovado se sua média for maior que 7.0
#            e se não apresentou nenhuma nota abaixo de 5.0.
# -------------------------------------------------------------

nome = input("Digite o nome do candidato: ")
nota_portugues = float(input("Nota de Português: "))
nota_matematica = float(input("Nota de Matemática: "))
nota_conhecimentos = float(input("Nota de Conhecimentos Gerais: "))

media = (nota_portugues + nota_matematica + nota_conhecimentos) / 3

print("Nome do candidato:", nome)
print("Notas:", nota_portugues, nota_matematica, nota_conhecimentos)
print("Média:", media)

# Só é aprovado SE a média for maior que 7.0 E nenhuma nota for menor que 5.0
if media > 7.0 and nota_portugues >= 5.0 and nota_matematica >= 5.0 and nota_conhecimentos >= 5.0:
    print("Aprovado!")
else:
    print("Reprovado.")
