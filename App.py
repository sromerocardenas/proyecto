from API import *

class App:

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
                print()
            elif menu==6:
                print()
            elif menu==7:
                print()
            elif menu==8:
                print()
            elif menu==9:
                print("Que la fuerza te acompane...")
                break
            elif menu==None:
                print('INGRESE UNA OPCION VALIDA')
            else:
                print('INGRESE UNA OPCION VALIDA')

