import os 
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
tmdb = pd.read_csv(f"{path}\\..\\tmdb\\tmdb_5000_movies.csv")

# Quando temos dados por categoria, podemos por exemplo, analisar quantas vezes aparece tal categoria
print(tmdb.original_language)
