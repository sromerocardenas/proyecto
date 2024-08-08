class Personaje:
    def __init__(self, name, planet, eps, gndr, species, ships, vehicles):
        self.name=name
        self.planet=planet
        self.eps=eps
        self.gndr=gndr
        self.species=species
        self.ships=ships
        self.vehicles=vehicles
#Este metodo muestra los atributos de un personaje
    def show(self):
        print()
        print("----------------------------------------------------")
        print(f'Nombre: {self.name}')
        print(f'Planeta: {self.planet}')
        print('Episodios en los que aparece: ')
        for ep in self.eps:
            print(f'-{ep}')
        print(f'Genero: {self.gndr}')
        print(f'Especie: {self.species}')
        print('Naves que utiliza: ')
        for ship in self.ships:
            print(f'-{ship}')
        print('Vehiculos que utiliza: ')
        for veh in self.vehicles:
            print(f'-{veh}')   
