import pandas as pd
import os 
import seaborn as sns

path = os.path.dirname(os.path.realpath(__file__))
notas = pd.read_csv(f"{path}\\..\\ml-latest-small\\ratings.csv")


#region Tratando dados com o Pandas
notas.columns = ["usuarioId","filmeId","nota","momento"]

notas.nota.head()
# Gera gráfico com os dados da coluna 'nota'
notas.nota.plot()


# "Contar uma história" do que está acontecendo com nossos dados
notas.nota.plot(kind="hist")

# Média e Mediana
print("Média: ", notas.nota.mean())
print("Mediana: ", notas.nota.median())

# .describe gera descrição dos nossos dados 
notas.nota.describe()
#endregion

#region Usando Seaborn
#boxplot gera um gráfico organizando a distribuição da frequencia dos valores
sns.boxplot(notas.nota)
#endregion