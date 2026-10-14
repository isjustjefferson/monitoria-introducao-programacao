# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 27
# Enunciado: Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
#            seguintes categorias:
#            - Infantil A: 5 a 7
#            - Infantil B: 8 a 10
#            - Juvenil A: 11 a 13
#            - Juvenil B: 14 a 17
#            - Sênior: maiores de 18 anos
# -------------------------------------------------------------

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Sênior")
else:
    print("Idade fora das categorias.")
