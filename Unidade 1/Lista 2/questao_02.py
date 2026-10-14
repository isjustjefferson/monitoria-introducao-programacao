# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

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
