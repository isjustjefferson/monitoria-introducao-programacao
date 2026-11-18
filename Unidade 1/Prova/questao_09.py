# ==============================================================
# Introdução à Programação
# Prova da 1ª Unidade
# ==============================================================

# -------------------------------------------------------------
# Questão 9
# Enunciado: Fechamento de compra. Leia o preço de 3 itens e 
# acumule o total usando +=. Mostre o subtotal, aplique 10% de
# desconto usando *= e calcule o frete: grátis se o valor com
# desconto for maior ou igual a R$ 100,00, ou R$ 15,00 caso 
# contrário. Use uma expressão condicional (if em uma linha) 
# para definir o frete. Mostre o total a pagar.
# -------------------------------------------------------------
# Exemplo de execução:
# Preço do item 1: R$ 20
# Preço do item 2: R$ 30
# Preço do item 3: R$ 40
# Subtotal: R$ 90.00
# Com desconto: R$ 81.00
# Frete: R$ 15.00
# Total a pagar: R$ 96.00
# -------------------------------------------------------------

total = 0
contador = 0

while contador < 3:
    total += int(input(f"Preço do item {contador+1}: R$ "))
    contador +=1

print(f"Subtotal: R$ {total:.2f}")

total *= 0.9
print(f"Com desconto: R$ {total:.2f}")

frete = 0 if total >= 100 else 15
print(f"Frete: R$ {frete:.2f}")

print(f"Total a pagar: R$ {(total + frete):.2f}")