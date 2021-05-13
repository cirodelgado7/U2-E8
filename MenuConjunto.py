import sys

class Menu:
    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.union,
            2: self.diferencia,
            3: self.igualdad,
            4: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, c1,c2):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(c1,c2)

    def union(self, c1, c2):
        print(c1 + c2)

    def diferencia(self, c1, c2):
        print(c1 - c2)

    def igualdad(self, c1, c2):
        igualdad = c1 == c2
        if igualdad:
            print('Los conjuntos son iguales')
        else:
            print('Los conjuntos no son iguales')

    def salir(self, c1,c2):
        sys.exit(0)