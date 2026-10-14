# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

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
