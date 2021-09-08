# Atividade 5 - Testes

# O programa deve ler dois valores inteiros
# Imprimir
  # São iguais, se forem iguais
  # São diferentes, se forem diferentes
  # Primeiro é maior, se o primeiro for maior
  # Segundo é maior se o segundo for maior
  
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
if val1 == val2:
    print("São iguais")
else:
    print("São diferentes")
if val1 > val2:
    print("O Primeiro é maior")
elif val1 < val2:
    print("Segundo é maior")
    
