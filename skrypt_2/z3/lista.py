import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################


def zapisz(lista):
    print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    wszystkie = []
    temp_lista = lista
    for i in range(len(temp_lista)):
        temp_lista[i] = str(temp_lista[i])
    temp_lista.sort()
    while len(temp_lista) > 1:
        amount = 1
        while len(temp_lista) > 1 and temp_lista[1] == temp_lista[0]:
            del temp_lista[1]
            amount += 1
        wszystkie.append(temp_lista[0])
        del temp_lista[0]
        wszystkie.append(amount)
    return wszystkie


def wypisz(lista):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    arr = zapisz(lista)
    print('"', sep='', end='')
    i = 1
    while i <= len(arr)-1:
        print(arr[i-1], ':', arr[i], ',', sep='', end='')
        i += 2
    print('"')


if __name__ == '__main__':
    print('Załadowano moduł "{0}"'.format(__name__))
    lista = []
    # print(zapisz(sys.argv[1:]))
    wypisz(sys.argv[1:])
