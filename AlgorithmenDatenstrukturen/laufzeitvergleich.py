import Mathfunctiongenerator

BIGNUM = 10000000


def o(f, g):
    return abs(f) <= abs(g)


def omega(f, g):
    return abs(f) >= abs(g)


def big(method, Gfunc, Ffunc):
    for c in range(1, 100):
        for n0 in range(200, 300):
            trynext = False
            success = False
            for n in range(n0, n0 + 100):
                tmp = method(Ffunc(n), c * Gfunc(n))
                if success and not tmp:
                    trynext = True
                success = tmp
            if not trynext and success:
                return {"c": c, "n0": n0}
    return None


def small(method, Gfunc, Ffunc):
    for n0 in range(200, 300):
        tryagain = False
        success = True
        for c in range(50, 100):
            for n in range(n0, n0 + 100):
                tmp = method(Ffunc(n), c * Gfunc(n))
                if not tmp:
                    tryagain = True
                    success = False
                    break
            if tryagain: break
        if success: return {"n0": n0}
    return None


class Laufzeitvergleich:
    def __init__(self, fstr, gstr):
        self.fstr = fstr
        self.gstr = gstr
        self.ffunc = Mathfunctiongenerator.str_to_func(fstr)
        self.gfunc = Mathfunctiongenerator.str_to_func(gstr)
        self.lim = self.ffunc(BIGNUM) / self.gfunc(BIGNUM)
        self.bigOmega = big(omega, self.gfunc, self.ffunc)
        self.bigOmega = small(omega, self.gfunc, self.ffunc)

        self.bigO = big(o, self.gfunc, self.ffunc)
        self.smallO = small(o, self.gfunc, self.ffunc)

    def __str__(self):
        str = f"f(x)={self.fstr}; g(x)={self.gstr}\n" + \
              f"limx->inf: f/g ={self.lim}" + \
              f"big Omega={self.bigOmega}" + \
              f"small Omega={self.bigOmega}" + \
              f"big O={self.bigO}" + \
              f"small O+={self.smallO}" + \
              f"Theta = {not self.bigO and not self.bigOmega}"
        return str

