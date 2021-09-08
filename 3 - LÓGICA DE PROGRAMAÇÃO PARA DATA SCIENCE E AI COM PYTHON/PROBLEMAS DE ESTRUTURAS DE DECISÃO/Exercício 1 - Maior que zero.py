# Exercício 1: Maior que zero

# Crie um programa qua leia a idade do cliente
# A idade deve ser um valor igual ou maior que zero. Se a entrada não atender este critério, o programa deve solicitar novamente a entrada do dado, até a condição ser atendida


idade = 0
while idade <= 0:
    idade = int(input("Informe a idade: "))
print("Idade Informada: ", idade)    
