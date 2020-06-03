import time
from src.SacarGeocode import *

def masivoGeocode(dataframe):
    puntos_geocode=[]
    for direccion in dataframe.adress:
        time.sleep(10)
        puntos_geocode.append(geocode(direccion))
    return puntos_geocode

    
def geocodeGoogleMasivo(dataframe):
    puntos_geocode=[]
    for direccion in dataframe.adress:
        puntos_geocode.append(geocodeGoogle(direccion))
    return puntos_geocode
