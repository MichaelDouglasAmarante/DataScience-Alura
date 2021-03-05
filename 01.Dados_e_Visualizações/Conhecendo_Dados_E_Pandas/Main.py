import pandas as pd
import os

path = os.path.dirname(os.path.realpath(__file__))

notas = pd.read_csv(f'{path}\\..\\ml-latest-small\\ratings.csv')
notas.head()

# Renomeando nomes das colunas -> .columns
notas.columns = ["usuarioId","filmeId","notas","momento"]

notas['notas']

# Verificando valores unicos da serie 'notas'
notas['notas'].unique()

# Conta os valores
notas['notas'].value_counts()

# Média de todas as notas
notas['notas'].mean()