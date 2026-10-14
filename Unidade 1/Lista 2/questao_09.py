# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

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
