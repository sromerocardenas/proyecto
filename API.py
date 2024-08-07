from Especie import Especie
from Pelicula import Pelicula 
from Personaje import Personaje
from Planeta import Planeta
import requests as rq

#Este metodo carga las peliculas a partir de la api y las devuelve en forma de lista de objetos tipo Pelicula
def cargar_peliculas():
    link='https://www.swapi.tech/api/films'
    pelis=rq.get(link).json()
    pelis2=pelis['result']
    movies=[]
    for peli in pelis2:
        name=peli['properties']['title']
        id=peli['properties']['episode_id']
        date=peli['properties']['release_date']
        o_crawl=peli['properties']['opening_crawl']
        dir=peli['properties']['director']
        movies.append(Pelicula(name,id,date,o_crawl,dir))
    return movies

#Este metodo carga las especies a partir de la api y las devuelve en forma de lista de objetos tipo Especie
def cargar_especies():
    link='https://www.swapi.tech/api/species'
    spec=rq.get(link).json()
    spec2=spec['results']
    species=[]
    #Como aca muestra los links de la info de cada especie por separado, se procede a hacer un get por cada una para obtener el resto de info
    for i in spec2:
        name=i['name']
        layer=rq.get(i['url']).json()
        layer2=layer['result']
        height=layer2['properties']['average_height']
        clas=layer2['properties']['classification']
        planeturl=rq.get(layer2['properties']['homeworld']).json()
        planet=planeturl['result']['properties']['name']
        lang=layer2['properties']['language']
        people=[]
        for j in layer2['properties']['people']:
            pers=rq.get(j).json()
            nompe=pers['result']['properties']['name']
            people.append(nompe)
        #Finalmente se verifica si el link de la especie pertenece a algun episodio y se agrega el nombre del mismo a la lista eps
        eps=[]
        linkfilm='https://www.swapi.tech/api/films'
        films=rq.get(linkfilm).json()
        filmes=films['result']
        for filme in filmes:
            if i['url'] in filme['properties']['species']:
                eps.append(filme['properties']['title'])

        species.append(Especie(name,height,clas,planet,lang,people,eps))

    return species
