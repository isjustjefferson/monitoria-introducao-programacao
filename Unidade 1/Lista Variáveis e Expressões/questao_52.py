# ==============================================================
# Introdução à Programação
# Lista de Variáveis e Expressões
# ==============================================================

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
