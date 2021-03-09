# Uma das áreas dentro de Ciencia de Dados é o estudo de como apresentar adequadamento dados,
# por exemplo: como usar um gráfico e qual usar

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tmdb = pd.read_csv("C:\\Users\\mdoug\\OneDrive\\Documentos\\GitHub\\DataScience-Alura\\tmdb\\tmdb_5000_movies.csv")

contagem_de_idiomas = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_idiomas.columns = ["original_language","total"]


# Gráfico torta/pizza
# Esse modelo de gráfico não é recomendado, por dificultar a visualização dos dados
plt.pie(contagem_de_idiomas["total"], labels = contagem_de_idiomas["original_language"])

# ***Devemos pensar em qual mensagem queremos passar com nosso gráfico

# Voltando ao gráfico catplot, podemos pensar da seguinte forma:
# Percebemos que o idioma Inglês tem um diferença grande comparado a todos os outros individualmente,
sns.catplot(x = "original_language", kind = "count", data = tmdb)
# então podemos fazer o seguinte: Analisar o idioma Inglês com um conjunto de todos os outros idiomas

# loc = localizar a(s) linhas onde o indice contenham /?/
total_por_idioma = tmdb["original_language"].value_counts()
total_geral = total_por_idioma.sum()
total_de_ingles = total_por_idioma.loc["en"]
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles,total_do_resto)


# Criando dicionario com os dados
dados = {
    'lingua': ['ingles','outros'],
    'total': [total_de_ingles, total_do_resto]
}

# Dataframe em cima de 'dados'
dados = pd.DataFrame(dados)

# Plotando os dados
sns.barplot(x = "lingua", y = "total", data = dados)