# ==============================================================
# RESOLUÇÃO - LISTA DE EXERCÍCIOS 2
# Disciplina: Introdução à Programação 
# ==============================================================
# Observações:
# - Estrutura condicional: if / elif / else
# - if: SE a condição for verdadeira
# - elif: SENÃO SE (outra condição)
# - else: SENÃO (nenhuma condição anterior deu verdadeira)
# ==============================================================


# -------------------------------------------------------------
# Questão 1
# Enunciado: Faça um algoritmo que leia um número N e imprima "F1", "F2" ou "F3",
#            conforme a condição:
#            - "F1", se N menor ou igual 10
#            - "F2", se N maior 10 e N menor ou igual 100
#            - "F3", se N maior 100
# -------------------------------------------------------------

numero = int(input("Digite um número: "))

if numero <= 10:
    print("F1")
elif numero > 10 and numero <= 100:
    print("F2")
else:
    print("F3")


# -------------------------------------------------------------
# Questão 2
# Enunciado: Um usuário deseja um algoritmo pelo qual possa escolher que tipo de
#            média deseja calcular a partir de três notas. Faça um algoritmo que
#            leia as notas, a opção escolhida pelo usuário e calcule a média:
#            - Aritmética
#            - Ponderada (pesos 3, 3 e 4)
# -------------------------------------------------------------

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("Escolha o tipo de média:")
print("1 - Aritmética")
print("2 - Ponderada (pesos 3, 3 e 4)")
opcao = int(input("Opção: "))

if opcao == 1:
    media = (nota1 + nota2 + nota3) / 3
    print("Média aritmética:", media)
elif opcao == 2:
    media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
    print("Média ponderada:", media)
else:
    print("Opção inválida!")


# -------------------------------------------------------------
# Questão 3
# Enunciado: Construa um algoritmo que receba como entrada três valores
#            e os imprima em ordem crescente.
# -------------------------------------------------------------

numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
numero3 = float(input("Digite o terceiro valor: "))

# Comparações para colocar em ordem (do menor para o maior).
# A linha abaixo troca os valores de lugar se a condição for verdadeira.
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

if numero1 > numero3:
    numero1, numero3 = numero3, numero1

if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Em ordem crescente:", numero1, numero2, numero3)


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


# -------------------------------------------------------------
# Questão 5
# Enunciado: Uma empresa de vendas tem três corretores. A empresa paga ao corretor
#            uma comissão calculada de acordo com o valor de suas vendas.
#            Se o valor da venda de um corretor for maior que R$ 50.000,00 a
#            comissão será de 12% do valor vendido.
#            Se o valor da venda do corretor estiver entre R$ 30.000,00 e
#            R$ 50.000,00 (incluindo extremos) a comissão será de 9,5%.
#            Em qualquer outro caso, a comissão será de 7%.
#            Escreva um algoritmo que gere um relatório contendo nome, valor da
#            venda e comissão de cada um dos corretores. O relatório deve mostrar
#            também o total de vendas da empresa.
# -------------------------------------------------------------

total_vendas = 0

# O laço for repete as instruções 3 vezes (um para cada corretor)
for contador in range(3):
    print("----- Corretor", contador + 1, "-----")
    nome = input("Digite o nome do corretor: ")
    valor_venda = float(input("Digite o valor das vendas: R$ "))

    if valor_venda > 50000:
        comissao = valor_venda * 0.12
    elif valor_venda >= 30000:
        comissao = valor_venda * 0.095
    else:
        comissao = valor_venda * 0.07

    total_vendas = total_vendas + valor_venda

    print("Nome:", nome)
    print("Valor da venda: R$", valor_venda)
    print("Comissão: R$", comissao)

print("----- RELATÓRIO DA EMPRESA -----")
print("Total de vendas: R$", total_vendas)


# -------------------------------------------------------------
# Questão 6
# Enunciado: Uma empresa produz três tipos de peças mecânicas: parafusos, porcas e
#            arruelas. Têm-se os preços unitários de cada tipo de peça e sabe-se
#            que sobre estes preços incidem descontos de 10% para porcas,
#            20% para parafusos e 30% para arruelas.
#            Escreva um algoritmo que calcule o valor total da compra de um cliente.
#            Deve ser mostrado o nome do cliente, o número de cada tipo de peça que
#            o mesmo comprou, o total de desconto e o total a pagar pela compra.
# -------------------------------------------------------------

nome_cliente = input("Digite o nome do cliente: ")

preco_parafuso = float(input("Preço unitário do parafuso: R$ "))
preco_porca = float(input("Preço unitário da porca: R$ "))
preco_arruela = float(input("Preço unitário da arruela: R$ "))

quantidade_parafusos = int(input("Quantidade de parafusos: "))
quantidade_porcas = int(input("Quantidade de porcas: "))
quantidade_arruelas = int(input("Quantidade de arruelas: "))

total_parafusos = preco_parafuso * quantidade_parafusos
total_porcas = preco_porca * quantidade_porcas
total_arruelas = preco_arruela * quantidade_arruelas

# Desconto de cada tipo de peça
desconto_parafusos = total_parafusos * 0.20
desconto_porcas = total_porcas * 0.10
desconto_arruelas = total_arruelas * 0.30

total_compra = total_parafusos + total_porcas + total_arruelas
total_desconto = desconto_parafusos + desconto_porcas + desconto_arruelas
total_a_pagar = total_compra - total_desconto

print("Cliente:", nome_cliente)
print("Parafusos:", quantidade_parafusos)
print("Porcas:", quantidade_porcas)
print("Arruelas:", quantidade_arruelas)
print("Total de desconto: R$", total_desconto)
print("Total a pagar: R$", total_a_pagar)


# -------------------------------------------------------------
# Questão 7
# Enunciado: Escreva um algoritmo que, para uma conta bancária, leia o seu número,
#            o saldo, o tipo de operação a ser realizada (depósito ou retirada) e
#            o valor da operação. Após, determine e mostre o novo saldo.
#            Se o novo saldo ficar negativo, deve ser mostrada, também, a mensagem
#            "conta estourada".
# -------------------------------------------------------------

numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo atual: R$ "))

print("Tipo de operação: 1 - Depósito  2 - Retirada")
tipo_operacao = int(input("Opção: "))
valor_operacao = float(input("Valor da operação: R$ "))

if tipo_operacao == 1:
    novo_saldo = saldo + valor_operacao
else:
    novo_saldo = saldo - valor_operacao

print("Número da conta:", numero_conta)
print("Novo saldo: R$", novo_saldo)

if novo_saldo < 0:
    print("conta estourada")


# -------------------------------------------------------------
# Questão 8
# Enunciado: Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos
#            dos lados de um triângulo e, se forem, verificar se é um triângulo
#            equilátero, isóscele ou escaleno. Se eles não formarem um triângulo,
#            escrever uma mensagem.
#            OBS: o comprimento de cada lado de um triângulo é menor do que a soma
#            dos comprimentos dos outros dois lados.
#            Definição 1 - triângulo equilátero: os três lados iguais;
#            Definição 2 - triângulo isóscele: dois lados iguais;
#            Definição 3 - triângulo escaleno: os três lados diferentes.
# -------------------------------------------------------------

lado1 = float(input("Digite o valor do lado X: "))
lado2 = float(input("Digite o valor do lado Y: "))
lado3 = float(input("Digite o valor do lado Z: "))

# Para ser triângulo, cada lado precisa ser menor que a soma dos outros dois
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É um triângulo.")

    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isóscele.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")


# -------------------------------------------------------------
# Questão 9
# Enunciado: Faça um algoritmo que leia quatro números (Opção, Num1, Num2 e Num3)
#            e mostre o valor de Num1 se Opção for igual a 2; o valor de Num2 se
#            Opção for igual a 3; e o valor de Num3 se Opção for igual a 4.
#            Os únicos valores possíveis para a variável Opção são 2, 3 e 4.
# -------------------------------------------------------------

opcao = int(input("Digite a Opção (2, 3 ou 4): "))
numero1 = float(input("Digite o Num1: "))
numero2 = float(input("Digite o Num2: "))
numero3 = float(input("Digite o Num3: "))

if opcao == 2:
    print("Num1 =", numero1)
elif opcao == 3:
    print("Num2 =", numero2)
elif opcao == 4:
    print("Num3 =", numero3)
else:
    print("Opção inválida! Os valores permitidos são 2, 3 e 4.")


# -------------------------------------------------------------
# Questão 10
# Enunciado: Crie um algoritmo que calcula o desconto previdenciário de um
#            funcionário. Dado um salário, o programa deve retornar o valor do
#            desconto proporcional ao mesmo. O cálculo segue a regra:
#            o desconto é de 11% do valor do salário, entretanto, o valor máximo
#            a ser descontado é R$ 318,20.
# -------------------------------------------------------------

salario = float(input("Digite o salário: R$ "))

desconto = salario * 0.11

# O desconto nunca pode passar de R$ 318,20
if desconto > 318.20:
    desconto = 318.20

salario_liquido = salario - desconto

print("Valor do desconto: R$", desconto)
print("Salário após o desconto: R$", salario_liquido)
