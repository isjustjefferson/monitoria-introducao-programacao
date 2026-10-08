# ==============================================================
# RESOLUÇÃO - LISTA DE EXERCÍCIOS: COMANDOS CONDICIONAIS
# Disciplina: Introdução à Programação 
# ==============================================================
# Observações:
# - Estrutura condicional: if / elif / else.
# - Python não possui o comando switch/case antigo; usamos if/elif/else.
# - Operadores relacionais: == != > < >= <=
# - Operadores lógicos: and, or, not
# ==============================================================


# -------------------------------------------------------------
# Questão 1
# Enunciado: Faça um programa que receba dois números e mostre qual deles é o maior.
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior é:", numero1)
else:
    print("O maior é:", numero2)


# -------------------------------------------------------------
# Questão 2
# Enunciado: Leia um número fornecido pelo usuário. Se esse número for positivo, calcule
#            a raiz quadrada do número. Se o número for negativo, mostre uma mensagem
#            dizendo que o número é inválido.
# -------------------------------------------------------------

numero = float(input("Digite um número: "))

if numero >= 0:
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("Número inválido")


# -------------------------------------------------------------
# Questão 3
# Enunciado: Leia um número real. Se o número for positivo imprima a raiz quadrada.
#            Do contrário, imprima o número ao quadrado.
# -------------------------------------------------------------

numero = float(input("Digite um número real: "))

if numero > 0:
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("Número ao quadrado:", numero ** 2)


# -------------------------------------------------------------
# Questão 4
# Enunciado: Faça um programa que leia um número e, caso ele seja positivo, calcule e
#            mostre:
#            - O número digitado ao quadrado
#            - A raiz quadrada do número digitado
# -------------------------------------------------------------

numero = float(input("Digite um número: "))

if numero > 0:
    print("Número ao quadrado:", numero ** 2)
    print("Raiz quadrada:", numero ** 0.5)
else:
    print("O número não é positivo.")


# -------------------------------------------------------------
# Questão 5
# Enunciado: Faça um programa que receba um número inteiro e verifique se este número é
#            par ou ímpar.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# -------------------------------------------------------------
# Questão 6
# Enunciado: Escreva um programa que, dados dois números inteiros, mostre na tela o maior
#            deles, assim como a diferença existente entre ambos.
# -------------------------------------------------------------

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("Maior:", numero1)
    print("Diferença:", numero1 - numero2)
else:
    print("Maior:", numero2)
    print("Diferença:", numero2 - numero1)


# -------------------------------------------------------------
# Questão 7
# Enunciado: Faça um programa que receba dois números e mostre o maior. Se por acaso, os
#            dois números forem iguais, imprima a mensagem "Números iguais".
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior é:", numero1)
elif numero2 > numero1:
    print("O maior é:", numero2)
else:
    print("Números iguais")


# -------------------------------------------------------------
# Questão 8
# Enunciado: Faça um programa que leia 2 notas de um aluno, verifique se as notas são
#            válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
#            obrigatoriamente, um valor entre 0.0 e 10.0. Caso a nota não possua um valor
#            válido, este fato deve ser informado ao usuário e o programa termina.
# -------------------------------------------------------------

nota1 = float(input("Digite a primeira nota: "))

if nota1 < 0 or nota1 > 10:
    print("Nota inválida!")
else:
    nota2 = float(input("Digite a segunda nota: "))

    if nota2 < 0 or nota2 > 10:
        print("Nota inválida!")
    else:
        media = (nota1 + nota2) / 2
        print("Média das notas:", media)


# -------------------------------------------------------------
# Questão 9
# Enunciado: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se
#            a prestação for maior que 20% do salário imprima: "Empréstimo não
#            concedido", caso contrário imprima: "Empréstimo concedido".
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))
prestacao = float(input("Digite o valor da prestação: R$ "))

limite = salario * 0.20

if prestacao > limite:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")


# -------------------------------------------------------------
# Questão 10
# Enunciado: Faça um programa que receba a altura e o sexo de uma pessoa e calcule e
#            mostre seu peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
#            - Homens: (72.7 * h) - 58
#            - Mulheres: (62.1 * h) - 44.7
# -------------------------------------------------------------

altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal (homem):", peso_ideal)
else:
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal (mulher):", peso_ideal)


# -------------------------------------------------------------
# Questão 11
# Enunciado: Escreva um programa que leia um número inteiro maior do que zero e devolva,
#            na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251
#            corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que
#            zero, o programa terminará com a mensagem "Número inválido".
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro maior que zero: "))

if numero > 0:
    soma = 0
    while numero > 0:
        soma = soma + numero % 10   # pega o último algarismo
        numero = numero // 10       # remove o último algarismo
    print("Soma dos algarismos:", soma)
else:
    print("Número inválido")


# -------------------------------------------------------------
# Questão 12
# Enunciado: Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
#            "Número inválido". Se o número for positivo, calcular o logaritmo deste
#            número.
# -------------------------------------------------------------

# Para a raiz quadrada usamos o operador ** (elevar a 0.5), que não precisa de
# biblioteca. Já o logaritmo não tem um operador simples na linguagem, por isso
# é necessário importar a biblioteca "math" e usar a função math.log().
import math

numero = float(input("Digite um número: "))

if numero > 0:
    print("Logaritmo:", math.log(numero))
else:
    print("Número inválido")


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


# -------------------------------------------------------------
# Questão 15
# Enunciado: Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da
#            semana correspondente a este número. Isto é, domingo se 1, segunda-feira se
#            2, e assim por diante.
# -------------------------------------------------------------

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Número inválido")


# -------------------------------------------------------------
# Questão 16
# Enunciado: Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
#            correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim
#            por diante.
# -------------------------------------------------------------

mes = int(input("Digite um número de 1 a 12: "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Número inválido")


# -------------------------------------------------------------
# Questão 17
# Enunciado: Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
#            A = (baseMaior + baseMenor) * altura / 2.
#            Lembre-se: a base maior e a base menor devem ser números maiores que zero.
# -------------------------------------------------------------

base_maior = float(input("Digite a base maior: "))
base_menor = float(input("Digite a base menor: "))

if base_maior > 0 and base_menor > 0:
    altura = float(input("Digite a altura: "))
    area = (base_maior + base_menor) * altura / 2
    print("Área do trapézio:", area)
else:
    print("As bases devem ser maiores que zero.")


# -------------------------------------------------------------
# Questão 18
# Enunciado: Faça um programa que mostre ao usuário um menu com 4 opções de operações
#            matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o
#            seu programa então pede dois valores numéricos e realiza a operação,
#            mostrando o resultado e saindo.
# -------------------------------------------------------------

print("Menu de operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Escolha uma opção: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", numero1 + numero2)
elif opcao == 2:
    print("Resultado:", numero1 - numero2)
elif opcao == 3:
    print("Resultado:", numero1 * numero2)
elif opcao == 4:
    print("Resultado:", numero1 / numero2)
else:
    print("Opção inválida")


# -------------------------------------------------------------
# Questão 19
# Enunciado: Faça um programa para verificar se um determinado número inteiro é divisível
#            por 3 ou 5, mas não simultaneamente pelos dois.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

divisivel_por_3 = numero % 3 == 0
divisivel_por_5 = numero % 5 == 0

if (divisivel_por_3 or divisivel_por_5) and not (divisivel_por_3 and divisivel_por_5):
    print("O número é divisível por 3 ou por 5, mas não pelos dois.")
else:
    print("O número não atende à condição.")


# -------------------------------------------------------------
# Questão 20
# Enunciado: Dados três valores, A, B e C, verificar se eles podem ser valores dos lados
#            de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou
#            isóscele, considerando:
#            - O comprimento de cada lado de um triângulo é menor do que a soma dos
#              outros dois lados.
#            - Equilátero: três lados iguais.
#            - Isóscele: dois lados iguais.
#            - Escaleno: os três lados diferentes.
# -------------------------------------------------------------

ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado C: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print("É um triângulo.")

    if ladoA == ladoB and ladoB == ladoC:
        print("Triângulo equilátero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triângulo isóscele.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")


# -------------------------------------------------------------
# Questão 21
# Enunciado: Escreva o menu de opções abaixo. Leia a opção do usuário e execute a
#            operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
#            Escolha a opção:
#            1- Soma de 2 números.
#            2- Diferença entre 2 números (maior pelo menor).
#            3- Produto entre 2 números.
#            4- Divisão entre 2 números (o denominador não pode ser zero).
# -------------------------------------------------------------

print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números (maior pelo menor)")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números")
opcao = int(input("Opção: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", numero1 + numero2)
elif opcao == 2:
    if numero1 > numero2:
        print("Resultado:", numero1 - numero2)
    else:
        print("Resultado:", numero2 - numero1)
elif opcao == 3:
    print("Resultado:", numero1 * numero2)
elif opcao == 4:
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida")


# -------------------------------------------------------------
# Questão 22
# Enunciado: Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou
#            não se aposentar. As condições para aposentadoria são:
#            - Ter pelo menos 65 anos;
#            - Ou ter trabalhado pelo menos 30 anos;
#            - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
# -------------------------------------------------------------

idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço (anos): "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")


# -------------------------------------------------------------
# Questão 23
# Enunciado: Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
#            se for divisível por 400 ou se for divisível por 4 e não for divisível por
#            100. Por exemplo: 1988, 1992, 1996.
# -------------------------------------------------------------

ano = int(input("Digite um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")


# -------------------------------------------------------------
# Questão 24
# Enunciado: Uma empresa vende o mesmo produto para quatro diferentes estados. Cada
#            estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%;
#            RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o
#            estado destino do produto e o programa retorne o preço final do produto
#            acrescido do imposto do estado em que ele será vendido. Se o estado digitado
#            não for válido, mostrar uma mensagem de erro.
# -------------------------------------------------------------

valor = float(input("Digite o valor do produto: R$ "))
estado = input("Digite o estado destino (MG, SP, RJ, MS): ")

if estado == "MG":
    preco_final = valor + valor * 0.07
    print("Preço final em MG: R$", preco_final)
elif estado == "SP":
    preco_final = valor + valor * 0.12
    print("Preço final em SP: R$", preco_final)
elif estado == "RJ":
    preco_final = valor + valor * 0.15
    print("Preço final no RJ: R$", preco_final)
elif estado == "MS":
    preco_final = valor + valor * 0.08
    print("Preço final no MS: R$", preco_final)
else:
    print("Estado inválido!")


# -------------------------------------------------------------
# Questão 25
# Enunciado: Calcule as raízes da equação de 2º grau. Lembrando que x = (-b ± raiz(Δ)) /
#            2a, onde Δ = b² - 4ac, e ax² + bx + c = 0.
#            A variável a tem que ser diferente de zero. Caso seja igual, imprima a
#            mensagem "Não é equação de segundo grau".
#            - Se Δ < 0, não existe raiz real. Imprima "Não existe raiz".
#            - Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única".
#            - Se Δ > 0, imprima as duas raízes reais.
# -------------------------------------------------------------

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação de segundo grau")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        raiz = -b / (2 * a)
        print("Raiz única:", raiz)
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print("Raiz 1:", raiz1)
        print("Raiz 2:", raiz2)


# -------------------------------------------------------------
# Questão 26
# Enunciado: Leia a distância em Km e a quantidade de litros de gasolina consumidos por um
#            carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
#            acordo com a tabela abaixo:
#            - menor que 8 Km/l -> "Venda o carro!"
#            - entre 8 e 14 Km/l -> "Econômico!"
#            - maior que 14 Km/l -> "Super econômico!"
# -------------------------------------------------------------

distancia = float(input("Digite a distância percorrida (Km): "))
litros = float(input("Digite a quantidade de litros consumidos: "))

consumo = distancia / litros
print("Consumo:", consumo, "Km/l")

if consumo < 8:
    print("Venda o carro!")
elif consumo <= 14:
    print("Econômico!")
else:
    print("Super econômico!")


# -------------------------------------------------------------
# Questão 27
# Enunciado: Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
#            seguintes categorias:
#            - Infantil A: 5 a 7
#            - Infantil B: 8 a 10
#            - Juvenil A: 11 a 13
#            - Juvenil B: 14 a 17
#            - Sênior: maiores de 18 anos
# -------------------------------------------------------------

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Sênior")
else:
    print("Idade fora das categorias.")


# -------------------------------------------------------------
# Questão 28
# Enunciado: Faça um programa que leia três números inteiros positivos e efetue o cálculo
#            de uma das seguintes médias de acordo com um valor numérico digitado pelo
#            usuário:
#            (1) Geométrica: raiz cúbica de x * y * z
#            (2) Ponderada: (x + 2*y + 3*z) / 6
#            (3) Harmônica: 3 / (1/x + 1/y + 1/z)
#            (4) Aritmética: (x + y + z) / 3
# -------------------------------------------------------------

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

print("1 - Geométrica")
print("2 - Ponderada")
print("3 - Harmônica")
print("4 - Aritmética")
opcao = int(input("Escolha o tipo de média: "))

if opcao == 1:
    media = (x * y * z) ** (1 / 3)
    print("Média geométrica:", media)
elif opcao == 2:
    media = (x + 2 * y + 3 * z) / 6
    print("Média ponderada:", media)
elif opcao == 3:
    media = 3 / (1 / x + 1 / y + 1 / z)
    print("Média harmônica:", media)
elif opcao == 4:
    media = (x + y + z) / 3
    print("Média aritmética:", media)
else:
    print("Opção inválida")


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


# -------------------------------------------------------------
# Questão 30
# Enunciado: Faça um programa que receba três números e mostre-os em ordem crescente.
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero1 > numero3:
    numero1, numero3 = numero3, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Ordem crescente:", numero1, numero2, numero3)


# -------------------------------------------------------------
# Questão 31
# Enunciado: Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a
#            tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
#            Altura           Peso Até 60 | Entre 60 e 90 | Acima de 90
#            Menor que 1,20        A             D             G
#            De 1,20 a 1,70        B             E             H
#            Maior que 1,70        C             F             I
# -------------------------------------------------------------

altura = float(input("Digite a altura (em metros): "))
peso = float(input("Digite o peso (em kg): "))

if altura < 1.20:
    if peso <= 60:
        classificacao = "A"
    elif peso <= 90:
        classificacao = "D"
    else:
        classificacao = "G"
elif altura <= 1.70:
    if peso <= 60:
        classificacao = "B"
    elif peso <= 90:
        classificacao = "E"
    else:
        classificacao = "H"
else:
    if peso <= 60:
        classificacao = "C"
    elif peso <= 90:
        classificacao = "F"
    else:
        classificacao = "I"

print("Classificação:", classificacao)


# -------------------------------------------------------------
# Questão 32
# Enunciado: Escrever um programa que leia o código do produto escolhido do cardápio de uma
#            lanchonete e a quantidade. O programa deve calcular o valor a ser pago por
#            aquele lanche. O cardápio segue o padrão abaixo:
#            100 - Cachorro Quente  - 1.20
#            101 - Bauru Simples    - 1.30
#            102 - Bauru com Ovo    - 1.50
#            103 - Hamburguer       - 1.20
#            104 - Cheeseburguer    - 1.70
#            105 - Suco             - 2.20
#            106 - Refrigerante     - 1.00
# -------------------------------------------------------------

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if codigo == 100:
    preco = 1.20
elif codigo == 101:
    preco = 1.30
elif codigo == 102:
    preco = 1.50
elif codigo == 103:
    preco = 1.20
elif codigo == 104:
    preco = 1.70
elif codigo == 105:
    preco = 2.20
elif codigo == 106:
    preco = 1.00
else:
    preco = 0
    print("Código inválido!")

if preco > 0:
    total = preco * quantidade
    print("Valor a pagar: R$", total)


# -------------------------------------------------------------
# Questão 33
# Enunciado: Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço
#            antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do
#            preço novo (de acordo com a segunda tabela).
#            Preço antigo -> percentual de aumento:
#            - até R$ 50 -> 5%
#            - entre R$ 50 e R$ 100 -> 10%
#            - acima de R$ 100 -> 15%
#            Preço novo -> mensagem:
#            - até R$ 80 -> Barato
#            - entre R$ 80 e R$ 120 (inclusive) -> Normal
#            - entre R$ 120 e R$ 200 (inclusive) -> Caro
#            - acima de R$ 200 -> Muito caro
# -------------------------------------------------------------

preco_antigo = float(input("Digite o preço antigo: R$ "))

if preco_antigo <= 50:
    preco_novo = preco_antigo + preco_antigo * 0.05
elif preco_antigo <= 100:
    preco_novo = preco_antigo + preco_antigo * 0.10
else:
    preco_novo = preco_antigo + preco_antigo * 0.15

print("Preço novo: R$", preco_novo)

if preco_novo <= 80:
    print("Barato")
elif preco_novo <= 120:
    print("Normal")
elif preco_novo <= 200:
    print("Caro")
else:
    print("Muito caro")


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


# -------------------------------------------------------------
# Questão 36
# Enunciado: Escreva um programa que, dado o valor da venda, imprima a comissão que
#            deverá ser paga ao vendedor. Considere a tabela:
#            Venda mensal                                  | Comissão
#            Maior ou igual a R$100.000,00                 | R$700,00 + 16%
#            Menor que R$100.000,00 e >= R$80.000,00       | R$650,00 + 14%
#            Menor que R$80.000,00 e >= R$60.000,00        | R$600,00 + 14%
#            Menor que R$60.000,00 e >= R$40.000,00        | R$550,00 + 14%
#            Menor que R$40.000,00 e >= R$20.000,00        | R$500,00 + 14%
#            Menor que R$20.000,00                         | R$400,00 + 14%
# -------------------------------------------------------------

venda = float(input("Digite o valor da venda: R$ "))

if venda >= 100000:
    comissao = 700 + venda * 0.16
elif venda >= 80000:
    comissao = 650 + venda * 0.14
elif venda >= 60000:
    comissao = 600 + venda * 0.14
elif venda >= 40000:
    comissao = 550 + venda * 0.14
elif venda >= 20000:
    comissao = 500 + venda * 0.14
else:
    comissao = 400 + venda * 0.14

print("Comissão: R$", comissao)


# -------------------------------------------------------------
# Questão 37
# Enunciado: As tarifas de certo parque de estacionamento são as seguintes:
#            - 1ª e 2ª hora - R$ 1,00 cada
#            - 3ª e 4ª hora - R$ 1,40 cada
#            - 5ª hora e seguintes - R$ 2,00 cada
#            O número de horas a pagar é sempre inteiro e arredondado por excesso. Os
#            momentos de chegada e partida são dados por pares de inteiros (hora e
#            minuto). Se a hora de chegada for maior que a de partida, a partida ocorreu
#            no dia seguinte.
# -------------------------------------------------------------

hora_chegada = int(input("Hora de chegada: "))
minuto_chegada = int(input("Minuto de chegada: "))
hora_partida = int(input("Hora de partida: "))
minuto_partida = int(input("Minuto de partida: "))

total_chegada = hora_chegada * 60 + minuto_chegada
total_partida = hora_partida * 60 + minuto_partida

if total_partida < total_chegada:
    total_partida = total_partida + 24 * 60

minutos = total_partida - total_chegada

# Arredonda as horas para cima (por excesso)
horas = minutos // 60
if minutos % 60 != 0:
    horas = horas + 1

if horas <= 2:
    preco = horas * 1.00
elif horas <= 4:
    preco = 2 * 1.00 + (horas - 2) * 1.40
else:
    preco = 2 * 1.00 + 2 * 1.40 + (horas - 4) * 2.00

print("Horas pagas:", horas)
print("Preço cobrado: R$", preco)


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


# -------------------------------------------------------------
# Questão 39
# Enunciado: Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
#            tabela que considera o salário atual e o tempo de serviço. Leia o salário e o
#            tempo de serviço (anos) e imprima o salário reajustado, ou uma mensagem caso
#            o funcionário não tenha direito a nenhum aumento.
#            Salário Atual -> Reajuste:      Tempo de Serviço -> Bônus:
#            até 500,00     -> 25%           abaixo de 1 ano   -> sem bônus
#            até 1000,00    -> 20%           de 1 a 3 anos     -> 100,00
#            até 1500,00    -> 15%           de 4 a 6 anos     -> 200,00
#            até 2000,00    -> 10%           de 7 a 10 anos    -> 300,00
#            acima de 2000,00 -> sem reajuste mais de 10 anos -> 500,00
# -------------------------------------------------------------

salario = float(input("Digite o salário atual: R$ "))
tempo = int(input("Digite o tempo de serviço (anos): "))

if salario <= 500:
    reajuste = 0.25
elif salario <= 1000:
    reajuste = 0.20
elif salario <= 1500:
    reajuste = 0.15
elif salario <= 2000:
    reajuste = 0.10
else:
    reajuste = 0

if tempo < 1:
    bonus = 0
elif tempo <= 3:
    bonus = 100.00
elif tempo <= 6:
    bonus = 200.00
elif tempo <= 10:
    bonus = 300.00
else:
    bonus = 500.00

if reajuste == 0:
    print("O funcionário não tem direito a reajuste.")
else:
    salario_final = salario + salario * reajuste + bonus
    print("Salário final reajustado: R$", salario_final)


# -------------------------------------------------------------
# Questão 40
# Enunciado: O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
#            comissão do distribuidor e dos impostos. A comissão e os impostos são
#            calculados sobre o custo de fábrica, conforme a tabela:
#            Custo de fábrica          | % Distribuidor | % Impostos
#            até R$12.000,00           |      5         | isento
#            entre R$12.000,00 e 25.000,00 |   10        | 15
#            acima de R$25.000,00      |     15         | 20
#            Leia o custo de fábrica e escreva o custo ao consumidor.
# -------------------------------------------------------------

custo_fabrica = float(input("Digite o custo de fábrica: R$ "))

if custo_fabrica <= 12000:
    percentual_distribuidor = 0.05
    percentual_impostos = 0
elif custo_fabrica <= 25000:
    percentual_distribuidor = 0.10
    percentual_impostos = 0.15
else:
    percentual_distribuidor = 0.15
    percentual_impostos = 0.20

comissao = custo_fabrica * percentual_distribuidor
impostos = custo_fabrica * percentual_impostos
custo_consumidor = custo_fabrica + comissao + impostos

print("Custo ao consumidor: R$", custo_consumidor)


# -------------------------------------------------------------
# Questão 41
# Enunciado: Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação
#            de acordo com a tabela abaixo:
#            IMC            | Classificação
#            < 18,5         | Abaixo do Peso
#            18,6 - 24,9    | Saudável
#            25,0 - 29,9    | Peso em excesso
#            30,0 - 34,9    | Obesidade Grau I
#            35,0 - 39,9    | Obesidade Grau II (severa)
#            >= 40,0        | Obesidade Grau III (mórbida)
# -------------------------------------------------------------

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)
print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Peso em excesso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
