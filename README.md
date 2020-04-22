# ProyectoMongo
En este proyecto vamos a buscar una localización para mi empresa de Gamer que vamos a hipotizar que vamos a crear.



## Desde un json de compañias vamos a empezar el análisis.
Primero seleciono una ubicación, como yo vivo en Madrid. Busco las empresas tecnológicas que vienen en el archivo que hemos limpiado y actualizado.

## Nos piden unos requisitos para la ubicación de nuestra empresa.
Los criterio que voy a coger son:
    --> Guarderias cercanas.
    --> Starbukcs
    --> Aeropuertos.
## Buscar información:
Haciendo web scraping saco las direcciones de los starbucks, guarderias y aeropuertos.
Los cruzo con la api de geocode.xyz despues de coger una Api key para poder realizar más repido las peticiones.

Inserto los datos en Mongodb y los indexo.

Y busco las hubicaciones de los lugares.

Como no encuentro ninguno cambio las geolocalizaciones,
 Y cambio a otra zona de busqueda ya que eso no me funciona y busco en New York
 por ser una de las mayores ciudades del mundo.
 Saco las direciones de guarderias, aeropuertos, restaurantes veganos y Starbucks.
 Y hay ya no me dejo exportar los json, o Mongos no me dejaba Indexar en modo geoespacial. 