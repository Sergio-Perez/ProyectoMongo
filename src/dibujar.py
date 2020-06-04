import folium
import folium.plugins
from src.buscarOficinas import *



query = getBuscar("RETIRO Madrid",4000)
coordenadasMadrid = query["Lugares"]["$near"]["$geometry"]['coordinates']

def etiquetar(cordenadas, nombre = "?",color="blue"):    
    m = folium.Map(location=[coordenadasMadrid[1],coordenadasMadrid[0]],zoom_start=12, tiles='OpenStreetMap')
    cluster = folium.plugins.MarkerCluster().add_to(m)
    
    for names,latlong in zip(nombre,cordenadas): 
        if latlong != None:
            folium.Marker(
            location=[latlong["coordinates"][1],latlong["coordinates"][0]],
            popup =names,
            icon=folium.Icon(icon='ok-sign',color=color)
            ).add_to(m)

    return m     