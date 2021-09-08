# Atividade 2: Alistamento

# O programa deve ler o ano de nascimento de uma pessoa
# O sistema deve imprimir informando se ela está na idade de se alistar ou não(considerando que se tiver mais de 18 anos, deve se alistar)
# Considere Ler o ano atual do sistema ao invés de usar um ano fixo, usando o exemplo de código abaixo:

from datetime import date
anonascimento = int(input("Informe o ano de seu nascimento: "))
anoatual = float(date.today().year)
if anoatual - anonascimento > 18:
    print("Deve se alistar!")
else:
    print("Não deve se alistar!")
    
