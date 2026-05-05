import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

#carregando a base
df = pd.read_csv('cat_acidentes.csv', sep=';')


#converter de object para data
df['data'] = pd.to_datetime(df['data'], errors='coerce')

#extrair os anos
df_ano = df['data'].dt.year.value_counts()

#customização gráfico
grad = df_ano/df_ano.max() #baseado na porcentagem dos anos ao ano com mais acidentes
cores = plt.cm.Blues(grad) #variação das coloração Blues baseado nas porcentagens por ano

plt.bar(df_ano.index, df_ano.values, color = cores)
plt.show()