import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################
def zapisz(slownik, argv):
    print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    for data in argv:
        if data in slownik:
            slownik[data] += 1
        else:
            slownik[data] = 1
    return slownik

def wypisz(slownik):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    slownik = zapisz(slownik, sys.argv[1:])
    for data, liczba in slownik.items():
        print(f"{data}:{liczba},", end="")

############################################


if __name__ == '__main__':
    print('Załadowano moduł "{0}"'.format(__name__))
    slownik = {}
    wypisz(slownik)
