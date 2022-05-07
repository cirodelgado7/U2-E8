class Conjunto:
    __listaConjunto = []

    def __init__(self, lista):
        self.__listaConjunto = lista

    def __str__(self):
        s = " { "
        for lista in self.__listaConjunto:
            s += str(lista) + ' '
        return s + "} "

    def __add__(self, other):
        self.__listaConjunto.sort()
        other.__listaConjunto.sort()
        a = len(self.__listaConjunto)
        b = len(other.__listaConjunto)
        i = 0
        j = 0
        listaFinal = []
        while i < a and j < b:
            if self.__listaConjunto[i] < other.__listaConjunto[j]:
                listaFinal.append(self.__listaConjunto[i])
                i += 1
            elif self.__listaConjunto[i] > other.__listaConjunto[j]:
                listaFinal.append(other.__listaConjunto[j])
                j += 1
            else:
                listaFinal.append(self.__listaConjunto[i])
                i += 1
                j += 1
        if i < a:
            while i < a:
                listaFinal.append(self.__listaConjunto[i])
                i += 1
        if j < b:
            while j < b:
                listaFinal.append(other.__listaConjunto[j])
                j += 1
        return Conjunto(listaFinal)

    def __sub__(self, other):
        listaFinal = []
        for i in self.__listaConjunto:
            if i not in other.__listaConjunto:
                listaFinal.append(i)
        return Conjunto(listaFinal)

    def __eq__(self, otro):
        return self.__listaConjunto == otro.__listaConjunto
