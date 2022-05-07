from MenuConjunto import Menu
from ClaseConjunto import Conjunto


if __name__ == '__main__':
    print('\n***** Conjuntos *****')
    c1 = Conjunto([1, 2, 3, 4])
    c2 = Conjunto([3, 6, 9])
    menu = Menu()
    menu.opciones(c1, c2)