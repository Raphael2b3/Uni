
class Zufallsexperiment:
    elementarWS = {}
    elementarereignisse = []

    def __init__(self, e_ereignisee=None, elementarWS=None, p=None, zufallsgröße=None, max_zufallsgr=1):
        self.elementarereignisse = e_ereignisee
        self.elementarWS = elementarWS if elementarWS else {}
        self.max_zufallsgr = max_zufallsgr
        if p:
            self.elemWSvon = p
        if zufallsgröße:
            self.zufallsgröße = zufallsgröße

    def zufallsgröße(self):
        print("Keine Zufallsgröße angegeben")

    def punktWSzufallsGröße(self, zufallGr):
        out = 0
        for eEregnis in self.elementarWS:
            if self.zufallsgröße(eEregnis) == zufallGr:
                out += self.elemWSvon(eEregnis)
        return out

    def verteilFunkZufallsGrößeBis(self, zufallGr):

        print("verteilFunkZufallsGröße Bis", zufallGr)
        out = 0
        for z in range(zufallGr + 1):
            pi = self.punktWSzufallsGröße(z)
            print(f"fx({z})=", pi)
            out += pi
            print(f"Fx({z})=", out)
            print()
        return out

    def verteilFunkZufallsGrößeAb(self, zufallGr=0):
        print("verteilFunkZufallsGrößeAb", zufallGr)
        out = 0
        for z in range(zufallGr, self.max_zufallsgr + 1):
            pi = self.punktWSzufallsGröße(z)
            print(f"fx({z})=", pi)
            out += pi
            print(f"Fx({z})=", out)
            print()
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
        print("A", A)
        for aa in A:
            print("aa", aa)
            p = 1
            for a in aa:
                p *= self.elemWSvon(a)
                print("p", p)
            out += p
        return out

    def erwartungswert_mü(self, gx=None):
        # mü , u
        out = 0
        for i in range(self.max_zufallsgr + 1):
            out += self.punktWSzufallsGröße(i) * (i if not gx else gx(i))
        return out

    def varianz_sigmaQuadrat(self):  # mü , u

        erwartWert = self.erwartungswert_mü()
        print("Erwartungswert mü = ", erwartWert)
        out = self.erwartungswert_mü(lambda x: (x - erwartWert) ** 2)
        print("Varianz sigma^2=", out)

        return out

    def standartabweichung_sigma(self):
        t = self.varianz_sigmaQuadrat()

        print("Standartabweichung sigma=", t ** 0.5)

        return t ** 0.5


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
    WSs = {}

    def permutateereeignisse(n, currentWS=1, p_ereigniss=""):
        if n == 0:
            WSs[p_ereigniss] = currentWS
            return
        for e in ereignisse:
            permutateereeignisse(n - 1, currentWS * experiment.elemWSvon(e), p_ereigniss + e)

    permutateereeignisse(züge)

    return Zufallsexperiment(e_ereignisee=list(WSs.keys()), elementarWS=WSs, zufallsgröße=experiment.zufallsgröße,
                             max_zufallsgr=züge)


if __name__ == '__main__':
    ps = [0.25216,0.37511,0.37273]

    out = ps[0]+ ps[1]
    print(out)