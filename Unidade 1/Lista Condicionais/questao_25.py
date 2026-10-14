# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 25
# Enunciado: Calcule as raízes da equação de 2º grau. Lembrando que x = (-b ± raiz(Δ)) /
#            2a, onde Δ = b² - 4ac, e ax² + bx + c = 0.
#            A variável a tem que ser diferente de zero. Caso seja igual, imprima a
#            mensagem "Não é equação de segundo grau".
#            - Se Δ < 0, não existe raiz real. Imprima "Não existe raiz".
#            - Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz única".
#            - Se Δ > 0, imprima as duas raízes reais.
# -------------------------------------------------------------

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação de segundo grau")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        raiz = -b / (2 * a)
        print("Raiz única:", raiz)
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print("Raiz 1:", raiz1)
        print("Raiz 2:", raiz2)
