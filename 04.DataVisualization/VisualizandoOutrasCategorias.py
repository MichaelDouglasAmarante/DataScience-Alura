# Uma das áreas dentro de Ciencia de Dados é o estudo de como apresentar adequadamento dados,
# por exemplo: como usar um gráfico e qual usar

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tmdb = pd.read_csv("C:\\Users\\mdoug\\OneDrive\\Documentos\\GitHub\\DataScience-Alura\\tmdb\\tmdb_5000_movies.csv")

# Análisando idiomas diferentes de 'en'
outros = tmdb.query("original_language != 'en'")

# Gerando gráfico com catplot
sns.catplot(x = "original_language", kind = "count", data = outros)