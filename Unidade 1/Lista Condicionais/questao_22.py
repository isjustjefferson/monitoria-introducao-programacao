# ==============================================================
# Introdução à Programação
# Lista de Comandos Condicionais
# ==============================================================

# -------------------------------------------------------------
# Questão 22
# Enunciado: Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou
#            não se aposentar. As condições para aposentadoria são:
#            - Ter pelo menos 65 anos;
#            - Ou ter trabalhado pelo menos 30 anos;
#            - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
# -------------------------------------------------------------

idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço (anos): "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")
