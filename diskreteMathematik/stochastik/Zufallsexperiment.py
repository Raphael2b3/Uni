from _distutils_hack import override


class Zufallsexperiment:
    elementarWS = {}
    elementarereignisse = []

    def __init__(self, e_ereignisee, elementarWS, p=None, zufallsgröße=None):
        self.elementarereignisse = e_ereignisee
        self.elementarWS = elementarWS
        if p:
            self.elemWSvon = p
        if zufallsgröße:
            self.zufallsgröße = zufallsgröße

    def zufallsgröße(self):
        print("Keine Zufallsgröße geseted")

    def punktWSzufallsGröße(self, zufallGr):
        out = 0
        for eEregnis in self.elementarWS:
            if self.zufallsgröße(eEregnis) == zufallGr:
                out += self.elementarWS[eEregnis]
        return out

    def verteilungsFunktionZufallsGröße(self, zufallGr):
        out = 0
        for z in range(zufallGr + 1):
            pi = self.punktWSzufallsGröße(z)
            print(f"X({z})=", pi)
            out += pi
        return out

    def elemWSvon(self, w):  # w ist elementar
        return self.elementarWS.get(w, 0)  # if doesn't exist: 0

    def WSvonEreignisse(self, A):
        p = 0
        for a in A:
            p += self.elemWSvon(a)
        return p

    def mehrfachziehenEreignis(self, A):
        out = 0
        for aa in A:
            p = 1
            for a in aa:
                p *= self.elemWSvon(a)
            out += p
        return out


class LaplaceExperiment(Zufallsexperiment):
    """
    mit zurücklegen

    """

    def __init__(self, ereignisse):
        self.elementarereignisse = ereignisse
        self.generateElemWS(ereignisse)  # side Effekt!!!

    def generateElemWS(self, ereignisse):
        for ereignis in ereignisse:
            self.elementarWS[ereignis] = self.elemWSvon(ereignis) + 1 / len(ereignisse)


class LaplaceOhneZurücklegen(LaplaceExperiment):
    """
    ohne zurücklegen
    """

    def __init__(self, ereignisse):
        super().__init__(ereignisse)
        self.currentEreignisse = ereignisse[:]

    def weglegen(self, a):
        self.currentEreignisse.remove(a)
        self.generateElemWS(self.currentEreignisse)

    def reset(self):
        self.currentEreignisse = self.elementarereignisse[:]
        self.generateElemWS(self.elementarereignisse)

    def mehrfachziehenEreignis(self, A):
        out = 0
        for aa in A:
            p = 1
            for a in aa:
                p *= self.elemWSvon(a)
                self.weglegen(a)
            out += p
            self.reset()
        return out


def convert_2_NmalZiehenZufallsExperiment(züge, experiment: Zufallsexperiment):
    ereignisse = experiment.elementarereignisse
    elementarWS = experiment.elementarWS
    WSs = {}

    def permutateereeignisse(n, currentWS=1, p_ereigniss=""):
        if n == 0:
            WSs[p_ereigniss] = currentWS
            return
        for e in ereignisse:
            permutateereeignisse(n - 1, currentWS * elementarWS[e], p_ereigniss + e)

    permutateereeignisse(züge)

    return Zufallsexperiment(e_ereignisee=list(WSs.keys()), elementarWS=WSs, zufallsgröße=experiment.zufallsgröße)


if __name__ == '__main__':
    import Mengen


    def kRG3ZufallsGröße(ereig):
        # anzahl gezogener Grüner Kugeln
        out = 0
        for i in ereig:
            if i == "g":
                out += 1
        return out


    kugelRG = Zufallsexperiment(["r", "g"], elementarWS={"r": 7 / 10, "g": 3 / 10}, zufallsgröße=kRG3ZufallsGröße)
    kugelRG_3mal = convert_2_NmalZiehenZufallsExperiment(3, kugelRG)
    kugelRG_3mal.verteilungsFunktionZufallsGröße(3)
