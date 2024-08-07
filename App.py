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
                print()
            elif menu==4:
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
                break

