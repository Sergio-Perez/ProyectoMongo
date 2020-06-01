import requests
from dotenv import load_dotenv
load_dotenv()
import os
api_key_Geo = os.getenv("api_key_Geo2")

def geocode(address):
    
    res = requests.get(f"https://geocode.xyz/{address}?json=1&auth={api_key_Geo}",params={"json":1})
    data = res.json()
    
    return {
        "type":"Point",
        "coordinates": [ float(data["longt"]),float(data["latt"])]
    }