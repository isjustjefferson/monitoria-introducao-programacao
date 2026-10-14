# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 26
# Enunciado: Leia a distância em Km e a quantidade de litros de gasolina consumidos por um
#            carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
#            acordo com a tabela abaixo:
#            - menor que 8 Km/l -> "Venda o carro!"
#            - entre 8 e 14 Km/l -> "Econômico!"
#            - maior que 14 Km/l -> "Super econômico!"
# -------------------------------------------------------------

distancia = float(input("Digite a distância percorrida (Km): "))
litros = float(input("Digite a quantidade de litros consumidos: "))

consumo = distancia / litros
print("Consumo:", consumo, "Km/l")

if consumo < 8:
    print("Venda o carro!")
elif consumo <= 14:
    print("Econômico!")
else:
    print("Super econômico!")
