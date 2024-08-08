class Planeta:
    def __init__(self, name, orbit, rotation, pop, weather, eps, characters):
        self.name=name
        self.orbit=orbit
        self.rotation=rotation
        self.pop=pop
        self.weather=weather
        self.eps=eps
        self.characters=characters

#Este metodo muestra los atributos de un planeta
    def show(self):
        print()
        print("----------------------------------------------------")
        print(f'Nombre: {self.name}')
        print(f'Periodo de orbita: {self.orbit}')
        print(f'Periodo de rotacion: {self.rotation}')
        print(f'Poblacion: {self.pop} habitantes')
        print(f'Tipo de clima: {self.weather}')
        print('Episodios en los que aparece: ')
        for ep in self.eps:
            print(f'-{ep}')
        print('Personajes nacidos en el: ')
        for i in self.characters:
            print(f'-{i}')

