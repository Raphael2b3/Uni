"""
Binomial verteilung

Exponential verteilung



"""



class Kugel:

    def __init__(self, id, wahrscheinlichkeit):
        self.id = id
        self.wahrscheinlichkeit = wahrscheinlichkeit


class VersuchMitZurückLegen:
    def __init__(self, ziehungen, menge, focus):
        self.ziehungen = ziehungen
        self.menge = menge
        self.focus = focus

    def erwartungswert(self, focus=None):
        if focus is None: focus = self.focus
        print("mü von x")

    def varianz(self):
        pass

    def verschiebungssatz(self):
        pass

    def baum(self, b, p=1, n=0):
        if n > self.ziehungen: return b
        b[0] = p
        for o in self.menge:
            b.append(self.baum([], p * o.wahrscheinlichkeit, n + 1))
        return b

    def baumdurchsuchen(self, baum, tiefe, erwartung, ziel):
        baum


print("Possion Verteilung")

print("Wahrscheinlichkeitsdichtefunktion")


def häfuigkeit(liste):
    out = {}
    for i in liste:
        if not i in out.keys():
            out[i] = 1
        out[i] += 1
    return out


class Exponentialverteilung:

    def __init__(self, lambda_):
        self.l = lambda_

    def zufallsgröße(self, x):
        return self.l * 2.71828 ** (-self.l * x)

    def erwartungswert(self):
        return 1 / self.l

    def zwischen(self, a, b):
        return self.zufallsgröße(b) - self.zufallsgröße(a)

    def varianz(self):
        return 1 / self.l ** 2

ex = Exponentialverteilung