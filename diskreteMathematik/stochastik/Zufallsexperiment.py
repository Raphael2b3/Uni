from _distutils_hack import override


class Zufallsexperiment:
    elementarWS = {}
    elementarereignisse = []

    def __init__(self, e_ereignisee, elementarWS, p=None):
        self.elementarereignisse = e_ereignisee
        self.elementarWS = elementarWS
        if p:
            self.WSvon = p

    def WSvon(self, w): # w ist elementar
        return self.elementarWS.get(w,0)  # if doesn't exist: 0

    def WSvonSumme(self,A):
        p = 0
        for a in A:
            p += self.WSvon(a)
        return p

    def mehrfachziehenEreignis(self, A):
        out = 0
        for aa in A:
            p = 1
            for a in aa:
                p *= self.WSvon(a)

            out += p

        return out


class LaplaceExperiment(Zufallsexperiment):
    """
    mit zurücklegen

    """


    def __init__(self, ereignisse):
        self.elementarereignisse = ereignisse
        self.generateElemWS(ereignisse) # side Effekt!!!


    def generateElemWS(self,ereignisse):
        for ereignis in ereignisse:
            self.elementarWS[ereignis] = self.WSvon(ereignis) +1/len(ereignisse)


class LaplaceOhneZurücklegen(LaplaceExperiment):
    """
    ohne zurücklegen
    """

    def __init__(self, ereignisse):
        super().__init__(ereignisse)
        self.currentEreignisse = ereignisse[:]

    def weglegen(self,a):
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
                p *= self.WSvon(a)
                self.weglegen(a)
            out += p
            self.reset()
        return out


if __name__ == '__main__':
    import Mengen

    würfelexperiment = LaplaceExperiment(range(1,7))
    A1 = [ *([5,i] for i in range(1,7)), *([6,i] for i in range(1,7))]  # min eine 5 im ersten wurf

    A2 = [*([i, 5] for i in range(1, 7)), *([i, 6] for i in range(1, 7))]  # min eine 5 im ersten wurf

    A1andA2 = Mengen.schnitt(A1,A2)
    p1 = würfelexperiment.mehrfachziehenEreigniss(A1)
    p2 = würfelexperiment.mehrfachziehenEreigniss(A2)
    p3 = würfelexperiment.mehrfachziehenEreigniss(A1andA2)

    #mind eine 5
    sus = p1+p2- p3
    print(sus)