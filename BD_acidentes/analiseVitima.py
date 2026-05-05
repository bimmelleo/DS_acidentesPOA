import pandas as pd
from matplotlib import pyplot as plt

#carregando a base
df = pd.read_csv('cat_acidentes.csv', sep=';')

#limpando valores NaN
df = df.dropna(subset=['feridos', 'feridos_gr', 'mortes', 'morte_post', 'fatais'], how='any')

#definindo os index's
colunas_feridos = ['feridos', 'feridos_gr']
colunas_graves = ['mortes', 'morte_post', 'fatais']

#convertendo para numéricos, evitando erros
df[colunas_feridos] = df[colunas_feridos].apply(pd.to_numeric, errors='coerce')
df[colunas_graves] = df[colunas_graves].apply(pd.to_numeric, errors='coerce')

df_feridos = df[colunas_feridos].sum()
df_graves = df[colunas_graves].sum()

#customização gráfico
maior = df_feridos.max()
grad = df_feridos / maior #baseado na porcentagem dos anos ao ano com mais acidentes
cores = plt.cm.Reds(grad) #variação das coloração Reds baseado nas porcentagens por ano

maior = df_graves.max()
grad = df_graves / maior #baseado na porcentagem dos anos ao ano com mais acidentes
cores = plt.cm.Reds(grad) #variação das coloração Reds baseado nas porcentagens por ano


plt.bar(df_feridos.index, df_feridos.values, color=cores)
plt.title('Total de vítimas por tipo')
plt.xlabel('Tipo de vítima')
plt.ylabel('Quantidade')
plt.show()

plt.bar(df_graves.index, df_graves.values, color=cores)
plt.title('Total de vítimas por tipo')
plt.xlabel('Tipo de vítima')
plt.ylabel('Quantidade')
plt.show()