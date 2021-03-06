import os 
import pandas as pd

path = os.path.dirname(os.path.realpath(__file__))
tmdb = pd.read_csv(f"{path}\\..\\tmdb\\tmdb_5000_movies.csv")

# Variavel categorica: Onde não há peso nos valores, e no exemplo abaixo sem ordem.
tmdb.original_language.unique()

# Exemplo de variavel categorica com ordem/ordinal: (Obs: a ideia de operações aritimeticas dificilmente se aplicam)
# primeiro grau
# segundo grau
# terceiro grau

# budget => orcamento => quantitativo continuo

# categorica intervalar:
# quantidade de votos => será 1,2,3,4... não tem meio(ex: 1.5) voto(s)