![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# ProyectoMongo
En este proyecto vamos a buscar una localización para mi empresa de Gamer que vamos a hipotizar que vamos a crear.


![Imagen mapa](https://cdni.rt.com/actualidad/public_images/2015.01/original/54b519f272139e17538b45b0.jpg)


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
Como con geocode.xyz no me da una geolocalización con la que estoy satisfecho uso la API de Google para ello.
Inserto los datos en Mongodb y los indexo en GEOSPHERE.

## Busco la proximidad entre estas opciones:
Por medio de Querys y de MongoDB usando el indice Geoespacial miro las distancias entre ellos.

Como solo me sale una coincidencia no tengo que probar más para Madrid.

Siendo el resultado.


<img src="/Input/imagenes/resultadoColocacionEmpresa.html" width="100">


