import sys
import lista
import slownik

if __name__ == '__main__':
    if sys.argv[1:] == '--lista':
        lista.wypisz(sys.argv[2:])

    if sys.argv[1:] == '--slownik':
        slownik.wypisz(sys.argv[2:])

    else:
        quit()
