import csv
#Esta funcion genera listas que vienen siendo los ejes x y y del grafico de personas por planeta
#Con el uso de la libreria csv, se leen los datos del archivo y .DictReader convierte cada fila del archivo en un diccionario para poder extraer la informacion de manera ordenada
#Luego se va agregando cada planeta al diccionario planetas, y se suman la cantidad de personajes nacidos en el

def personajes_por_planeta():
    planetas={}
    data=open('characters.csv', 'r')
    ordenado=csv.DictReader(data)
    for i in ordenado:
        planeta=i['homeworld']
        if not planeta in planetas:
            planetas[planeta]=1
        else:
            planetas[planeta]+=1
    planets=list(planetas.keys())
    cantidad_personajes=list(planetas.values())
    data.close()
    return planets, cantidad_personajes
        
#Por otra parte, esta funcion parte de la opcion escogida por el usuario, y genera un eje x y un eje y(que depende de la opcion escogida)
def naves(opcion):
    naves={}
    data=open('starships.csv', 'r')
    ordenado=csv.DictReader(data)
    if opcion==1:
        for i in ordenado:
            nave=i['name']
            #Los valores de y son guardados en forma de float para luego ser ordenados y que el grafico tenga sentido.
            naves[nave]=float(i['length'])
        navesorden=dict(sorted(naves.items(),key=lambda x: x[1]))
        ships=list(navesorden.keys())
        lengths=list(navesorden.values())
        data.close()
        yaxis=lengths
        yname='Longitud'
    #Se repite el procedimiento para el resto de opciones, esto solo cambia el dato que va a extraer (Longitud, carga, etc)
    elif opcion==2:
        for i in ordenado:
            nave=i['name']
            #Debido a que algunos espacios estan vacios, este condicional convierte esos vacios en 0 para que puedan leerse en forma de float
            if not i['cargo_capacity']:
                naves[nave]=float(0)
            else:
                naves[nave]=float(i['cargo_capacity'])
        navesorden=dict(sorted(naves.items(),key=lambda x: x[1]))
        ships=list(navesorden.keys())
        capacity=list(navesorden.values())
        data.close()
        yaxis=capacity
        yname='Capacidad de carga'
    elif opcion==3:
        for i in ordenado:
            nave=i['name']
            if not i['hyperdrive_rating']:
                naves[nave]=float(0)
            else:
                naves[nave]=float(i['hyperdrive_rating'])
        navesorden=dict(sorted(naves.items(),key=lambda x: x[1]))
        ships=list(navesorden.keys())
        hyperd=list(navesorden.values())
        data.close()
        yaxis=hyperd
        yname='Clasificacion de hiperimpulsor'
    elif opcion==4:
        for i in ordenado:
            nave=i['name']
            if not i['MGLT']:
                naves[nave]=float(0)
            else:
                naves[nave]=float(i['MGLT'])
        navesorden=dict(sorted(naves.items(),key=lambda x: x[1]))
        ships=list(navesorden.keys())
        mglt=list(navesorden.values())
        data.close()
        yaxis=mglt
        yname='Modern Galactic Light Time'
    return ships, yaxis, yname