import os 
import pandas as pd
import seaborn as sns


path = os.path.dirname(os.path.realpath(__file__))
tmdb = pd.read_csv(f"{path}\\..\\tmdb\\tmdb_5000_movies.csv")

# Quando temos dados por categoria, podemos por exemplo, analisar quantas vezes aparece tal categoria
print(tmdb["original_language"].value_counts())

# .value_counts() gera uma série
# usa-se .to_frame() para transformar a série em um dataframe:
contagem_de_idiomas = tmdb["original_language"].value_counts().to_frame()

# Caso queira transformar o index/indice em uma coluna usar .reset_index():
contagem_de_idiomas = tmdb["original_language"].value_counts().to_frame().reset_index()

# Redefinindo
contagem_de_idiomas.columns = ["original_language","total"]
print(contagem_de_idiomas.head())


# Para comparar categorias, podemos usar plots de categoria
# Seaborn categorical plot:
# https://seaborn.pydata.org/tutorial/categorical.html

# Gráfico de barras
sns.barplot(x ="original_language", y = "total", data = contagem_de_idiomas)


# Gráfico de auto-nivel, com menor possibilidade de manipulação comparado a um de baixo nivel
# catplot: plota baseado em categoria
# kind: define a maneira como os dados serão organizados
sns.catplot(x = "original_language", kind = "count", data = tmdb)