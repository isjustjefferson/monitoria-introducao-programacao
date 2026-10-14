# ==============================================================
# Introdução à Programação
# Lista 3
# ==============================================================

# -------------------------------------------------------------
# Questão 6
# Enunciado: Desenvolva um algoritmo em python que leia um número n que indica
#            quantos valores devem ser lidos a seguir. Após isso, o usuário deve
#            digitar os números e, ao final, o algoritmo deve imprimir a soma de
#            todos eles.
# -------------------------------------------------------------

quantidade = int(input("Quantos números você vai digitar? "))

soma = 0
contador = 0

# while: fica repetindo enquanto o contador for menor que a quantidade
while contador < quantidade:
    numero = float(input("Digite um número: "))
    soma = soma + numero
    contador = contador + 1

print("A soma de todos os números é:", soma)
