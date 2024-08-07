class Especie:
    def __init__(self, name, height, clas, planet, language, characters, eps):
        self.name=name
        self.height=height
        self.clas=clas
        self.planet=planet
        self.language=language
        self.characters=characters
        self.eps=eps
        

    def show(self):
        print()
        print("----------------------------------------------------")
        print(f'Nombre: {self.name}')
        print(f'Altura promedio: {self.height}')
        print(f'Clasificacion: {self.clas}')
        print(f'Planet: {self.planet}')
        print('Personajes de esta especie: ')
        for character in self.characters:
            print(f'-{character}')
        print('Episodios en los que aparece: ')
        for ep in self.eps:
            print(f'-{ep}')


