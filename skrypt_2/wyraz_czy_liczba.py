
tekst = "12131julia"


def wyraz_czy_liczba(tekst):
    temp_wyrazy = []
    temp_liczby = []
    wyrazy = ""
    liczby = ""

    for i in range(len(tekst)):
        try:
            int(tekst[i])
            temp_liczby.append(tekst[i])
        except:
            temp_wyrazy.append(tekst[i])

    for i in range(len(temp_wyrazy)):
        wyrazy += temp_wyrazy[i]
    for i in range(len(temp_liczby)):
        liczby += temp_liczby[i]

    return (wyrazy, liczby)


if __name__ == '__main__':
    while True:
        try:
            wyrazy, liczby = wyraz_czy_liczba(input())
            if len(wyrazy) != 0:
                print("Wyrazy:", wyrazy)
            if len(liczby) != 0:
                print("Liczby:", liczby)
        except(EOFError):
            exit()
