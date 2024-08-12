import csv
from Mision import Mision
#Este metodo nos permite seleccionar un planeta de la lista de planetas, para ello utiliza csv.DictReader para organizar la info del archivo y poder extraer los nombres de los planetas en una lista
#Luego permite al usuario seleccionar una opcion y se retorna el nombre seleccionado
def agg_planeta():
    planetas=open('planets.csv', 'r')
    planetas_ord=csv.DictReader(planetas)
    contador_planet=1
    listaplanetas=[]
    print('Seleccione el planeta destino: ')
    for i in planetas_ord:
        print(f'{contador_planet}- {i['name']}')
        contador_planet+=1
        listaplanetas.append(i['name'])
    print()
    while True:
        nplaneta=int(input('Planeta destino numero(ingrese valores enteros):'))
        if nplaneta>0 and nplaneta<14:
            break
        else:
            print('Planeta invalido')
    planetselecc=listaplanetas[nplaneta-1]
    planetas.close()
    return planetselecc
#Al igual que el metodo anterior, crea una lista con los nombres de las naves a partir del archivo csv y permite al usuario escoger una de ellas
def agg_nave():
    naves=open('starships.csv', 'r')
    naves_ord=csv.DictReader(naves)
    print()
    contador_nave=1
    listanaves=[]
    print('Seleccione la nave: ')
    for i in naves_ord:
        print(f'{contador_nave}- {i['name']}')
        contador_nave+=1
        listanaves.append(i['name'])
    print()
    while True:
        nnave=int(input('Nave numero(ingrese un valor entero):'))
        if nnave>0 and nnave<61:
            break
        else:
            print('Numero de nave invalido')
    naveselecc=listanaves[nnave-1]
    naves.close()
    return naveselecc
#Este metodo es muy parecido a los anteriores. Se diferencia de ellos en que no retorna un solo dato sino una lista de ellos, es decir, una lista de armas a partir del numero de armas que desee el usuario
def agg_armas(cantidad):
    armas=open('weapons.csv', 'r')
    armas_ord=csv.DictReader(armas)
    print()
    print('Lista de armas: ')
    listaarmas=[]
    weapons=[]
    contador_armas=1
    for i in armas_ord:
        print(f'{contador_armas}- {i['name']}')
        contador_armas+=1
        listaarmas.append(i['name'])
    agg=0
    print()
    while agg<cantidad:
        while True:
            narma=int(input(f'Arma #{agg+1}(ingrese valor entero): '))
            if narma>0 and narma<61:
                break
            else:
                print('Numero de arma invalido')
        weapons.append(listaarmas[narma-1])
        agg+=1
    armas.close()
    return weapons

#Al igual que el anterior, a partir de la cantidad solicitada por el usuario devuelve una lista de personajes a seleccionar por conveniencia
def agg_persos(cantidad):
    persos=open('characters.csv', 'r')
    persos_ord=csv.DictReader(persos)
    print()
    print('Lista de personajes: ')
    listapersos=[]
    characters=[]
    contador_persos=1
    for i in persos_ord:
        print(f'{contador_persos}- {i['name']}')
        contador_persos+=1
        listapersos.append(i['name'])
    agg=0
    print()
    while agg<cantidad:
        while True:
            nperso=int(input(f'Personaje #{agg+1}(ingrese valor entero): '))
            if nperso>0 and nperso<97:
                break
            else:
                print('Numero de personaje invalido')
        characters.append(listapersos[nperso-1])
        agg+=1
    persos.close()
    return characters
#Este metodo se apoya en los anteriores para crear un objeto del tipo mision, y lo devuelve con todos sus atributos
def crear_mision():
    nombre=input('Por favor ingrese el nombre de la mision: ')
    print()
    planeta=agg_planeta()
    nave=agg_nave()
    while True:
        armasqtty=int(input('Ingrese el numero de armas a agregar (7 max): '))
        if armasqtty>0 and armasqtty<8:
            break
        else: 
            print('Numero de armas invalido')
    armas=agg_armas(armasqtty)
    while True:
        persosqtty=int(input('Ingrese el numero de personajes a agregar (7 max): '))
        if persosqtty>0 and persosqtty<8:
            break
        else: 
            print('Numero de personajes invalido')
    persos=agg_persos(persosqtty)
    mision=Mision(nombre,planeta,nave,armas,persos)
    print()
    print('Mision creada con EXITO')

    return mision
#Este metodo es utilizado para convertir un diccionario en un objeto de tipo mision
def dic_a_mision(dic):
    return Mision(dic['nombre'],dic['planeta'],dic['nave'],dic['armas'],dic['gente'])


