import math


class Zerlegung:

    def __init__(self, zerleger, potenz, rest):
        self.rest = rest
        self.zerleger = zerleger
        self.potenz = potenz


# Euklidischem Algorithmus
def teiler_fremd(a, b):
    pass


def zerlegung_mit(zahl, zerlgr):
    potenz = 0
    while True:
        if zahl % zerlgr != 0:
            break
        potenz += 1
        zahl /= zerlgr

    return Zerlegung(zerlgr, potenz, zahl)


def generate_primzahlen(bis=100):
    all = [i for i in range(2, bis + 1)]
    locked = 0
    while locked + 1 < len(all):
        mabyprim = all[locked + 1]

    pass


def proof_prim(prim):
    goal = int(math.sqrt(prim))


"""Miller Rabin Primzahltest"""


def probably_prim(prim):
    t = prim - 1

    pass
