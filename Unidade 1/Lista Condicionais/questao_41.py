# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 41
# Enunciado: Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação
#            de acordo com a tabela abaixo:
#            IMC            | Classificação
#            < 18,5         | Abaixo do Peso
#            18,6 - 24,9    | Saudável
#            25,0 - 29,9    | Peso em excesso
#            30,0 - 34,9    | Obesidade Grau I
#            35,0 - 39,9    | Obesidade Grau II (severa)
#            >= 40,0        | Obesidade Grau III (mórbida)
# -------------------------------------------------------------

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)
print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Peso em excesso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
