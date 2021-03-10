import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tmdb = pd.read_csv("C:\\Users\\mdoug\\OneDrive\\Documentos\\GitHub\\DataScience-Alura\\tmdb\\tmdb_5000_movies.csv")

outros = tmdb.query("original_language != 'en'")
total_por_lingua_de_outros_files = tmdb.query("original_language != 'en'").original_language.value_counts()
# Gerando gráfico com catplot
sns.catplot(x = "original_language", kind = "count", data = outros)

# Alterando configurações da figura
# https://seaborn.pydata.org/generated/seaborn.catplot.html
# Para ordenar: order
sns.catplot(x = "original_language", kind = "count", data = outros, aspect = 2, order = total_por_lingua_de_outros_files.index)


# Coloração: Palet
# https://seaborn.pydata.org/tutorial/color_palettes.html
sns.catplot(x = "original_language", kind = "count", data = outros, aspect = 2, palette = "GnBu_d", order = total_por_lingua_de_outros_files.index)