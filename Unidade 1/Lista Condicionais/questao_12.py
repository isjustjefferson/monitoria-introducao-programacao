# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 12
# Enunciado: Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
#            "Número inválido". Se o número for positivo, calcular o logaritmo deste
#            número.
# -------------------------------------------------------------

# Para a raiz quadrada usamos o operador ** (elevar a 0.5), que não precisa de
# biblioteca. Já o logaritmo não tem um operador simples na linguagem, por isso
# é necessário importar a biblioteca "math" e usar a função math.log().
import math

numero = float(input("Digite um número: "))

if numero > 0:
    print("Logaritmo:", math.log(numero))
else:
    print("Número inválido")
