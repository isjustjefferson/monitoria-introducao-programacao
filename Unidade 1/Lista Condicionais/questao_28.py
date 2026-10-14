# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 28
# Enunciado: Faça um programa que leia três números inteiros positivos e efetue o cálculo
#            de uma das seguintes médias de acordo com um valor numérico digitado pelo
#            usuário:
#            (1) Geométrica: raiz cúbica de x * y * z
#            (2) Ponderada: (x + 2*y + 3*z) / 6
#            (3) Harmônica: 3 / (1/x + 1/y + 1/z)
#            (4) Aritmética: (x + y + z) / 3
# -------------------------------------------------------------

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

print("1 - Geométrica")
print("2 - Ponderada")
print("3 - Harmônica")
print("4 - Aritmética")
opcao = int(input("Escolha o tipo de média: "))

if opcao == 1:
    media = (x * y * z) ** (1 / 3)
    print("Média geométrica:", media)
elif opcao == 2:
    media = (x + 2 * y + 3 * z) / 6
    print("Média ponderada:", media)
elif opcao == 3:
    media = 3 / (1 / x + 1 / y + 1 / z)
    print("Média harmônica:", media)
elif opcao == 4:
    media = (x + y + z) / 3
    print("Média aritmética:", media)
else:
    print("Opção inválida")
