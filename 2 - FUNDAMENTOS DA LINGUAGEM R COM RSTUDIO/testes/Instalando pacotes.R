# Instalando pacotes

install.packages("e1071", dependencies = TRUE)
library(e1071)

# Para saber o diretório padrão
getwd()

# Para alterar o diretório padrão
setwd()

------------------------------------------------------------------------------------------

getwd()
setwd("C:/Users/leand/OneDrive/Imagens/Área de Trabalho/ESCOLA DE INTELIGÊNCIA ARTIFICIAL/FUNDAMENTOS DA LINGUAGEM R COM RSTUDIO/testes")


class(iris)

iristeste = iris
save(iristeste, file = "iristeste.Rdata")
iristeste
rm(iristeste)
iristeste
load(file ="iristeste.Rdata")
iristeste

x = c(12,34,56,79)
y = c(1,6,9,14)
plot(x,y)

quit()

-------------------------------------------------
  # Tipos de dados e Operadores Parte I
  
delta <- 8
class(delta)

delta = 8L
class(delta)

c = 2
d = 4
(c + d) * d
e = (c + d) * d
e

a = 1
b = 2
a < b
a == b

sqrt(2500)

--------------------------------------------------------------------------
# Estruturas de Dados Parte I
  
# Vetores
x <- c(1,2,3,4,5,6)
x
x[1]
x[1] <- 10
x[1]

# Outros tipos de vetores
y = c("a","b","c","d")
y
z = c(1L,2L,3L)
z

# Matrizes
VADeaths
colnames(VADeaths)
row.names(VADeaths)

# Só a Coluna 1
VADeaths[,1]

# Só a Linha 1
VADeaths[1,]

# Das Linhas 1 até a 3
VADeaths[1:3,]

# Data Frame
longley

# Funciona como Matrizes
longley[,1:3]
$acessar coluna com $
longley$Unemployed

# Ou nome
longley['Unemployed']

# Listas
ability.cov

# Acessando elementos
ability.cov$cov
ability.cov[1]

# Verificando que sao objetos diferentes
class( ability.cov$cov)
class( ability.cov$center)

# Acessando elementos dentro da lista
ability.cov$cov[,1:3]

# Fatores, variáveis categóricas com um número limitado de valores
# São armazenados como inteiros
state.region
----------------------------------------------------------------------------------------------------------------------------
  
head(x=iris, n=2)
head(iris)
head(iris,2)
head(n=22)

help(sd)

-----------------------------------------------------------------------------------------------------------------------------
esoph
# Default 6 linhas
head(esoph)
tail(esoph)
# Default 10 linhas
head(esoph, n=10)
tail(esoph, n=10)
# Funcao dim() mostra quantas linhas e colunas existe no dataframe
dim(esoph)

# Vamos usar apenas para um vetor, se usar com objetos bidimensional vai retornar colunas
length(islands)

colnames(esoph)
rownames(esoph)
summary(esoph)

x = file.choose()
x

-------------------------------------------------------------------------------------------------------------------------------------------------------
# Importando dados
# Texto
  
x = read.csv(file.choose(), header = TRUE, sep = ";")
x

# odbc
install.packages("RODBC")
library(RODBC)
conexao <- odbcDriverConnect('driver={SQL Server};server=DESKTOP-UD9RQJ9\\SQLEXPRESS;database=VENDAS;trusted_connection=true')

resultado <- sqlQuery(conexao, "select * from dbo.vendas ")
resultado

odbcClose(conexao)

# Planilha
install.packages("xlsx")
library(xlsx)
dados = read.xlsx(file.choose(),sheetIndex = 1)
dados

# arff
install.packages('foreign')
library(foreign)
dados = read.arff(file.choose())
dados

---------------------------------------------------------------------------------------------------------------
# Programação Parte II

a = 10
b = 20

if (a > 10)
{
  print("A é maior")
}else
{
  print("A não é maior")
}  

x = ifelse(a > 10,"A é maior", "A não é maior")
x

for (i in 1:10) {
  print(i)
}

a = 1
while(a <= 10)
{
  print(a)
  a = a+1
}  

parouimpar <- function(x) {
  return(ifelse(x%%2==0,"Par","impar"))
}
                      
parouimpar(5)
parouimpar(12)







  












