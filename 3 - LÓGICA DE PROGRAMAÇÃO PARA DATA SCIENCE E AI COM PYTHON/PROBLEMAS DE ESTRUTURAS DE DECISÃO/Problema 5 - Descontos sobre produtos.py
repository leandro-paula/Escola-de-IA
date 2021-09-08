# Problema 5 - Descontos sobre produtos

# O programa deve ler a quantidade de produtos comprados(int) e o valor total(float)
# Deverá imprimir:
  # O valor total da compra - sem desconto
  # O valor total da compra - com desconto
  # O valor da economia
# Deve ser utilizada a tabela de descontos abaixo:

quantidade = int(input("Informe a quantidade de produtos: "))
total = float(input(" Informe o valor total da compra: "))
desconto = 0
if quantidade == 2:
    desconto = 0.02
elif quantidade > 2 and quantidade <= 5:
    desconto = 0.05
elif quantidade > 5 and quantidade < 10:
    desconto = 0.1
elif quantidade >= 10:
    desconto = 0.15

caldesc = total - (total * desconto)

print("O valor total da compra: ", total)
print("O valor total com desconto: ", caldesc)
print("Economia: ", total - caldesc)



