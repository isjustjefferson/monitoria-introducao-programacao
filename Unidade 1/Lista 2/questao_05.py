# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

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
