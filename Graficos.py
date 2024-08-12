import csv
import pandas as pd
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
    #Finalmente se repite el proceso de generar ejes para las demas opciones de comparar naves
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

#Este metodo permite calcular la moda a partir de una lista de valores. Al igual que en el grafico de personajes por planeta, crea un diccionario que nos dice cuantas veces se repite cada valor.
#Luego extrae del diccionario el valor mas repetido y lo retorna. 
def moda(lista):
    aparece={}
    for i in lista:
        if not i in aparece:
            aparece[i]=1
        else:
            aparece[i]+=1
    apariciones=list(aparece.values())
    valores=list(aparece.keys())
    elemento=apariciones.index(max(apariciones))
    moda=valores[elemento]
    return moda

#Finalmente, este metodo nos permite, a partir de la opcion seleccionada por el usuario, crear un dataframe con la libreria pandas. Retorna la tabla que haya seleccionado el usuario.
#Como puede observarse los datos se extraen de forma similar a como se ha venido haciendo, pero esta vez son agregados a una lista especifica para cada atributo, verificando que haya un valor existente.
#Luego a partir de las listas creadas, se calculan datos estadisticos como promedio (sum/len), moda (metodo anterior) y finalmente max y min (con sus funciones respectivas)
def tabla_naves(opcion):
    data=open('starships.csv', 'r')
    ordenado=csv.DictReader(data)
    mglt=[]
    cost=[]
    maxspeed=[]
    hyperdrive=[]
    for i in ordenado:
        if i['MGLT']:
            mglt.append(float(i['MGLT']))
        if i['cost_in_credits']:
            cost.append(float(i['cost_in_credits']))
        if i['max_atmosphering_speed']:
            maxspeed.append(float(i['max_atmosphering_speed']))
        if i['hyperdrive_rating']:
            hyperdrive.append(float(i['hyperdrive_rating']))
    data.close()

    if opcion==1:
        mgltpromedio=sum(mglt)/len(mglt)
        datos={
            "Dato": ["Promedio","Moda","Maximo","Minimo"],
            "MGLT":[mgltpromedio,moda(mglt),max(mglt),min(mglt)]
        }
    if opcion==2:
        hyperpromedio=sum(hyperdrive)/len(hyperdrive)
        datos={
            "Dato": ["Promedio","Moda","Maximo","Minimo"],
            "Hiperimpulsor":[hyperpromedio,moda(hyperdrive),max(hyperdrive),min(hyperdrive)]
        }
    if opcion==3:
        maxspeedpromedio=sum(maxspeed)/len(maxspeed)
        datos={
            "Dato": ["Promedio","Moda","Maximo","Minimo"],
            "Velocidad":[maxspeedpromedio,moda(maxspeed),max(maxspeed),min(maxspeed)]
        }
    if opcion==4:
        costpromedio=sum(cost)/len(cost)
        datos={
            "Dato": ["Promedio","Moda","Maximo","Minimo"],
            "Costo":[costpromedio,moda(cost),max(cost),min(cost)]
        }

    tabla=pd.DataFrame(datos)
    return tabla
    