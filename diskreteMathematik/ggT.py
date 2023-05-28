def ggT(a, b):  # a=3 b = 31
    gr = max((a, b))
    kl = min((a, b))

    q = gr // kl
    r = gr % kl
    print(f"{gr} = {q} * {kl} + {r}")
    return kl if r == 0 else ggT(kl, r)


def s_t(a, b, ggt):
    pass


def erweiterter_euklid(a, b, history=None):
    if history is None:
        gr = max((a, b))
        kl = min((a, b))
        return erweiterter_euklid(gr, kl, [[0, 0], [0, 1], None])

    q = a // b
    r = a % b

    temp = True
    if history[2] is None:
        history[2] = [1, -q]
        temp = False

    a1, a2 = history[0]
    history[0] = history[1].copy()
    history[1] = history[2].copy()

    if temp:
        history[2][0] *= -q
        history[2][1] *= -q

    history[2][0] += a1
    history[2][1] += a2
    if r == 0:
        return b, history[1]
    print(f"{a}={q}*{b}+{r} | {r}={a}-{q}*{b} | s={history[2][0]} t={history[2][1]}")
    return erweiterter_euklid(b, r, history)


if __name__ == '__main__':
    a, b = 111, 100,
    ggt, (s, t) = erweiterter_euklid(a, b)
    print(f"{ggt} = {s}*{a} + {t}*{b} = {s * a + t * b}")
