# ==============================================================
# Introdução à Programação
# Lista 2
# ==============================================================

# -------------------------------------------------------------
# Questão 8
# Enunciado: Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos
#            dos lados de um triângulo e, se forem, verificar se é um triângulo
#            equilátero, isóscele ou escaleno. Se eles não formarem um triângulo,
#            escrever uma mensagem.
#            OBS: o comprimento de cada lado de um triângulo é menor do que a soma
#            dos comprimentos dos outros dois lados.
#            Definição 1 - triângulo equilátero: os três lados iguais;
#            Definição 2 - triângulo isóscele: dois lados iguais;
#            Definição 3 - triângulo escaleno: os três lados diferentes.
# -------------------------------------------------------------

lado1 = float(input("Digite o valor do lado X: "))
lado2 = float(input("Digite o valor do lado Y: "))
lado3 = float(input("Digite o valor do lado Z: "))

# Para ser triângulo, cada lado precisa ser menor que a soma dos outros dois
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É um triângulo.")

    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isóscele.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")
