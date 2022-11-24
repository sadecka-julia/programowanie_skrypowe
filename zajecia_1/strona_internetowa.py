import sys  #argv

strona = {}


def dodaj_kanal():
    nazwa = input('Podaj nazwe nowego kanalu: ')
    while nazwa in strona:
        print("Kanal o podanej nazwie istnieje")
        nazwa = input('Podaj nazwe nowego kanalu: ')
    strona[nazwa] = {'artykuly': []}
    print("Dodano kanal!")


def usun_kanal():
    nazwa = input('Podaj nazwe kanalu, ktory chcesz usunac: ')
    while nazwa not in strona:
        print('Kanal o podanej nazwie nie istnieje')
        nazwa = input('Podaj nazwe kanalu, ktory chcesz usunac: ')
    del strona[nazwa]
    print('Usunieto kanal!')


def dodaj_artykul():
    nazwa = input('Podaj nazwe kanalu: ')
    while nazwa not in strona:
        print('Kanal o podanej nazwie nie istnieje')
        nazwa = input('Podaj nazwe kanalu: ')
    tytul = input('Podaj tytul artykulu: ')
    strona[nazwa]['artykuly'].append(tytul)
    print('Dodano artykul!')


def usun_artykul():
    nazwa = input('Podaj nazwe kanalu: ')
    while nazwa not in strona:
        print('Kanal o podanej nazwie nie istnieje')
        nazwa = input('Podaj nazwe kanalu: ')
    print(strona[nazwa]['artykuly'])
    index = int(input('Podaj indeks artykulu ktory chcesz usunac: '))
    del nazwa[index]
    print("Usunieto artykul!")


def wypisz():
    print(strona.items())
    for key in strona:
        print('Kanal:', key, strona[key])


if __name__ == "__main__":
    while True:
        try:
            command = input("dodanie kanalu [a], usuniecie kanalu [b], dodanie artykulu [c], usuniecie artykulu [d]")
            if command == 'a':
                dodaj_kanal()
            elif command == 'b':
                usun_kanal()
            elif command == 'c':
                dodaj_artykul()
            elif command == 'd':
                usun_artykul()
            else:
                print("Podana komenda jest zła, podaj poprawną: ")
        except(EOFError):
            wypisz()
            exit()
