# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

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
