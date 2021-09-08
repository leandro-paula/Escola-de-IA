# Problema 3 - Inversão de variáveis

var1 = input("Informe a primeira variável: ")
var2 = input("Informe a primeira variável: ")
vartemp = var2
var2 = var1
var1 = vartemp
print("As variáveis invertidas são: ",var1, "e", var2)

# Forma errada

var1 = input("Informe a primeira variável: ")
var2 = input("Informe a primeira variável: ")
print("As variáveis invertidas são: ",var2, "e", var1)

