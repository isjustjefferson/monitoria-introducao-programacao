# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 29
# Enunciado: Faça uma prova de matemática para crianças que estão aprendendo a somar
#            números inteiros menores do que 100. Escolha números aleatórios entre 1 e
#            100 e mostre a pergunta: qual é a soma de a + b? Peça a resposta. Faça cinco
#            perguntas ao aluno e mostre para ele as perguntas e as respostas corretas,
#            além de quantas vezes o aluno acertou.
# -------------------------------------------------------------

import random

acertos = 0

for pergunta in range(5):
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    resposta = int(input("Qual é a soma de " + str(a) + " + " + str(b) + "? "))

    print("Resposta correta:", a + b)

    if resposta == a + b:
        print("Você acertou!")
        acertos = acertos + 1
    else:
        print("Você errou.")

print("Total de acertos:", acertos)
