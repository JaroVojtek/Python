import folium
import pandas

map = folium.Map(location=[58,-99],zoom_start=6, tiles="Mapbox Bright")
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation > 3000 :
        return 'red'
    elif elevation > 1000 :
        return 'orange'
    else:
        return 'green'

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el)+" m",
    fill_color = color_producer(el), radius = 10))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding = 'utf-8-sig'),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
