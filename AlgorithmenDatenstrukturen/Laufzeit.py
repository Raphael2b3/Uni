import math

import Mathfunctiongenerator
from laufzeitvergleich import *


def laufzeitOrdnung():
    msg = """LAUFZEIT Ordnung: \nDie Laufzeit P(n) ist in einer Funktion das am schnellsten Wachsende Polynom ohne Konstanten
             \ndie Ordnung ist in etwa 8, log(n), sqrt(n), n, n*log(n), n^2, n^3, 2^n
           """
    print(msg)


def laufzeitvergleichProgram():
    g = input("Funktion g(x): ")
    f = input("Funktion f(x): ")
    lzvgl = Laufzeitvergleich(gstr=g, fstr=f)
    print(lzvgl)


if __name__ == '__main__':
    x = 20.0
    f = 2**x+math.cos(x)+math.e**x-math.log(x, 4)
    function = "2 ** x + math.cos(x) + math.e ** x - math.log(x, 4)"
    g = Mathfunctiongenerator.str_to_func(function)

    print(f,g(x))

    #laufzeitOrdnung()
    #laufzeitvergleichProgram()
