

class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __setitem__(self, key, value):
        if key == 'suma':
            Operacje.argumentySuma = value
        elif key == 'roznica':
            Operacje.argumentyRoznica = value

    @staticmethod
    def argumenty(arg):
        def dekor(funkcja):
            def wew(*args, **kwargs):
                true_arg = []
                if arg == [4, 5]:
                    true_arg = Operacje.argumentySuma
                elif arg == [4, 5, 6]:
                    true_arg = Operacje.argumentyRoznica
                list_from_tuple = list(args)
                list_from_tuple.pop(0)
                for i in range(len(true_arg)):
                    list_from_tuple.append(true_arg[i])
                print(list_from_tuple)
                args = tuple(list_from_tuple)
                x = funkcja(*args, **kwargs)
                return x
            return wew
        return dekor

    @argumenty(argumentySuma)
    def suma(*args):
        print("%d+%d+%d=%d" % (args[0], args[1], args[2], args[0]+args[1]+args[2]))
        try:
            return args[3]
        except IndexError:
            return 0

    @argumenty(argumentyRoznica)
    def roznica(*args):
        print("%d-%d=%d" % (args[0], args[1], args[0]-args[1]))
        try:
            return args[2]
        except IndexError:
            return 0



#
op = Operacje()
op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
op.suma(1, 2)     # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
op.suma(1)        # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# # op.suma()         # TypeError: suma() takes exactly 3 arguments (2 given)
op.roznica(2, 1)  # Wypisze: 2-1=1
op.roznica(2)     # Wypisze: 2-4=-2
wynik = op.roznica()  # Wypisze: 4-5=-1
print(wynik)      # Wypisze: 6
#
# # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
# op['suma'] = [1, 2]
# # oznacza, że   argumentySuma=[1,2]
#
# # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
# op['roznica'] = [1, 2, 3]
# # oznacza, że   argumentyRoznica=[1,2,3]
op.suma(1, 2)
op = Operacje()
print(Operacje.argumentyRoznica)
print(Operacje.argumentySuma)
op['suma'] = [1, 2]
op['roznica'] = [1, 2, 3]
print(Operacje.argumentyRoznica)
print(Operacje.argumentySuma)
op.suma(1)
op.roznica(2)
