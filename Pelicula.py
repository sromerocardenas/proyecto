class Pelicula:
    def __init__(self, name, ep, date, o_crawl, director):
        self.name=name
        self.ep=ep
        self.date=date
        self.o_crawl=o_crawl
        self.director=director
#Este metodo muestra los atributos de una pelicula
    def show(self):
        print()
        print("----------------------------------------------------")
        print(f">Titulo: {self.name}")
        print(f">Numero de episodio: {self.ep}")
        print(f">Fecha de lanzamiento: {self.date}")
        print(f">Director: {self.director}")
        print(f">Opening crawl: {self.o_crawl}")
        
