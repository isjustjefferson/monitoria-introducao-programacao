# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

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
