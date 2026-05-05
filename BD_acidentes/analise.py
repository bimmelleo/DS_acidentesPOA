import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster


#carregando a base
df = pd.read_csv('cat_acidentes.csv', sep=';')


#limpando valores NaN
df = df.dropna(subset=['latitude', 'longitude'], how='any')


#definindo região com o folium
mapa_um = folium.Map(location = [-30.1, -51.15], zoom_start=11)
mapa_dois = folium.Map(location = [-30.1, -51.15], zoom_start=11)

mapa = folium.Map(location = [-30.1, -51.15], zoom_start=10)


#variavel coordenadas para funcoes de mapa
coordenadas = list(zip(df['latitude'], df['longitude']))


#variaves que recebem as funcoes do Folium
mapa_um_calor = HeatMap(coordenadas, radius=9, blur=10)
mapa_dois_cluster = MarkerCluster(coordenadas)

mapa_calor = HeatMap(coordenadas, radius=9, blur=10)
mapa_cluster = MarkerCluster(coordenadas)


#adicionando os resultados das funcoes nas variaveis de mapa
mapa_um.add_child(mapa_um_calor)
mapa_dois.add_child(mapa_dois_cluster)

mapa.add_child(mapa_calor)
mapa.add_child(mapa_cluster)


#salvando como arquivo html para visualização web
mapa_um.save('map_acid_calor.html')
mapa_dois.save('map_acid_cluster.html')

mapa.save('mapa_union.html')