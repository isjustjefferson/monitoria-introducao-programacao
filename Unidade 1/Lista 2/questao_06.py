# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

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
