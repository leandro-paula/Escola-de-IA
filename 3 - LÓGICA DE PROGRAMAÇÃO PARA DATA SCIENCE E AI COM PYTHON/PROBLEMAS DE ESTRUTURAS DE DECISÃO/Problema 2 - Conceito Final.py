# Problema 2 - Conceito Final

# O  professor deve entrar com uma nota no sistema (float)
# O programa deve imprimir o conceito final de acordo com a nota, de acordo com a tabela abaixo:

nota = float(input("Informe a nota do aluno: "))
if nota >90:
    print(" Conceito A")
elif nota >=75 and nota <=90:
    print(" Conteito B")
elif nota >=60 and nota <75:
    print(" Conceito C")
elif nota >=40 and nota <60:
    print(" Conceito D")
elif nota >=20 and nota <40:
    print(" Conceito E")
else:
    print(" Conceito F")
    
