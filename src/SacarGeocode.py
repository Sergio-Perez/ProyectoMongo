import requests
from dotenv import load_dotenv
import os
from geopy.geocoders import GoogleV3
load_dotenv()


api_key_Geo = os.getenv("api_key_Geo2")
api_Google = os.getenv("api_Google")
# Sacar geolocalización con XYZ api
def geocode(address):
    
    res = requests.get(f"https://geocode.xyz/{address}?json=1&auth={api_key_Geo}",params={"json":1})
    data = res.json()
    
    return {
        "type":"Point",
        "coordinates": [ float(data["longt"]),float(data["latt"])]
    }

# Sacar geolocalización con la Api de Google
def geocodeGoogle(address):
    geolocator = GoogleV3(api_key=api_Google)
    direccion = geolocator.geocode(f'{address} ,Madrid, Spain')

    return {
        "type":"Point",
        "coordinates": [ float(direccion.longitude),float(direccion.latitude)]
    }


# Sacar geolocalización con XYZ api en New York

def geocodeNewYork(address):
    '''resp = requests.get("https://geocode.xyz/51.4647,0.0079?json=1&auth=your auth code")
    Use geocode api to do forward geocoding. https://geocode.xyz/api
    '''
    res = requests.get(f"https://geocode.xyz/{address},NewYork?region=USA?json=1&auth={api_key_Geo}",params={"json":1})
    #res = requests.get(f"https://geocode.xyz/{address}",params={"json":1})
    data = res.json()
    print(res)
    # Return as GeoJSON -> https://geojson.org/
    return {
        "type":"Point",
        "coordinates": [ float(data["longt"]),float(data["latt"])]
    }


# Sacar geolocalización con XYZ api en Madrid

    def geocodeMadrid(address):
    '''resp = requests.get("https://geocode.xyz/51.4647,0.0079?json=1&auth=your auth code")
    Use geocode api to do forward geocoding. https://geocode.xyz/api
    '''
    res = requests.get(f"https://geocode.xyz/{address},MADRID?region=ES?json=1&auth={api_key_Geo}",params={"json":1})
    #res = requests.get(f"https://geocode.xyz/{address}",params={"json":1})
    data = res.json()
    print(res)
    # Return as GeoJSON -> https://geojson.org/
    return {
        "type":"Point",
        "coordinates": [ float(data["longt"]),float(data["latt"])]
    }