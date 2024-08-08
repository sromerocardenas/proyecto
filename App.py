from API import *
from Graficos import naves, personajes_por_planeta
import matplotlib.pyplot as plt
class App:

#Este es el menu del programa, llama a funciones de otros archivos segun la opcion que escojamos. Para las primeras 3 opciones realiza la carga de los datos y luego los imprime de manera ordenada segun su metodo 
    def start(self):
        print("Bienvenido a Star Wars Metropedia")

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
    7. Estadisticas de naves
    8. Misiones
    9. Salir
    
    ---> '''))
            if menu==1:
                ver=cargar_peliculas()
                for i in ver:
                    i:Pelicula
                    i.show()
            elif menu==2:
                ver=cargar_especies()
                for i in ver:
                    i:Especie
                    i.show()
            elif menu==3:
                ver=cargar_planetas()
                for i in ver:
                    i:Planeta
                    i.show()
            #La cuarta opcion tambien carga los datos, pero en vez de imprimirlos solicita al usuario el nombre del personaje que desea buscar y procede a imprimir los resultados que contengan el input del usuario
            elif menu==4:
                ver=cargar_peronajes()
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
                    print('activo')
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
                print()
            elif menu==8:
                print()
            elif menu==9:
                print()
                print("Que la fuerza te acompane...")
                break
            elif menu==None:
                print('INGRESE UNA OPCION VALIDA')
            else:
                print('INGRESE UNA OPCION VALIDA')

