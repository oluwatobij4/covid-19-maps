import pandas as pd
import folium as folium
data = pd.read_csv('time.csv')
pd.set_option('display.max_colwidth', -1)
m = folium.Map(location = [0,0], tiles = 'Stamen Toner', zoom_start = 2 )
for i in range(0,len(data)):
        popUp = folium.Popup(data.iloc[i]['link'])
        folium.Marker([data.iloc[i]['latitude'], data.iloc[i]['longitude']], popup=popUp ).add_to(m)
   m