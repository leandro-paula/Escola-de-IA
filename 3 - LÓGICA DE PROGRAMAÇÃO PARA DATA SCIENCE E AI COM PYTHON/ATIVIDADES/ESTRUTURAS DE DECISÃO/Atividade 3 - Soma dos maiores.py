# Atividade 3: Soma dos maiores

# Faça a leitura de 2 valores inteiros
# Imprima os valores em ordem crescente

numeros = [25,87,46,92,65,36,74,21,10]
numeros
numeros_ordenados = sorted(numeros)

print(numeros)
print(numeros_ordenados)
              
#Prof. Fernando Amaral
#3 Soma dos maiores
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
if val1 < val2 :
    print(val1, " ", val2)
else:
    print(val2, " ", val1)
