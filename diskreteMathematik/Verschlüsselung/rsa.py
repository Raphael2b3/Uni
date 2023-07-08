import ggT
from decoding import *
import decoding


def phi(n, primfaktorzerl):
    for p in primfaktorzerl:
        n*=(1-1/p)
    return n

def phiprime(P, Q):
    return (P - 1) * (Q - 1)

def generate_keys(p=79,q=139):

    PHI = phiprime(p, q)
    N = p * q
    e = 29
    # wähle e < phi(p, q) wobei e Teiler fremd zu N
    while True:
        if ggT.ggT(e, PHI) == 1:
            break
        e += 1

    _, (__, d) = ggT.erweiterter_euklid(PHI, e)

    d = d % PHI
    print("p", p, "    q", q, "  N", N, "   phi", PHI, "    e", e, "   d", d)
    return e, d, N


def decode(_e, _N, wort= "DECKMANTEL", split=2):
    nums = str2nums(wort, split)
    rec = nums2str(nums)

    print(nums, rec, wort)

    # 3*11067 %33200
    chiffrats = [num ** _e % _N for num in nums]
    print(chiffrats, "[num**e % N for num in nums]")
    return chiffrats

decoding.set(ord("@"), ord("Z")) # @ = Leertaste
if __name__ == '__main__':

    generate_keys(79, 109)
    c = decode(_e=35, _N=8611, wort="DATENBASIS")
    print(c)
