import ggT
from decoding import *
import decoding


def phi(n, primfaktorzerl):
    for p in primfaktorzerl:
        n*=(1-1/p)
    return n

def phiprime(P, Q):
    return (P - 1) * (Q - 1)

def generate_keys(p=47,q=61):

    PHI = phiprime(p, q)
    N = p * q
    e = 13
    # wähle e < phi(p, q) wobei e Teiler fremd zu N
    while True:
        if ggT.ggT(e, PHI) == 1:
            break
        e += 1

    _, (__, d) = ggT.erweiterter_euklid(PHI, e)

    d = d % PHI
    print("p", p, "    q", q, "  N", N, "   phi", PHI, "    e", e, "   d", d)
    return e, d, N

def decodeString(_e,_N, wort,split = 2):
    nums = str2nums(wort, split)
    test = nums2str(nums)
    print(nums, test, wort)
    return decode(_e, _N, nums)

def decode(_e, _N, m):
    # 3*11067 %33200
    chiffrats = [(num ** _e) % _N for num in m]
    print(chiffrats, "[num**e % N for num in nums]")
    return chiffrats

decoding.set(ord("@"), ord("Z")) # @ = Leertaste
if __name__ == '__main__':

    e,d,N = generate_keys()

    c = decodeString(_e=e, _N=N, wort="DISKRETE@MATHE")
    c1 = decoding.nums2str(c)
    print(c1)
    m = decode(_e=d,_N=N,m=c)
    m = decoding.nums2str(m)
    print(m)


