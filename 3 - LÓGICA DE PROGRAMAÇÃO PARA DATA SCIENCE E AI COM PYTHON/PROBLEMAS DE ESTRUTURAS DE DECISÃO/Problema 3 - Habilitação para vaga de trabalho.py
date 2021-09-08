# Problema 3: Habilitação para vaga de trabalho
# Para se habilitar a uma vaga de trabalho, o candidato deve cumprir pelo menos um dos requisistos abaixo:
# Ter menos de 70 anos de idade
# Ter pelo menos 25 anos de atividade profissional
# Ter mais de 70 anos e pelo menos 30 anos de atividade profissional
# O programa deve ler estas informações (todas do tipo inteiro) e imprimir se o candidato está ou não habilitado a vaga de trabalho

idade = int(input("Informe sua idade: "))
atividade = float(input("Informe o tempo de atividade profissional: "))
if (idade < 70) or (atividade >= 25) or (idade >= 70 and atividade >=30):
    print("Habilitado para o trabalho!")
else:
    print("Não habilitado")
    
 # Testes
 # 70 anos de idade e outro valor qualquer, habilitado
 # 24 anos de atividade profissional e outro valor qualquer, habilitado
 # 73 anos e 30 anos, habilitado(3ª condição)
 # 72 anos e 22 anos, não habilitado
