from MenuConjunto import Menu
from ClaseConjunto import Conjunto

if __name__ == '__main__':
    print('\n***** Conjuntos *****')
    c2 = Conjunto([1, 2, 3, 4, 5, 6])
    c1 = Conjunto([2, 4, 6, 8, 10])
    print(c1)
    print(c2)
    menu = Menu()
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print("1 - Union")
        print("2 - Diferencia")
        print("3 - Igualdad")
        print("4 - Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, c1, c2)