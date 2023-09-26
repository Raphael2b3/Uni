import gdi.konvertierung as kon
"""
A  B  C  D  E  F
10 11 12 13 14 15
"""


def a():
    codepunkt = [2, 3, 2, 12]
    r = kon.hex2bin(codepunkt)
    print("Binäre darstellung:", r )

    print("präfixe wenn in ascii bereich (007F)- Startbit ist 0")

    print("präfixe n 1en wobei n die anzahl der benötigten bytes")
    print("folgebytes starten mit 10")

def b():
    print("""
    UTF-8 Erfüllt Fano Bedingung, da kein Codewort Präfix eines anderen ist, Aufgrund von Nutzung von präfixen
    UTF-16 erfüllt die fano bedinung
    UTF-32 Erfüllt Fano Bedingung, da kein Codewort Präfix eines anderen sein kann, auf grund fester länge
    """)

def c():
    # https://de.wikipedia.org/wiki/UTF-16
    print("""
    UTF-16
    Unicode-Zeichen außerhalb der BMP (d. h. U+10000 bis U+10FFFF)
    D83EDD14
    """)

if __name__ == '__main__':
    a()
    b()
    c()
