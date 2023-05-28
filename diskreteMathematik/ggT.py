def ggT(a, b): # a=3 b = 31
    gr = max((a, b))
    kl = min((a, b))

    q = gr // kl
    r = gr % kl
    print(f"{gr} = {q} * {kl} + {r}")
    return kl if r == 0 else ggT(kl, r)


def s_t(a, b, ggt):
    pass


def multiplikativ_inverse(a, b, history):
    gr = max((a, b))
    kl = min((a, b))

    q = gr // kl
    r = gr % kl
    print(f"{gr} = {q} * {kl} + {r}")
    if r == 0:
        return kl, gr, 0
    else:
        (r1, q1, p1) = multiplikativ_inverse(kl, r, history)
        return r1, q

if __name__ == '__main__':
    print(ggT(15, 11))
