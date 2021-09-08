# Atividade 1 - Positivo ou Negativo

# O sistema deve ler um valor inteiro
# Imprimir positivo se o valor for positivo e negativo, se for negativo e neutro se for zero

val = int(input("Informe um valor: "))
if val < 0:
    print("Número Negativo")
elif val > 0:
    print("Numero Positivo")
else:
    print("Número Neutro")
    
