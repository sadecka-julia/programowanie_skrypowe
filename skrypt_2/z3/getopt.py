import getopt
import sys
import lista
import slownik


def main():

    opts, args = getopt.getopt(sys.argv[1:], "mod:", ["modul="])
    flaga = opts[0][1]

    if flaga == "lista":
        lista.wypisz(sys.argv[2:])
    elif flaga == "slownik":
        slownik.wypisz(sys.argv[2:])
    else:
        exit()


if __name__ == "__main__":
    main()

