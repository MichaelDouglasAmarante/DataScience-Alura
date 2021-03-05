import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


path = os.path.dirname(os.path.realpath(__file__))

notas = pd.read_csv(f'{path}\\..\\ml-latest-small\\ratings.csv')
filmes = pd.read_csv(f'{path}\\..\\ml-latest-small\\movies.csv')

notas.columns = ["usuarioId","filmeId","nota","momento"]
filmes.columns = ["filmeId","titulo","generos"]

# Analisando algumas notas especificas por filme
notas.query("filmeId==1").head()
notas.query("filmeId==1").nota.mean()

# Vinculando todo o dataframe carregando com o pandas
# e agrupando pela coluna filme id
medias_por_filme = notas.groupby("filmeId").mean().nota
medias_por_filme.plot(kind='hist')

# Exibindo descrição
medias_por_filme.describe()

# Usando o boxsplot - seaborn  | no eixo y
sns.boxplot(y=medias_por_filme)

# Histograma no seaborn 
sns.displot(medias_por_filme)
sns.distplot(medias_por_filme)

# bins = quantidade de "caixas" para organização do gráfico
# bins deve ser usado com cuidado para que os dados gráfico não pareçam
# algo que não é 
sns.distplot(medias_por_filme, bins=10) 

# Usando puplot

# Maneira "mais baixo nivel" de gerar histograma
# Obs: pandas e seaborne usam pyplot por baixo dos planos
plt.hist(medias_por_filme) 
plt.title("Histograma das médias dos filmes")

