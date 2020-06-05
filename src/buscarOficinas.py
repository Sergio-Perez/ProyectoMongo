
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



def comprobarDistancias(listaDirecciones,coleccion,distancia=1000):
    resultados = []
    solucion = []
    diccio ={}
    for e in listaDirecciones:
        query={ "coordenadas": {
              "$near": {
              "$geometry": {'type': 'Point',
                            'coordinates': e["coordinates"]},
              "$maxDistance": distancia,
                        }
          }}
        resultados.append(query)
        for query in resultados:
            result = coleccion.find(query)
            result2 = list(result)

            if result2 != []:            
                solucion.append(result2)
                diccio[(f'{query["coordenadas"]["$near"]["$geometry"]["coordinates"]}')] = result2

            if solucion == []:
                print("No hay resultados para esa distancia")
        #d = [i[0] for n, i in enumerate(solucion) if i not in solucion[n + 1:]] 
    return diccio