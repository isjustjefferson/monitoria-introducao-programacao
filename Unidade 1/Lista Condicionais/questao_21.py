# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 21
# Enunciado: Escreva o menu de opções abaixo. Leia a opção do usuário e execute a
#            operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
#            Escolha a opção:
#            1- Soma de 2 números.
#            2- Diferença entre 2 números (maior pelo menor).
#            3- Produto entre 2 números.
#            4- Divisão entre 2 números (o denominador não pode ser zero).
# -------------------------------------------------------------

print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números (maior pelo menor)")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números")
opcao = int(input("Opção: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", numero1 + numero2)
elif opcao == 2:
    if numero1 > numero2:
        print("Resultado:", numero1 - numero2)
    else:
        print("Resultado:", numero2 - numero1)
elif opcao == 3:
    print("Resultado:", numero1 * numero2)
elif opcao == 4:
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Não é possível dividir por zero.")
else:
    print("Opção inválida")
