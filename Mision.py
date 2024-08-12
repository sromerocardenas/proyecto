
class Mision:
    def __init__(self, nombre, planeta, nave, armas, gente):
        self.nombre=nombre
        self.planeta=planeta
        self.nave=nave
        self.armas=armas
        self.gente=gente

#Este metodo muestra los atributos de una mision determinada
    def showmis(self):
        print()
        print(f'Nombre: {self.nombre}')
        print(f'Planeta destino: {self.planeta} ')  
        print(f'Nave: {self.nave}')
        print('Armas:')
        for i in self.armas:
            print(f'-{i}')
        print('Personajes:')
        for j in self.gente:
            print(f'-{j}')
        print()
  #Este metodo elimina un arma seleccionada de la lista de armas de la mision, para ello solicita al usuario seleccionar una opcion y posteriormente se elimina la misma de la propia lista  
    def delarmas(self):
        print('Armas:')
        cont=1
        for i in self.armas:
            print(f'{cont}-{i}')
            cont+=1
        while True:
            opc=int(input('Numero de arma a eliminar: '))
            if opc>0 and opc<=len(self.armas):
                break
            else:
                print('Numero invalido')
        armadel=self.armas[opc-1]
        self.armas.remove(armadel)
        print()
        print('ARMA ELIMINADA CON EXITO')
        print()
#Este metodo, es igual al anterior en su funcionamiento, solo que en este caso no se trata de armas si no de personajes de la mision
    def delgente(self):
        print('Personajes:')
        cont=1
        for i in self.gente:
            print(f'{cont}-{i}')
            cont+=1
        while True:
            opc=int(input('Numero de personaje a eliminar: '))
            if opc>0 and opc<=len(self.gente):
                break
            else:
                print('Numero invalido')
        persodel=self.gente[opc-1]
        self.gente.remove(persodel)
        print()
        print('PERSONAJE ELIMINADO CON EXITO')
        print()

    
    #Este metodo permite modificar el nombre asignado a la mision
    def cambiar_nomb(self):
        print()
        newname=input('Ingrese el nuevo nombre: ')
        self.nombre=newname
        print(f'El nuevo nombre es: {self.nombre}')
    #Este metodo convierte un objeto de tipo mision en un diccionario, con el objetivo de guardarse posteriormente en un archivo txt
    def diccionario(self):
        return {
            "nombre":self.nombre,
            "planeta":self.planeta,
            "nave":self.nave,
            "armas":self.armas,
            "gente":self.gente
        }

    
