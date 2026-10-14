# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

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
