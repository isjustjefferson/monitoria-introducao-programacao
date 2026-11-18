# ==============================================================
# Introdução à Programação
# Prova da 1ª Unidade
# ==============================================================

# -------------------------------------------------------------
# Questão 10
# Enunciado: Múltiplos de 3. Leia dois inteiros, início e fim.
# Usando While, mostre na mesma linha todos os múltiplos de 3 
# desse intervalo (incluindo os extremos) e, ao final, a 
# quantidae (contador) e a soma (acumulador) desses números.
# -------------------------------------------------------------
# Exemplo de execução:
# Início: 4
# Fim: 20
# 6 9 12 15 18
# Quantidade: 5 | Soma: 60
# -------------------------------------------------------------

inicio = int(input("Início: "))
fim = int(input("Fim: "))

contador = 0
acumulador = 0

while inicio <= fim:
    if inicio % 3 == 0:
        print(inicio, end=" ")
        contador += 1
        acumulador += inicio

    inicio +=1

print(f"\nQuantidade: {contador} | Soma: {acumulador}")