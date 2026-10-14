# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 20
# Enunciado: Dados três valores, A, B e C, verificar se eles podem ser valores dos lados
#            de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou
#            isóscele, considerando:
#            - O comprimento de cada lado de um triângulo é menor do que a soma dos
#              outros dois lados.
#            - Equilátero: três lados iguais.
#            - Isóscele: dois lados iguais.
#            - Escaleno: os três lados diferentes.
# -------------------------------------------------------------

ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado C: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print("É um triângulo.")

    if ladoA == ladoB and ladoB == ladoC:
        print("Triângulo equilátero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Triângulo isóscele.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")
