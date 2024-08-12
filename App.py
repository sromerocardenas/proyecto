from API import *
from Graficos import naves, personajes_por_planeta, tabla_naves
import matplotlib.pyplot as plt
from misiones import *
import json
class App:

#Este es el menu del programa, llama a funciones de otros archivos segun la opcion que escojamos. Para las primeras 3 opciones realiza la carga de los datos y luego los imprime de manera ordenada segun su metodo 
#Se recomienda pedir las primeras 4 opciones para que el programa las cargue al comienzo (una vez se cargan no vuelve a hacer request al API, quedan los datos guardados en la lista)
    def start(self):
        print("Bienvenido a Star Wars Metropedia")
        filmcarga=None
        speccarga=None
        planetcarga=None
        peoplecarga=None
        missions=[]
        while True:
            print()
            menu=int(input('''
-----------------Menu-----------------
    1. Lista de peliculas
    2. Lista de especies 
    3. Lista de planetas
    4. Buscar Personaje
    5. Personajes por su planeta (grafico)
    6. Comparar naves (graficos)
    7. Estadisticas de naves (tablas)
    8. Misiones (submenu misiones)
    9. Salir
    
    ---> '''))
            if menu==1:
                if not filmcarga:
                    print('Por favor espere mientras se cargan los datos del servidor...')
                    filmsmain=cargar_peliculas()
                    filmcarga=True
                for i in filmsmain:
                    i:Pelicula
                    i.show()
            elif menu==2:
                if not speccarga:
                    print('Por favor espere mientras se cargan los datos del servidor...')
                    specmain=cargar_especies()
                    speccarga=True
                for i in specmain:
                    i:Especie
                    i.show()
            elif menu==3:
                if not planetcarga:
                    print('Por favor espere mientras se cargan los datos del servidor...')
                    planetsmain=cargar_planetas()
                    planetcarga=True
                for i in planetsmain:
                    i:Planeta
                    i.show()
            #La cuarta opcion tambien carga los datos, pero en vez de imprimirlos solicita al usuario el nombre del personaje que desea buscar y procede a imprimir los resultados que contengan el input del usuario
            elif menu==4:
                if not peoplecarga:
                    print('Por favor espere mientras se cargan los datos del servidor...')
                    peoplemain=cargar_peronajes()
                    peoplecarga=True
                while True:
                    menuperso=int(input('''Ingrese una opcion:
                                        1. Buscar personajes (a partir de primeras letras del nombre):
                                        2. Salir
                                        ---> '''))
                    if menuperso==1:
                        busq=input('Ingrese nombre o parte de el (todo en minusculas): ')
                        contador=0
                        for i in ver:
                            i:Personaje
                            minus=str(i.name)
                            minus2=minus.lower()
                            if busq in minus2:
                                i.show()
                                contador+=1
                            if contador<1:
                                print('No se encontraron personajes con ese nombre')
                            print(f'-----------{contador} personaje(s) encontrados---------')
                    elif menuperso==2:
                        break
                    else:
                        print('Ingrese una opcion valida !!')
                        print()
                 
            elif menu==5:
                #Esta opcion utiliza los ejes x y y generados como listas y los grafica con el uso de pyplot(libreria matplotlib). Se le asignan nombres a cada eje del grafico y se ajusta la inclinacion de los nombres para que sean legibles
                planetas, personajes=personajes_por_planeta()
                plt.bar(planetas, personajes)
                plt.xlabel('Planetas')
                plt.ylabel('Personajes nacidos en el')
                plt.title('Cantidad de personajes nacidos en cada planeta')
                plt.xticks(rotation=90, ha='right')
                plt.show()
            elif menu==6:
                print()
                opcion=int(input('''Ingrese una caracteristica a comparar:
                                 1. Longitud de la nave
                                 2. Capacidad de carga
                                 3. Clasificacion de hiperimpulsor
                                 4. Modern Galactic Light Time
                                    --->'''))
                if opcion>0 and opcion<5:
                    #Esta parte valida que la opcion sea correcta, y llama a la funcion que generara los ejes del grafico dependiendo de lo escogido por el usuario.
                    ships,yaxis,yname=naves(opcion)
                    plt.bar(ships, yaxis)
                    plt.xlabel('Naves')
                    plt.ylabel(f'{yname}')
                    plt.title('Comparacion de naves')
                    plt.xticks(rotation=90, ha='right')
                    plt.show()
                else: 
                    print('Opcion no valida')
                
            elif menu==7:
                #En esta opcion se solicita al usuario que escoja la caracteristica de naves de la cual desea ver datos estadisticos
                print()
                opciontabla=int(input('''Ingrese la caracteristica de la cual desea ver datos estadisticos:
                                 1. Modern Galactic Light Time
                                 2. Clasificacion de hiperimpulsor
                                 3. Velocidad maxima en la atmosfera
                                 4. Costo en creditos
                                    --->'''))
                if opciontabla>0 and opciontabla<5:
                    #Una vez se haya seleccionado una opcion, imprime una tabla llamando el metodo tabla_naves, que se encuentra en Graficos.py
                    print(tabla_naves(opciontabla))
                else:
                    print('Opcion no valida')
            elif menu==8:
                #Esta opcion abre el submenu misiones, que tiene varias opciones en torno a ellas.
                print()
                while True: 
                    print()
                    misionmenu=int(input('''Por favor ingrese una opcion:
                                         1. Crear mision
                                         2. Modificar mision
                                         3. Ver misiones
                                         4. Guardar misiones (guarda la lista actual de misiones)
                                         5. Cargar misiones (carga las misiones que se encuentren contenidas en misiones.txt)
                                         6. Volver al menu principal
                                         ----> '''))
                    #En primer lugar, se llama al metodo crear_mision y agrega una nueva mision a la lista, si ya se ha alcanzado el maximo de 5 misiones, no permite agregar nuevas
                    if misionmenu==1:
                        print('Crear mision')
                        if len(missions)>4:
                            print('MAXIMO DE MISIONES ALCANZADO')
                            print('--------------------------------------------')
                        else: 
                            newmis=crear_mision()
                            missions.append(newmis)
                    elif misionmenu==2:
                        #Por otra parte, la opcion 2 nos permite seleccionar una mision que queramos modificar, y luego nos muestra un menu con las opcines de modificacion
                        print('Modificar misiones:')
                        print()
                        contadormis=1
                        for mis in missions:
                            mis:Mision
                            print(f'{contadormis}- {mis.nombre}')
                            contadormis+=1
                        while True:
                            selection=int(input('Numero de mision a modificar(valor entero):'))
                            if selection>0 and selection<=len(missions):
                                break
                            else:
                                print('NUMERO DE MISION INVALIDO')
                        selectedmis=missions[selection-1]
                        selectedmis:Mision
                        print()
                        opcionmodmis=int(input('''Ingrese la opcion de modificacion:
                                               1. Cambiar nombre
                                               2. Cambiar planeta destino
                                               3. Cambiar nave
                                               4. Eliminar arma
                                               5. Agregar armas
                                               6. Eliminar personaje
                                               7. Agregar personajes
                                               ---->'''))
                        if opcionmodmis==1:
                            selectedmis.cambiar_nomb()
                        elif opcionmodmis==2:
                            #Esta opcion nos permite cambiar el planeta destino, para ello, se apoya en el metodo de agregar planeta
                            print()
                            newplanet=agg_planeta()
                            selectedmis.planeta=newplanet
                            print()
                            print(f'El nuevo planeta destino es: {selectedmis.planeta}')
                        elif opcionmodmis==3:
                            #Esta opcion nos permite cambiar la nave de la mision, para ello, se apoya en el metodo de agregar nave
                            print()
                            newship=agg_nave()
                            selectedmis.nave=newship
                            print()
                            print(f'La nueva nave es: {selectedmis.nave}')
                        elif opcionmodmis==4:
                            print()
                            selectedmis.delarmas()
                        elif opcionmodmis==5:
                            #Esta opcion nos permite agregar nuevas armas, primero verifica si se ha alcanzado el maximo o el numero a agregar lo sobrepasa, y si no, procede a agregar nuevas con el metodo agg_armas
                            if len(selectedmis.armas)>6:
                                print()
                                print('Ya se ha alcanzado el maximo de armas para la mision')
                            else: 
                                newarmasnumb=int(input('Numero de armas a agregar: '))
                                if newarmasnumb+len(selectedmis.armas)>7:
                                    print('Operacion invalida. Se sobrepasa el maximo de armas de la mision')
                                else:
                                    nuevasarmas=agg_armas(newarmasnumb)
                                    selectedmis.armas+=nuevasarmas
                                    print('Nuevas armas han sido agregadas con exito')
                                    print()
                        elif opcionmodmis==6:
                            print()
                            selectedmis.delgente()
                        elif opcionmodmis==7:
                             #Esta opcion nos permite agregar nuevos personajes, primero verifica si se ha alcanzado el maximo o el numero a agregar lo sobrepasa, y si no, procede a agregar nuevos con el metodo agg_persos
                            print()
                            if len(selectedmis.gente)>6:
                                print()
                                print('Ya se ha alcanzado el maximo de personajes para la mision')
                            else: 
                                newpersosnumb=int(input('Numero de personajes a agregar: '))
                                if newpersosnumb+len(selectedmis.gente)>7:
                                    print('Operacion invalida. Se sobrepasa el maximo de personajes de la mision')
                                else:
                                    nuevospersonajes=agg_persos(newpersosnumb)
                                    selectedmis.gente+=nuevospersonajes
                                    print('Nuevos personajes han sido agregados con exito')
                                    print()
                        else: 
                            print('No se puede modificar la mision. Opcion invalida!!')
                    elif misionmenu==3:
                        #Esta opcion nos muestra de manera agradable las misiones registradas
                        print('Ver misiones')
                        for mis in missions:
                            mis:Mision
                            mis.showmis()
                    elif misionmenu==4:
                        #En primer lugar se crea una lista de misiones en forma de diccionario, con el metodo .diccionario(), alli se agregan cada una de las misiones creadas por el usuario
                        misionesdic=[]
                        print()
                        for mis in missions:
                            mis:Mision
                            misionesdic.append(mis.diccionario())
                     #Ahora utilizando el metodo .dumps de la libreria json, se guardan en un archivo de texto con formato json de manera que sea agradable la lectura, esto es gracias al parametro indent=4, que la hace mas agradable visualmente
                        misionestxt=json.dumps(misionesdic, indent=4)
                        guardado=open('misiones.txt', 'w')
                        guardado.write(misionestxt)
                        guardado.close()
                        print('Sus misiones han sido guardadas con exito')
                    elif misionmenu==5:
                        #Nuevamente usando la libreria json, convertimos el archivo de texto en una lista de diccionarios que posteriormente se convertiran a misiones con el metodo dic_a_mision
                        #De esta manera podemos agregar las misiones contenidas en el txt a nuestra lista de misiones principal
                        print()
                        misionesob=[]
                        datosmis=open('misiones.txt', 'r')
                        misionescarga=json.load(datosmis)
                        for mis in misionescarga:
                            misionesob.append(dic_a_mision(mis))
                        datosmis.close()
                        missions+=misionesob
                        print('Las misiones de misiones.txt han sido cargadas con exito')
                    elif misionmenu==6:
                        break
                    else:
                        print('Por favor ingrese una opcion valida')
                    
            elif menu==9:
                print()
                print("Que la fuerza te acompane...")
                break
            elif menu==None:
                print('INGRESE UNA OPCION VALIDA')
            else:
                print('INGRESE UNA OPCION VALIDA')

