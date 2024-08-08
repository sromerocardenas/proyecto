from Especie import Especie
from Pelicula import Pelicula 
from Personaje import Personaje
from Planeta import Planeta
import requests as rq

#Este metodo carga las peliculas a partir de la api y las devuelve en forma de lista de objetos tipo Pelicula
def cargar_peliculas():
    link='https://swapi.dev/api/films'
    pelis=rq.get(link).json()
    pelis2=pelis['results']
    movies=[]
    for peli in pelis2:
        name=peli['title']
        id=peli['episode_id']
        date=peli['release_date']
        o_crawl=peli['opening_crawl']
        dir=peli['director']
        movies.append(Pelicula(name,id,date,o_crawl,dir))
    return movies

#Este metodo carga las especies a partir de la api y las devuelve en forma de lista de objetos tipo Especie
#En general la estructura de cargar_especies, planetas y personajes utiliza un while true para ir pasando las paginas pues la api por defecto solo muestra la primera pagina
#NOTA: Duran un poco en cargar los datos, en especial cargar_personajes
def cargar_especies():
    species=[]
    link='https://swapi.dev/api/species'
    while True:
        spec=rq.get(link).json()
        spec2=spec['results']
        #Se itera para ir guardando cada elemento de la lista de especies 
        for i in spec2:
            name=i['name']
            height=i['average_height']
            clas=i['classification']
            #Para la especie droide no hay un link guardado en el diccionario, por lo que se hace un condicional que elimine el problema
            if i['name']=='Droid':
                planet='Ninguno'
            else:
                urlplanet=str(i['homeworld'])
                planeta=rq.get(urlplanet).json()
                planet=planeta['name']
            lang=i['language']
            #Finalmente para guardar los datos de los personajes y films, se hace un get nuevamente a los enlaces que muestra en los campos 'people' y 'films' para obtener la info solicitada
            people=[]
            for j in i['people']:
                pers=rq.get(j).json()
                nompe=pers['name']
                people.append(nompe)
            eps=[]
            for k in i['films']:
                film=rq.get(k).json()
                eps.append(film['title'])
                
            species.append(Especie(name,height,clas,planet,lang,people,eps))
        #pasar pagina o cortar ciclo
        if not spec['next']:
            break
        else:
            link=spec['next']
    return species

#Este metodo carga los planetas a partir de la api y los devuelve en forma de lista de Planetas, pasa las paginas igual que cargar_especies y agrega los personajes y films de igual manera
def cargar_planetas():
    planets=[]
    link='https://swapi.dev/api/planets'
    while True:
        planet=rq.get(link).json()
        planet2=planet['results']
        for i in planet2:
            name=i['name']
            orbit=i['orbital_period']
            rotation=i['rotation_period']
            pop=i['population']
            weather=i['climate']
            eps=[]
            for k in i['films']:
                film=rq.get(k).json()
                eps.append(film['title'])
            persos=[]
            for j in i['residents']:
                perso=rq.get(j).json()
                persos.append(perso['name'])
            
            planets.append(Planeta(name,orbit,rotation,pop,weather,eps,persos))
        if not planet['next']:
            break
        else:
            link=planet['next']
    return planets
#Este metodo funciona parecido a los ultimos dos, pero debido a que varios datos que se piden estan en forma de lista, se verfica si hay algun dato en la lista y si ese es el caso se agrega.
#NOTA: Al ser el metodo que mas debe iterar (82 personajes), y buscar bastante informacion en cada iteracion, dura un par de minutos en cargar todos los datos
def cargar_peronajes():
    personajes=[]
    link='https://swapi.dev/api/people'
    while True:
        perso=rq.get(link).json()
        perso2=perso['results']
        for i in perso2:
            name=i['name']
            if not i['homeworld']:
                planet='Ninguno'
            else:
                urlplanet=str(i['homeworld'])
                planeta=rq.get(urlplanet).json()
                planet=planeta['name']
            eps=[]
            for k in i['films']:
                film=rq.get(k).json()
                eps.append(film['title'])
            gndr=i['gender']
            if i['species']==[]:
                specie="N/A"
            else:
                urlspec=rq.get(i['species'][-1]).json()
                specie=urlspec['name']
            nav=[]
            if i['starships']==[]:
                nav.append('N/A')
            else:
                for j in i['starships']:
                    urlnav=rq.get(j).json()
                    nav.append(urlnav['name'])
            veh=[]
            if i['vehicles']==[]:
                veh.append('N/A')
            else:
                for o in i['vehicles']:
                    urlveh=rq.get(o).json()
                    veh.append(urlveh['name'])
            personajes.append(Personaje(name,planet,eps,gndr,specie,nav,veh))            
        if not perso['next']:
            break
        else:
            link=perso['next']
    return personajes