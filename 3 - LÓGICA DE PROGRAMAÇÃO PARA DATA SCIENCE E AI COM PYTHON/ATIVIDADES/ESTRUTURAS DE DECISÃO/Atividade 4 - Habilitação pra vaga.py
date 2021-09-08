# Atividade 4: Habilitação pra vaga

# O programa deve perguntar a idade de um candidato a vaga
# O programa ainda deve perguntar a escolaridade, imprimindo as opções:
  # 1 - ensino fundamental
  # 2 - ensino médio
  # 3 - ensino superior
# O candidato é habilitado a concorrer a vaga se:
  # Tem ensino superior completo ou
  # Tem ensino médio completo e mais de 60 anos
# Imprimir mensagem irformando se o candidato está habilitado ou não

idade = int(input("Informe a sua idade: "))
print("Informe a sua escolaridade: ")
print("1 - ensino fundamental")
print("2 - ensino médio")
print("3 - ensino superior")
escolaridade = float(input())

if (escolaridade==3) or (escolaridade==2 and idade > 60):
    print("Habilitado!")
else:
    print("Não Habilitado!")
    

