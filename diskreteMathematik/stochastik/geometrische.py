from math import factorial

import binomialverteiltesExperiment

class Geometrische:
    def __init__(self,p_success):
        self.p = p_success

    def zufallsgröße(self,x):
        return (1-self.p)**(x-1)*self.p


class Poisson:
    def __init__(self,lambda_):
        self.l = lambda_

    def zufallsgröße(self,x):
        return (self.l**x)*2.71828**(-self.l)/ factorial(x)
tore = 90/43
p = Poisson(tore)
a = p.zufallsgröße(0)
b= p.zufallsgröße(1)
print(a,b,1-a-b)