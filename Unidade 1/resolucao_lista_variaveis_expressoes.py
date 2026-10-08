# ==============================================================
# RESOLUÇÃO - LISTA DE EXERCÍCIOS: VARIÁVEIS E EXPRESSÕES
# Disciplina: Introdução à Programação 
# ==============================================================
# Observações:
# - int(input(...)) lê um número inteiro.
# - float(input(...)) lê um número decimal.
# - input(...) lê um texto (string).
# - print(...) mostra o resultado na tela.
# - ** é potência (ex.: 5 ** 2 = 25).
# ==============================================================


# -------------------------------------------------------------
# Questão 1
# Enunciado: Faça um programa que leia um número inteiro e o imprima.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))
print("Número digitado:", numero)


# -------------------------------------------------------------
# Questão 2
# Enunciado: Faça um programa que leia um número real e o imprima.
# -------------------------------------------------------------

numero = float(input("Digite um número real: "))
print("Número digitado:", numero)


# -------------------------------------------------------------
# Questão 3
# Enunciado: Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
# -------------------------------------------------------------

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

soma = valor1 + valor2 + valor3
print("A soma dos três valores é:", soma)


# -------------------------------------------------------------
# Questão 4
# Enunciado: Leia um número real e imprima o resultado do quadrado desse número.
# -------------------------------------------------------------

numero = float(input("Digite um número real: "))
quadrado = numero ** 2
print("O quadrado do número é:", quadrado)


# -------------------------------------------------------------
# Questão 5
# Enunciado: Leia um número real e imprima a quinta parte deste número.
# -------------------------------------------------------------

numero = float(input("Digite um número real: "))
quinta_parte = numero / 5
print("A quinta parte do número é:", quinta_parte)


# -------------------------------------------------------------
# Questão 6
# Enunciado: Leia uma temperatura em graus Celsius e apresente-a convertida em graus
#            Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0.
# -------------------------------------------------------------

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * (9.0 / 5.0) + 32.0
print("Temperatura em Fahrenheit:", fahrenheit)


# -------------------------------------------------------------
# Questão 7
# Enunciado: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
#            Celsius. A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0.
# -------------------------------------------------------------

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print("Temperatura em Celsius:", celsius)


# -------------------------------------------------------------
# Questão 8
# Enunciado: Leia uma temperatura em graus Kelvin e apresente-a convertida em graus
#            Celsius. A fórmula de conversão é: C = K - 273.15.
# -------------------------------------------------------------

kelvin = float(input("Digite a temperatura em Kelvin: "))
celsius = kelvin - 273.15
print("Temperatura em Celsius:", celsius)


# -------------------------------------------------------------
# Questão 9
# Enunciado: Leia uma temperatura em graus Celsius e apresente-a convertida em graus
#            Kelvin. A fórmula de conversão é: K = C + 273.15.
# -------------------------------------------------------------

celsius = float(input("Digite a temperatura em Celsius: "))
kelvin = celsius + 273.15
print("Temperatura em Kelvin:", kelvin)


# -------------------------------------------------------------
# Questão 10
# Enunciado: Leia uma velocidade em km/h e apresente-a convertida em m/s.
#            A fórmula de conversão é: M = K / 3.6.
# -------------------------------------------------------------

kmh = float(input("Digite a velocidade em km/h: "))
ms = kmh / 3.6
print("Velocidade em m/s:", ms)


# -------------------------------------------------------------
# Questão 11
# Enunciado: Leia uma velocidade em m/s e apresente-a convertida em km/h.
#            A fórmula de conversão é: K = M * 3.6.
# -------------------------------------------------------------

ms = float(input("Digite a velocidade em m/s: "))
kmh = ms * 3.6
print("Velocidade em km/h:", kmh)


# -------------------------------------------------------------
# Questão 12
# Enunciado: Leia uma distância em milhas e apresente-a convertida em quilômetros.
#            A fórmula de conversão é: K = 1.61 * M.
# -------------------------------------------------------------

milhas = float(input("Digite a distância em milhas: "))
quilometros = 1.61 * milhas
print("Distância em quilômetros:", quilometros)


# -------------------------------------------------------------
# Questão 13
# Enunciado: Leia uma distância em quilômetros e apresente-a convertida em milhas.
#            A fórmula de conversão é: M = K / 1.61.
# -------------------------------------------------------------

quilometros = float(input("Digite a distância em quilômetros: "))
milhas = quilometros / 1.61
print("Distância em milhas:", milhas)


# -------------------------------------------------------------
# Questão 14
# Enunciado: Leia um ângulo em graus e apresente-o convertido em radianos.
#            A fórmula de conversão é: R = G * 3.14 / 180.
# -------------------------------------------------------------

graus = float(input("Digite o ângulo em graus: "))
radianos = graus * 3.14 / 180
print("Ângulo em radianos:", radianos)


# -------------------------------------------------------------
# Questão 15
# Enunciado: Leia um ângulo em radianos e apresente-o convertido em graus.
#            A fórmula de conversão é: G = R * 180 / 3.14.
# -------------------------------------------------------------

radianos = float(input("Digite o ângulo em radianos: "))
graus = radianos * 180 / 3.14
print("Ângulo em graus:", graus)


# -------------------------------------------------------------
# Questão 16
# Enunciado: Leia um comprimento em polegadas e apresente-o convertido em centímetros.
#            A fórmula de conversão é: C = P * 2.54.
# -------------------------------------------------------------

polegadas = float(input("Digite o comprimento em polegadas: "))
centimetros = polegadas * 2.54
print("Comprimento em centímetros:", centimetros)


# -------------------------------------------------------------
# Questão 17
# Enunciado: Leia um comprimento em centímetros e apresente-o convertido em polegadas.
#            A fórmula de conversão é: P = C / 2.54.
# -------------------------------------------------------------

centimetros = float(input("Digite o comprimento em centímetros: "))
polegadas = centimetros / 2.54
print("Comprimento em polegadas:", polegadas)


# -------------------------------------------------------------
# Questão 18
# Enunciado: Leia um volume em metros cúbicos (m3) e apresente-o convertido em litros.
#            A fórmula de conversão é: L = 1000 * M.
# -------------------------------------------------------------

metros_cubicos = float(input("Digite o volume em metros cúbicos: "))
litros = 1000 * metros_cubicos
print("Volume em litros:", litros)


# -------------------------------------------------------------
# Questão 19
# Enunciado: Leia um volume em litros e apresente-o convertido em metros cúbicos (m3).
#            A fórmula de conversão é: M = L / 1000.
# -------------------------------------------------------------

litros = float(input("Digite o volume em litros: "))
metros_cubicos = litros / 1000
print("Volume em metros cúbicos:", metros_cubicos)


# -------------------------------------------------------------
# Questão 20
# Enunciado: Leia uma massa em quilogramas e apresente-a convertida em libras.
#            A fórmula de conversão é: L = K / 0.45.
# -------------------------------------------------------------

quilogramas = float(input("Digite a massa em quilogramas: "))
libras = quilogramas / 0.45
print("Massa em libras:", libras)


# -------------------------------------------------------------
# Questão 21
# Enunciado: Leia uma massa em libras e apresente-a convertida em quilogramas.
#            A fórmula de conversão é: K = L * 0.45.
# -------------------------------------------------------------

libras = float(input("Digite a massa em libras: "))
quilogramas = libras * 0.45
print("Massa em quilogramas:", quilogramas)


# -------------------------------------------------------------
# Questão 22
# Enunciado: Leia um comprimento em jardas e apresente-o convertido em metros.
#            A fórmula de conversão é: M = 0.91 * J.
# -------------------------------------------------------------

jardas = float(input("Digite o comprimento em jardas: "))
metros = 0.91 * jardas
print("Comprimento em metros:", metros)


# -------------------------------------------------------------
# Questão 23
# Enunciado: Leia um comprimento em metros e apresente-o convertido em jardas.
#            A fórmula de conversão é: J = M / 0.91.
# -------------------------------------------------------------

metros = float(input("Digite o comprimento em metros: "))
jardas = metros / 0.91
print("Comprimento em jardas:", jardas)


# -------------------------------------------------------------
# Questão 24
# Enunciado: Leia uma área em metros quadrados (m2) e apresente-a convertida em acres.
#            A fórmula de conversão é: A = M * 0.000247.
# -------------------------------------------------------------

metros_quadrados = float(input("Digite a área em metros quadrados: "))
acres = metros_quadrados * 0.000247
print("Área em acres:", acres)


# -------------------------------------------------------------
# Questão 25
# Enunciado: Leia uma área em acres e apresente-a convertida em metros quadrados (m2).
#            A fórmula de conversão é: M = A * 4048.58.
# -------------------------------------------------------------

acres = float(input("Digite a área em acres: "))
metros_quadrados = acres * 4048.58
print("Área em metros quadrados:", metros_quadrados)


# -------------------------------------------------------------
# Questão 26
# Enunciado: Leia uma área em metros quadrados (m2) e apresente-a convertida em hectares.
#            A fórmula de conversão é: H = M * 0.0001.
# -------------------------------------------------------------

metros_quadrados = float(input("Digite a área em metros quadrados: "))
hectares = metros_quadrados * 0.0001
print("Área em hectares:", hectares)


# -------------------------------------------------------------
# Questão 27
# Enunciado: Leia uma área em hectares e apresente-a convertida em metros quadrados (m2).
#            A fórmula de conversão é: M = H * 10000.
# -------------------------------------------------------------

hectares = float(input("Digite a área em hectares: "))
metros_quadrados = hectares * 10000
print("Área em metros quadrados:", metros_quadrados)


# -------------------------------------------------------------
# Questão 28
# Enunciado: Faça a leitura de três valores e apresente como resultado a soma dos
#            quadrados dos três valores lidos.
# -------------------------------------------------------------

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

soma_dos_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2
print("Soma dos quadrados:", soma_dos_quadrados)


# -------------------------------------------------------------
# Questão 29
# Enunciado: Leia quatro notas, calcule a média aritmética e imprima o resultado.
# -------------------------------------------------------------

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print("Média aritmética:", media)


# -------------------------------------------------------------
# Questão 30
# Enunciado: Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor
#            correspondente em dólares.
# -------------------------------------------------------------

valor_reais = float(input("Digite o valor em reais: R$ "))
cotacao_dolar = float(input("Digite a cotação do dólar: R$ "))

valor_dolares = valor_reais / cotacao_dolar
print("Valor em dólares: US$", valor_dolares)


# -------------------------------------------------------------
# Questão 31
# Enunciado: Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))
print("Antecessor:", numero - 1)
print("Sucessor:", numero + 1)


# -------------------------------------------------------------
# Questão 32
# Enunciado: Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
#            antecessor de seu dobro.
# -------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

sucessor_do_triplo = numero * 3 + 1
antecessor_do_dobro = numero * 2 - 1
resultado = sucessor_do_triplo + antecessor_do_dobro

print("Resultado:", resultado)


# -------------------------------------------------------------
# Questão 33
# Enunciado: Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
# -------------------------------------------------------------

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
print("Área do quadrado:", area)


# -------------------------------------------------------------
# Questão 34
# Enunciado: Leia o valor do raio de um círculo e calcule e imprima a área do círculo
#            correspondente. A área do círculo é PI * raio², considere PI = 3.141592.
# -------------------------------------------------------------

raio = float(input("Digite o raio do círculo: "))
area = 3.141592 * raio ** 2
print("Área do círculo:", area)


# -------------------------------------------------------------
# Questão 35
# Enunciado: Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela
#            equação: hipotenusa = raiz(a² + b²). Faça um programa que receba os valores
#            de a e b e calcule o valor da hipotenusa através da equação.
# -------------------------------------------------------------

import math

a = float(input("Digite o cateto a: "))
b = float(input("Digite o cateto b: "))

hipotenusa = math.sqrt(a ** 2 + b ** 2)
print("Hipotenusa:", hipotenusa)


# -------------------------------------------------------------
# Questão 36
# Enunciado: Leia a altura e o raio de um cilindro circular e imprima o volume do
#            cilindro. A fórmula é: V = PI * raio² * altura, onde PI = 3.141592.
# -------------------------------------------------------------

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = 3.141592 * raio ** 2 * altura
print("Volume do cilindro:", volume)


# -------------------------------------------------------------
# Questão 37
# Enunciado: Faça um programa que leia o valor de um produto e imprima o valor com
#            desconto, tendo em vista que o desconto foi de 12%.
# -------------------------------------------------------------

valor_produto = float(input("Digite o valor do produto: R$ "))
valor_com_desconto = valor_produto - valor_produto * 0.12
print("Valor com desconto: R$", valor_com_desconto)


# -------------------------------------------------------------
# Questão 38
# Enunciado: Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
#            sabendo que ele recebeu um aumento de 25%.
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))
novo_salario = salario + salario * 0.25
print("Novo salário: R$", novo_salario)


# -------------------------------------------------------------
# Questão 39
# Enunciado: A importância de R$ 780.000,00 será dividida entre três ganhadores de um
#            concurso. Sendo que da quantia total:
#            - O primeiro ganhador receberá 46%;
#            - O segundo receberá 32%;
#            - O terceiro receberá o restante.
#            Calcule e imprima a quantia ganha por cada um dos ganhadores.
# -------------------------------------------------------------

importancia = 780000.00

primeiro = importancia * 0.46
segundo = importancia * 0.32
terceiro = importancia - primeiro - segundo

print("Primeiro ganhador: R$", primeiro)
print("Segundo ganhador: R$", segundo)
print("Terceiro ganhador: R$", terceiro)


# -------------------------------------------------------------
# Questão 40
# Enunciado: Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
#            solicite o número de dias trabalhados pelo encanador e imprima a quantia
#            líquida que deverá ser paga, sabendo-se que são descontados 8% para
#            imposto de renda.
# -------------------------------------------------------------

dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

valor_bruto = dias_trabalhados * 30.00
imposto = valor_bruto * 0.08
valor_liquido = valor_bruto - imposto

print("Valor líquido a receber: R$", valor_liquido)


# -------------------------------------------------------------
# Questão 41
# Enunciado: Faça um programa que leia o valor da hora de trabalho (em reais) e o número
#            de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário,
#            adicionando 10% sobre o valor calculado.
# -------------------------------------------------------------

valor_hora = float(input("Digite o valor da hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

valor = valor_hora * horas_trabalhadas
valor_com_aumento = valor + valor * 0.10

print("Valor a ser pago: R$", valor_com_aumento)


# -------------------------------------------------------------
# Questão 42
# Enunciado: Receba o salário-base de um funcionário. Calcule e imprima o salário a
#            receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o
#            salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
# -------------------------------------------------------------

salario_base = float(input("Digite o salário-base: R$ "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_a_receber = salario_base + gratificacao - imposto

print("Salário a receber: R$", salario_a_receber)


# -------------------------------------------------------------
# Questão 43
# Enunciado: Escreva um programa de ajuda para vendedores. A partir de um valor total
#            lido, mostre:
#            - o total a pagar com desconto de 10%;
#            - o valor de cada parcela, no parcelamento de 3x sem juros;
#            - a comissão do vendedor, no caso da venda ser à vista
#              (5% sobre o valor com desconto);
#            - a comissão do vendedor, no caso da venda ser parcelada
#              (5% sobre o valor total).
# -------------------------------------------------------------

valor_total = float(input("Digite o valor total da venda: R$ "))

total_com_desconto = valor_total - valor_total * 0.10
valor_parcela = valor_total / 3
comissao_a_vista = total_com_desconto * 0.05
comissao_parcelada = valor_total * 0.05

print("Total a pagar com desconto: R$", total_com_desconto)
print("Valor de cada parcela (3x): R$", valor_parcela)
print("Comissão à vista: R$", comissao_a_vista)
print("Comissão parcelada: R$", comissao_parcelada)


# -------------------------------------------------------------
# Questão 44
# Enunciado: Receba a altura do degrau de uma escada e a altura que o usuário deseja
#            alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá
#            subir para atingir seu objetivo.
# -------------------------------------------------------------

import math

altura_degrau = float(input("Digite a altura do degrau: "))
altura_objetivo = float(input("Digite a altura a ser alcançada: "))

quantidade_degraus = math.ceil(altura_objetivo / altura_degrau)
print("Quantidade de degraus a subir:", quantidade_degraus)


# -------------------------------------------------------------
# Questão 45
# Enunciado: Faça um programa que leia um número inteiro positivo de três dígitos
#            (de 100 a 999). Gere outro número formado pelos dígitos invertidos do
#            número lido. Exemplo: NúmeroLido = 123 -> NúmeroGerado = 321.
# -------------------------------------------------------------

numero = int(input("Digite um número de três dígitos (100 a 999): "))

centena = numero // 100
dezena = (numero // 10) % 10
unidade = numero % 10

invertido = unidade * 100 + dezena * 10 + centena
print("Número invertido:", invertido)


# -------------------------------------------------------------
# Questão 46
# Enunciado: Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito
#            por linha.
# -------------------------------------------------------------

numero = int(input("Digite um número de quatro dígitos (1000 a 9999): "))

milhar = numero // 1000
centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)


# -------------------------------------------------------------
# Questão 47
# Enunciado: Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.
# -------------------------------------------------------------

total_segundos = int(input("Digite o total de segundos: "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)


# -------------------------------------------------------------
# Questão 48
# Enunciado: Faça um programa para ler o horário (hora, minuto e segundo) de início e a
#            duração, em segundos, de uma experiência biológica. O programa deve resultar
#            com o novo horário (hora, minuto e segundo) do término da mesma.
# -------------------------------------------------------------

hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))
segundo_inicio = int(input("Digite o segundo de início: "))
duracao = int(input("Digite a duração em segundos: "))

total_segundos = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + duracao

hora_termino = (total_segundos // 3600) % 24
minuto_termino = (total_segundos % 3600) // 60
segundo_termino = total_segundos % 60

print("Horário de término:", hora_termino, ":", minuto_termino, ":", segundo_termino)


# -------------------------------------------------------------
# Questão 49
# Enunciado: Implemente um programa que calcule o ano de nascimento de uma pessoa a
#            partir de sua idade e do ano atual.
# -------------------------------------------------------------

idade = int(input("Digite a idade: "))
ano_atual = int(input("Digite o ano atual: "))

ano_nascimento = ano_atual - idade
print("Ano de nascimento:", ano_nascimento)


# -------------------------------------------------------------
# Questão 50
# Enunciado: Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule
#            sua distância da origem (0, 0).
# -------------------------------------------------------------

import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

distancia = math.sqrt(x ** 2 + y ** 2)
print("Distância da origem:", distancia)


# -------------------------------------------------------------
# Questão 51
# Enunciado: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser
#            repartido proporcionalmente ao valor que cada um deu para a realização da
#            aposta. Faça um programa que leia quanto cada apostador investiu, o valor do
#            prêmio, e imprima quanto cada um ganharia do prêmio com base no valor
#            investido.
# -------------------------------------------------------------

investimento1 = float(input("Digite o valor investido pelo apostador 1: R$ "))
investimento2 = float(input("Digite o valor investido pelo apostador 2: R$ "))
investimento3 = float(input("Digite o valor investido pelo apostador 3: R$ "))
premio = float(input("Digite o valor do prêmio: R$ "))

total_investido = investimento1 + investimento2 + investimento3

parte1 = premio * (investimento1 / total_investido)
parte2 = premio * (investimento2 / total_investido)
parte3 = premio * (investimento3 / total_investido)

print("Apostador 1 recebe: R$", parte1)
print("Apostador 2 recebe: R$", parte2)
print("Apostador 3 recebe: R$", parte3)


# -------------------------------------------------------------
# Questão 52
# Enunciado: Faça um programa para ler as dimensões de um terreno (comprimento c e
#            largura l), bem como o preço do metro de tela p. Imprima o custo para cercar
#            este mesmo terreno com tela.
# -------------------------------------------------------------

comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
preco_metro = float(input("Digite o preço do metro de tela: R$ "))

perimetro = 2 * (comprimento + largura)
custo = perimetro * preco_metro

print("Custo para cercar o terreno: R$", custo)
