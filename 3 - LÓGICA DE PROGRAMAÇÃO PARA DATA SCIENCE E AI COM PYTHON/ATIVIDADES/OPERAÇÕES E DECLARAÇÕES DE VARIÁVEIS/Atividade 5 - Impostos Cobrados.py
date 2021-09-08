# Atividade 5 - Impostos Cobrados

# O programa deve ler o valor total da manutenção de um veículo
# O programa deve ler o percentual de impostos de serviço
# O programa deve ler o percentual de impostos de produtos
# O programa deve imprimir o total a ser pago nos dois impostos, bem como o valor que sobra depois de descontado os imposto

#5 Impostos
#Professor Fernando Amaral

total =  float(input("Informe o valor total da manutenção: "))
issqn =  float(input("Informe o percentual de impostos sobre serviços: "))
icms =  float(input("Informe o percentual de impostos sobre circulação de produtos: "))

totalissqn = total * (issqn/100)
totalicms =total * (icms/100)

print("O total de ISSQN é de  ", totalissqn)
print("O total de ICMS é de  ", totalicms)
print("O valor restante retirado os impostos é de   ",total -  totalissqn - totalicms)     


