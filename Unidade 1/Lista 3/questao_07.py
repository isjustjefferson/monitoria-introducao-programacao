# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 7
# Enunciado: Construa um algoritmo que leia a idade, o sexo ("M"/"F") e a renda
#            mensal de vários habitantes. O laço deve ser encerrado quando o
#            usuário digitar a idade inferior a 18. Ao final, o programa deve
#            exibir:
#            - A média de renda do grupo;
#            - A maior e a menor idade registradas;
#            - A quantidade de mulheres com renda superior a R$ 3.000,00.
# -------------------------------------------------------------

soma_rendas = 0
quantidade_pessoas = 0
quantidade_mulheres_renda_alta = 0
maior_idade = 0
menor_idade = 999

idade = int(input("Digite a idade (menor que 18 encerra o programa): "))

# O laço só continua enquanto a idade for maior ou igual a 18
while idade >= 18:
    sexo = input("Digite o sexo (M/F): ")
    renda = float(input("Digite a renda mensal: R$ "))

    soma_rendas = soma_rendas + renda
    quantidade_pessoas = quantidade_pessoas + 1

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade:
        menor_idade = idade

    if sexo == "F" and renda > 3000:
        quantidade_mulheres_renda_alta = quantidade_mulheres_renda_alta + 1

    idade = int(input("Digite a idade (menor que 18 encerra o programa): "))

# A pessoa que digitou idade menor que 18 não entra nos cálculos
if quantidade_pessoas > 0:
    media_renda = soma_rendas / quantidade_pessoas
    print("Média de renda do grupo: R$", media_renda)
    print("Maior idade registrada:", maior_idade)
    print("Menor idade registrada:", menor_idade)
    print("Mulheres com renda superior a R$ 3.000,00:", quantidade_mulheres_renda_alta)
else:
    print("Nenhuma pessoa com 18 anos ou mais foi registrada.")
