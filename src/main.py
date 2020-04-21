from bs4 import BeautifulSoup
from urllib.request import urlopen
from pymongo import MongoClient
import pandas as pd
import requests
import os
import folium
import json
from dotenv import load_dotenv
load_dotenv()
from BuscarGeooficias import *
from SacarGeocode import *
from LugaresCerca import *
from LatLong import *
from SacarDireccion import *
from MasivoGeocoe import *
#Cargo mongodb y le añado Datamad0320
client = MongoClient("mongodb://localhost/datamad0320")
db = client.get_database()

#organizo de DataFrame companias
all_offices = list(db.ejercicios.find({},{"offices":1,"name":1,"category_code":1}))

#Hago un explode y añado las columnas.
companias = pd.DataFrame (all_offices )
companias = companias.explode("offices")

#Busco Geooficinas
limpias_offices = companias.apply(buscaroficinaGeoPoint,axis=1, result_type="expand")
limpias_offices.columns = ["office","clean_state"]

#Concateno las columnas
companias_limpias= pd.concat([companias,limpias_offices], axis=1)

#Elijo las columnas que deseo
companias_limpias = companias_limpias[["name","category_code","office","clean_state"]]

#Reno,bro las columnas
companias_limpias.rename(columns={'office':'Lugares'}, inplace=True)

#Exporto a un json el dataframe
companias_limpias.to_json("../Input/companias_limpias.json",orient="records")

#Le doy una variable a la apikey de geocode.xyz
api_key_Geo = os.getenv("api_key_Geo2")


#Saco los lugares cerca de mis oficinas dependiendo de la zona elejida

query = getOfficeNear("Centro Madrid")
cur = db.mongo_project.find(query, {"_id":0})
print(cur.count())
result = list(cur)

#Convierto en un DataFrame el result loconcateno con los resultados y renombro las columnas
df = pd.DataFrame(result)

df_conGeo = pd.concat([df, df.apply(easyLatLng, axis=1, result_type="expand")], axis=1)
df_conGeo.rename(columns={'office':'Lugares'}, inplace=True)

#Lo exporto a un .json a la carpeto Input
df_conGeo.to_json("../Input/companiasMadridconGeo.json",orient="records")

#Elijo las columnas de trabajo de mi DataFrame
df=["latitude","longitude","name"]
conGeo2 = df_conGeo[df]

#Haciendo Web Scraping saco la direción y los nombres de lo que busco
#guarderiasretiro = ExtractDireccion("madrid retiro","guarderias", 2)
#aeropuerto = ExtractDireccion("madrid","aeropuerto", 1)
#starbucks = ExtractDireccion("madrid retiro","starbucks", 1)

#Convierto en DataFrame esos datos(esta parte la dejo comentada ya que desde mi conexión no puedo volver a usarla ya que me tienen baneado por exceso de uso)


#Importo los archivos ya guardados en Input
with open('../Input/guarderiasDireccion.json', 'r') as myfile:
       guarderiasretiroDatos=myfile.read()

with open('../Input/starbucksDireccion.json', 'r') as tofile:
       starbucksDatos= tofile.read()
with open('../Input/aeropuertoDireccion.json', 'r') as sufile:
       aeropuertoDatos = sufile.read()

    
#Los datos los meto en variables
aeropuertoDatos = pd.read_json(aeropuertoDatos)
starbucksDatos =pd.read_json(starbucksDatos)
guarderiasretiroDatos =pd.read_json(guarderiasretiroDatos)

#Renombro las columnas con name y adress
aeropuertoDatos = aeropuertoDatos.rename(columns={0:'name',1:'adress'})
starbucksDatos= starbucksDatos.rename(columns={0:'name',1:'adress'})
guarderiasretiroDatos = guarderiasretiroDatos.rename(columns={0:'name',1:'adress'})

#Elimino las filas que no coinciden con un aeropuerto
aeropuertoDatos.drop(aeropuertoDatos.index[[0,2,4,6,7]],inplace=True)

#Elimino la fila con dos direcciones parejas
guarderiasretiroDatos.drop(guarderiasretiroDatos.index[[17]],inplace=True)

#Elimino la fila con el Starbucks cerrado
starbucksDatos.drop(starbucksDatos.index[[4]],inplace=True)

#Con la función Geocode pido los puntos geospatial
aeropuertoGeocode= masivoGeocode(aeropuertoDatos)
guarderiasretirogeo = masivoGeocode(guarderiasretiroDatos)
starbucksgeo = masivoGeocode(starbucksDatos)

#Meto en un DataFrame lso datos
df_starbucksgeo = pd.DataFrame(starbucksgeo)
df_guarderiasgeo= pd.DataFrame(guarderiasretirogeo)
df_aeropuertosgeo= pd.DataFrame(aeropuertoGeocode)


#Organizo el indice de guarderiasDatos y uno los DataFrame.
guarderiasretiroDatos = guarderiasretiroDatos.reset_index()
df_guarderias = pd.concat([df_guarderiasgeo, df_guarderiasgeo.apply(easyLatLng2, axis=1, result_type="expand")], axis=1)
df_guarderias2 = pd.concat([guarderiasretiroDatos,df_guarderias], axis=1) 

#Organizo el indice de aeropuertoDatos y uno los DataFrame.
aeropuertoDatos = aeropuertoDatos.reset_index()
df_aeropuertos = pd.concat([df_aeropuertosgeo, df_aeropuertosgeo.apply(easyLatLng2, axis=1, result_type="expand")], axis=1)
df_aeropuertos2 = pd.concat([aeropuertoDatos,df_aeropuertos], axis=1) 

#Organizo el indice de starbucksDatos y uno los DataFrame.
starbucksDatos = starbucksDatos.reset_index()
df_starbucks = pd.concat([df_starbucksgeo, df_starbucksgeo.apply(easyLatLng2, axis=1, result_type="expand")], axis=1)
df_starbucks2 = pd.concat([starbucksDatos,df_starbucks], axis=1) 

#cambio a lugares el nombre de la columna
df_starbucks3 =pd.concat([df_starbucks2,(pd.DataFrame({'Lugares': starbucksgeo},index= df_starbucks2.index ))],axis=1)
                                                      
df_guarderias3 =pd.concat([df_guarderias2,(pd.DataFrame({'Lugares': guarderiasretirogeo},index= df_guarderias2.index ))],axis=1)   
                                                                                                           
df_aeropuertos3 =pd.concat([df_aeropuertos2,(pd.DataFrame({'Lugares': aeropuertoGeocode},index= df_aeropuertos2.index ))],axis=1)

#Elimino la columna de index que salio de más.
df_starbucks3 = df_starbucks3.drop(['index','type','coordinates'], axis=1)
df_aeropuertos3 = df_aeropuertos3.drop(['index','type','coordinates'], axis=1)
df_guarderias3 = df_guarderias3.drop(['index','type','coordinates'], axis=1)

#Genero unos .json con los datos
df_starbucks3.to_json("./Input/Starbucks.json",orient="records")
df_aeropuertos3.to_json("./Input/aeropuertos.json",orient="records")
df_guarderias3.to_json("./Input/guarderias.json",orient="records")

#Busco los lugares cerca de Madrid que tengo en mis json desde mongodb
#Vuelvo a buscar la query de Madrid zona Retiro
query = buscarLugaresCerca("Madrid Retiro")
cur = db.colleccion.find(query, {"_id":0})

print(cur.count())
result = list(cur)
print(result)
                                                        