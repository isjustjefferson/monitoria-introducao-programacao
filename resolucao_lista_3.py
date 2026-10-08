# ==============================================================
# RESOLUÇÃO - LISTA DE EXERCÍCIOS 3
# Disciplina: Introdução à Programação 
# ==============================================================
# Enunciado geral: Utilize as três estruturas de repetição para resolver
# todas as questões abaixo.
#
# Observações:
# - for: repete um número determinado de vezes.
#       for numero in range(1, 51):   # conta de 1 até 50
# - while: repete enquanto uma condição for verdadeira.
# - Em Python não existe o do-while; ele é feito com while + break.
# - range(inicio, fim) vai de "inicio" até "fim - 1".
# - range(50, 0, -1) conta de 50 até 1, diminuindo de 1 em 1.
# ==============================================================


# -------------------------------------------------------------
# Questão 1
# Enunciado: Desenvolva um algoritmo em python que imprima todos os números
#            inteiros de 1 a 50 (em ordem crescente).
# -------------------------------------------------------------

for numero in range(1, 51):
    print(numero)


# -------------------------------------------------------------
# Questão 2
# Enunciado: Desenvolva um algoritmo em python que imprima todos os números
#            inteiros de 1 a 50 (em ordem decrescente).
# -------------------------------------------------------------

for numero in range(50, 0, -1):
    print(numero)


# -------------------------------------------------------------
# Questão 3
# Enunciado: Desenvolva um algoritmo em python que receba dez números do usuário
#            e imprima a soma de todos os números digitados.
# -------------------------------------------------------------

soma = 0

for contador in range(10):
    numero = float(input("Digite um número: "))
    soma = soma + numero

print("A soma de todos os números é:", soma)


# -------------------------------------------------------------
# Questão 4
# Enunciado: Desenvolva um algoritmo em python que receba dez números do usuário
#            e imprima a soma da metade de todos os números digitados.
# -------------------------------------------------------------

soma_das_metades = 0

for contador in range(10):
    numero = float(input("Digite um número: "))
    soma_das_metades = soma_das_metades + numero / 2

print("A soma das metades é:", soma_das_metades)


# -------------------------------------------------------------
# Questão 5
# Enunciado: Desenvolva um algoritmo em python que receba 5 números do usuário e,
#            ao final, imprima quantos destes valores são pares e ímpares.
# -------------------------------------------------------------

quantidade_pares = 0
quantidade_impares = 0

for contador in range(5):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:          # % 2 igual a 0 significa que o número é par
        quantidade_pares = quantidade_pares + 1
    else:
        quantidade_impares = quantidade_impares + 1

print("Quantidade de pares:", quantidade_pares)
print("Quantidade de ímpares:", quantidade_impares)


# -------------------------------------------------------------
# Questão 6
# Enunciado: Desenvolva um algoritmo em python que leia um número n que indica
#            quantos valores devem ser lidos a seguir. Após isso, o usuário deve
#            digitar os números e, ao final, o algoritmo deve imprimir a soma de
#            todos eles.
# -------------------------------------------------------------

quantidade = int(input("Quantos números você vai digitar? "))

soma = 0
contador = 0

# while: fica repetindo enquanto o contador for menor que a quantidade
while contador < quantidade:
    numero = float(input("Digite um número: "))
    soma = soma + numero
    contador = contador + 1

print("A soma de todos os números é:", soma)


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


# -------------------------------------------------------------
# Questão 8
# Enunciado: Escreva um algoritmo que leia dois inteiros, início e fim, e exiba
#            todos os números primos presentes dentro desse intervalo fechado.
# -------------------------------------------------------------

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print("Números primos entre", inicio, "e", fim, ":")

# Um número é primo se for maior que 1 e tiver apenas 2 divisores: 1 e ele mesmo
for numero in range(inicio, fim + 1):
    quantidade_divisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            quantidade_divisores = quantidade_divisores + 1

    if quantidade_divisores == 2:
        print(numero)
