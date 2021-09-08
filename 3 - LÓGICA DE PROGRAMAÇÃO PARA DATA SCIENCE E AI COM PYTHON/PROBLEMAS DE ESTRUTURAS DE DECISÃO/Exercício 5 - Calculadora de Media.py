# Exercício 5: Calculadora de Média

# O programa deve calcular a média dos números informados pelo usuário
# Primeiramente o programa pergunta quantos números o usuário vai entrar
# Em seguida ele pede para o usuário entrar com cada um dos números
# Por fim, o programa imprime a média dos números

tab = int(input("Quantos números serão calculados? "))
soma = 0
for tab in range(1,tab+1):
    texto = "Informe o " + str(tab) + "º número: "
    soma = soma + int(input(texto))

print("A média é igual a : ", soma / tab)

                
