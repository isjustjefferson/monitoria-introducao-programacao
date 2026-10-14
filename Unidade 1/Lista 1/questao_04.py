# ==============================================================
# Introdução à Programação
# Lista 1
# ==============================================================

# -------------------------------------------------------------
# Questão 4
# Enunciado: Sabendo que um caixa eletrônico terá notas de R$ 50 e R$ 10,
#            faça um programa que, fornecido um valor para saque (inteiro),
#            calcule quantas notas de 50 e quantas notas de 10 o cliente
#            deve receber em um caixa eletrônico, além de indicar a parte
#            do valor cujo saque é impossível (resto entre 0 e 9, inclusive).
#            O número de notas deve ser o menor possível.
# -------------------------------------------------------------

saque = int(input("Digite o valor do saque: "))

# Primeiro pegamos as notas de R$ 50 (maiores) e depois o que sobrou.
notas_de_50 = saque // 50        # // devolve só a parte inteira da divisão
resto = saque % 50               # % devolve o resto da divisão

notas_de_10 = resto // 10
valor_nao_sacavel = resto % 10

print("Notas de R$ 50:", notas_de_50)
print("Notas de R$ 10:", notas_de_10)

if valor_nao_sacavel > 0:
    print("Não é possível sacar o valor de: R$", valor_nao_sacavel)
else:
    print("O valor inteiro pode ser sacado.")
