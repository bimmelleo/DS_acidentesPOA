import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv('cat_acidentes.csv', sep=';')
df = df.dropna(subset=['latitude', 'longitude'])

mapa = folium.Map(location = [-30.1, -51.15], zoom_start=11)

coordenadas = list(zip(df['latitude'], df['longitude']))

mapa_calor = HeatMap(coordenadas)
mapa.add_child(mapa_calor)

mapa.save('mapa_acidentes.html')



