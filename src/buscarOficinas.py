
from src.SacarGeocode import *


def getBuscar(address, maxDist=1000):
    point = geocodeMadrid(address)
    return {
       "Lugares": {
         "$near": {
           "$geometry": point,
           "$maxDistance": maxDist,
         }
       }
    }