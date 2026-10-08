# ==============================================================
# RESOLUÇÃO - LISTA DE EXERCÍCIOS 1
# Disciplina: Introdução à Programação
# ==============================================================
# Observações:
# - input() sempre lê um TEXTO (string).
# - int(input()) converte para número inteiro.
# - float(input()) converte para número decimal (com vírgula).
# - print() serve para mostrar o resultado na tela.
# ==============================================================


# -------------------------------------------------------------
# Questão 1
# Enunciado: Sabendo que a área de um trapézio pode ser calculada como:
#            Área = ((BaseMaior + BaseMenor) * altura) / 2
#            Faça um programa que receba os dados de entrada necessários
#            e calcule a área do trapézio.
# -------------------------------------------------------------

base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

area = ((base_maior + base_menor) * altura) / 2

print("A área do trapézio é:", area)


# -------------------------------------------------------------
# Questão 2
# Enunciado: Faça um programa que leia o raio de um círculo e calcule:
#            a) O comprimento da circunferência: Comprimento = 2 * PI * Raio
#            b) A área da circunferência: Área = PI * Raio ao quadrado
#            c) O volume da esfera: Volume = (4/3) * PI * Raio ao cubo
#            OBS: Para utilizar a função PI, pode-se utilizar a instrução
#            math.pi, importando a biblioteca math, com a instrução import math.
# -------------------------------------------------------------

import math

raio = float(input("Digite o raio do círculo: "))

comprimento = 2 * math.pi * raio
area_circulo = math.pi * raio ** 2
volume_esfera = (4 / 3) * math.pi * raio ** 3

print("Comprimento da circunferência:", comprimento)
print("Área do círculo:", area_circulo)
print("Volume da esfera:", volume_esfera)


# -------------------------------------------------------------
# Questão 3
# Enunciado: Faça um programa que receba o ano de nascimento de uma pessoa
#            e o ano atual e, com estes valores, calcule aproximadamente:
#            a) A idade da pessoa em anos.
#            b) A idade da pessoa em meses (1 ano = 12 meses).
#            c) A idade da pessoa em dias (1 ano = 365 dias).
#            d) A idade dessa pessoa em semanas (1 ano = 52 semanas).
# -------------------------------------------------------------

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)


# -------------------------------------------------------------
# Questão 4
# Enunciado: Sabendo que um caixa eletrônico terá notas de R$ 50 e R$ 10,
#            faça um programa que, fornecido um valor para saque (inteiro),
#            calcule quantas notas de 50 e quantas notas de 10 o cliente
#            deve receber em um caixa eletrônico, além de indicar a parte
#            do valor cujo saque é impossível (resto entre 0 e 9, inclusive).
#            O número de notas deve ser o menor possível.
# -------------------------------------------------------------

saque = int(input("Digite o valor do saque: "))

# Primeiro pegamos as notas de R$ 50 (maiores) e depois o que sobrou.
notas_de_50 = saque // 50        # // devolve só a parte inteira da divisão
resto = saque % 50               # % devolve o resto da divisão

notas_de_10 = resto // 10
valor_nao_sacavel = resto % 10

print("Notas de R$ 50:", notas_de_50)
print("Notas de R$ 10:", notas_de_10)

if valor_nao_sacavel > 0:
    print("Não é possível sacar o valor de: R$", valor_nao_sacavel)
else:
    print("O valor inteiro pode ser sacado.")


# -------------------------------------------------------------
# Questão 5
# Enunciado: Construa um algoritmo que, tendo como dados de entrada dois
#            pontos quaisquer no plano, P(x1, y1) e P(x2, y2), escreva a
#            distância entre eles. A fórmula que efetua tal cálculo é:
#            distância = raiz de ((x2 - x1) ao quadrado + (y2 - y1) ao quadrado)
#            Para a raiz quadrada pode-se utilizar a instrução math.sqrt(),
#            importando a biblioteca math, com a instrução import math.
# -------------------------------------------------------------

import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("A distância entre os pontos é:", distancia)
