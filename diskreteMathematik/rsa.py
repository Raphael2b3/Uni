import ggT

start = ord("A")
ende = ord("Z") + 1
dif = ende - start


def keyvalue(c):
    return ord(c) - start + 1


def phi(P, Q):
    return (P - 1) * (Q - 1)


wort = "MY_NAME_IS_BOB"
e = 107
p, q = 37, 71
PHI = phi(p, q)
N = p * q

# wähle e < phi(p, q) wobei e Teiler fremd zu N

while True:
    if ggT.ggT(e, N) == 1:
        break
    e += 1

print("e", e)
ggT.multiplikativ_inverse(e, PHI, [])
