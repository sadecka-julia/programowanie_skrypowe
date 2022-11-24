from inspect import signature

def argumenty(*args, **kwargs):
    def wynik(funkcja):
        decList = []
        decList += args[0]
        parLen = len(signature(funkcja).parameters) - 1

        def wrapper(self, *args, **kwargs):
            remaining = 0
            finalArgs = []
            finalArgs += args
            if ([len(args) < parLen]):
                remaining = parLen - len(args)
            if remaining > 0:
                finalArgs += decList[:remaining]
            string = funkcja(self, *finalArgs)
            if type(string) == tuple:
                if (len(string) > 1):
                    return string[1]
            out = 0
            if len(decList) > remaining:
                out = decList[remaining]
            else:
                out = decList[-1]
            return (string, out)

        return wrapper

    return wynik


class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __setitem__(self, key, value):
        if (key == "suma"):
            self.argumentySuma = value
        elif (key == "roznica"):
            self.argumentyRoznica = value

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        return ("%d+%d+%d=%d" % (a, b, c, a + b + c))

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        return ("%d-%d=%d" % (x, y, x - y))
